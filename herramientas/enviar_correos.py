"""Envía un correo individual a cada estudiante a partir de una plantilla.

    python herramientas/enviar_correos.py inscripcion.csv herramientas/plantillas/pedir_usuario_github.txt \\
        --var fecha_limite="2 de octubre" \
        --var formulario_github=https://forms.gle/... --var formulario_horarios=https://forms.gle/...   # vista previa
    python herramientas/enviar_correos.py ... --enviar    # envía (pide confirmación)

El CSV puede ser la exportación del formulario de inscripción: las columnas de
correo y nombre se detectan solas ("correo"/"email", "nombre"), o se indican con
--columna-correo y --columna-nombre.

La plantilla es un archivo de texto: la primera línea es "Asunto: ...", después una
línea vacía y el cuerpo. {nombre} se reemplaza por el primer nombre del estudiante ("estudiante" si falta);
cualquier otra columna del CSV o --var clave=valor también se puede usar como {clave}.

Cada correo enviado queda en herramientas/correos_enviados.csv: si el envío se corta,
volver a ejecutar solo manda los que faltan (--reenviar para mandar todos otra vez).

Configuración del servidor (variables de entorno):
    SMTP_USUARIO   cuenta de Gmail que envía, p. ej. curso.ia@gmail.com (obligatoria)
    SMTP_CLAVE     contraseña de aplicación; si falta, se pide al enviar
    SMTP_NOMBRE    nombre del remitente (por defecto, "Melvin Poveda")
    SMTP_SERVIDOR  por defecto smtp.gmail.com
    SMTP_PUERTO    por defecto 587
"""

import argparse
import csv
import getpass
import os
import re
import smtplib
import ssl
import sys
import time
from datetime import datetime
from email.message import EmailMessage
from email.utils import formataddr, formatdate, make_msgid
from pathlib import Path

REGISTRO = Path(__file__).parent / "correos_enviados.csv"
CORREO_VALIDO = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def leer_plantilla(ruta):
    texto = Path(ruta).read_text(encoding="utf-8")
    primera, _, cuerpo = texto.partition("\n")
    if not primera.lower().startswith("asunto:"):
        sys.exit(f"{ruta}: la primera línea debe ser 'Asunto: ...'")
    return primera.split(":", 1)[1].strip(), cuerpo.lstrip("\n")


def elegir_columna(encabezados, pedida, pistas, que):
    if pedida:
        if pedida not in encabezados:
            sys.exit(f"No existe la columna '{pedida}'. Columnas: {encabezados}")
        return pedida
    candidatas = [h for h in encabezados if any(p in h.lower() for p in pistas)]
    if len(candidatas) != 1:
        sys.exit(f"No pude detectar la columna de {que} (candidatas: {candidatas}). "
                 f"Indícala con --columna-{que}. Columnas: {encabezados}")
    return candidatas[0]


def leer_destinatarios(ruta, col_correo, col_nombre):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        lector = csv.DictReader(f)
        encabezados = [h.strip() for h in lector.fieldnames or []]
        filas = [{k.strip(): (v or "").strip() for k, v in fila.items() if k} for fila in lector]
    col_correo = elegir_columna(encabezados, col_correo, ("correo", "email", "e-mail"), "correo")
    col_nombre = elegir_columna(encabezados, col_nombre, ("nombre",), "nombre")

    destinatarios, vistos = [], set()
    for fila in filas:
        correo = fila.get(col_correo, "").lower()
        if not correo:
            continue
        if not CORREO_VALIDO.match(correo):
            print(f"⚠ correo inválido, se omite: {correo!r}")
            continue
        if correo in vistos:  # el formulario puede tener respuestas repetidas
            continue
        vistos.add(correo)
        completo = fila.get(col_nombre, "")
        datos = dict(fila, correo=correo, nombre_completo=completo,
                     nombre=completo.split()[0].capitalize() if completo else "estudiante")
        destinatarios.append(datos)
    return destinatarios


def rellenar(texto, datos):
    try:
        return texto.format_map(datos)
    except KeyError as e:
        sys.exit(f"La plantilla usa {{{e.args[0]}}} pero no hay columna ni --var con ese nombre.")


def ya_enviados(plantilla):
    if not REGISTRO.exists():
        return set()
    with open(REGISTRO, encoding="utf-8", newline="") as f:
        return {fila["correo"] for fila in csv.DictReader(f) if fila["plantilla"] == plantilla}


def anotar(correo, plantilla):
    nuevo = not REGISTRO.exists()
    with open(REGISTRO, "a", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f)
        if nuevo:
            escritor.writerow(["fecha", "correo", "plantilla"])
        escritor.writerow([datetime.now().isoformat(timespec="seconds"), correo, plantilla])


def conectar():
    usuario = os.environ.get("SMTP_USUARIO")
    if not usuario:
        sys.exit("Falta SMTP_USUARIO (la cuenta que envía). Ver herramientas/README.md.")
    servidor = os.environ.get("SMTP_SERVIDOR", "smtp.gmail.com")
    puerto = int(os.environ.get("SMTP_PUERTO", "587"))
    local = servidor in ("localhost", "127.0.0.1")

    smtp = smtplib.SMTP_SSL(servidor, puerto, context=ssl.create_default_context()) if puerto == 465 \
        else smtplib.SMTP(servidor, puerto)
    smtp.ehlo()
    if puerto != 465:
        if smtp.has_extn("starttls"):
            smtp.starttls(context=ssl.create_default_context())
            smtp.ehlo()
        elif not local:
            sys.exit(f"{servidor} no ofrece conexión cifrada (STARTTLS): no envío la contraseña.")
    if not local:
        clave = os.environ.get("SMTP_CLAVE") or getpass.getpass(f"Contraseña de aplicación de {usuario}: ")
        smtp.login(usuario, clave)
    return smtp, usuario


def armar(remitente, destinatario, asunto, cuerpo):
    msg = EmailMessage()
    msg["From"] = formataddr((os.environ.get("SMTP_NOMBRE", "Melvin Poveda"), remitente))
    msg["To"] = destinatario
    msg["Subject"] = asunto
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain=remitente.split("@")[-1])
    msg.set_content(cuerpo)
    return msg


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv", help="CSV con los estudiantes (p. ej. la exportación del formulario de inscripción)")
    parser.add_argument("plantilla", help="archivo de plantilla (ver herramientas/plantillas/)")
    parser.add_argument("--var", action="append", default=[], metavar="CLAVE=VALOR", help="valor extra para la plantilla")
    parser.add_argument("--columna-correo", help="nombre exacto de la columna de correo")
    parser.add_argument("--columna-nombre", help="nombre exacto de la columna de nombre")
    parser.add_argument("--enviar", action="store_true", help="enviar de verdad (sin esto solo muestra una vista previa)")
    parser.add_argument("--reenviar", action="store_true", help="incluir a quienes ya recibieron esta plantilla")
    args = parser.parse_args()

    extras = {}
    for v in args.var:
        clave, sep, valor = v.partition("=")
        if not sep:
            sys.exit(f"--var debe ser CLAVE=VALOR, no {v!r}")
        extras[clave.strip()] = valor.strip()

    asunto_t, cuerpo_t = leer_plantilla(args.plantilla)
    destinatarios = leer_destinatarios(args.csv, args.columna_correo, args.columna_nombre)
    nombre_plantilla = Path(args.plantilla).name
    enviados = set() if args.reenviar else ya_enviados(nombre_plantilla)
    pendientes = [d for d in destinatarios if d["correo"] not in enviados]

    # Se rellenan todos antes de enviar el primero: un error en la plantilla no deja envíos a medias
    correos = [(d["correo"], rellenar(asunto_t, {**d, **extras}), rellenar(cuerpo_t, {**d, **extras})) for d in pendientes]
    sin_nombre = [d["correo"] for d in pendientes if not d["nombre_completo"]]

    print(f"{len(destinatarios)} estudiantes en el CSV, {len(destinatarios) - len(pendientes)} ya recibieron "
          f"'{nombre_plantilla}', {len(correos)} por enviar.")
    if sin_nombre:
        print(f"⚠ Sin nombre (se saluda con \"estudiante\"): {', '.join(sin_nombre)}")
    if not correos:
        return
    correo, asunto, cuerpo = correos[0]
    print(f"\n--- Ejemplo: para {correo} ---\nAsunto: {asunto}\n\n{cuerpo}---")
    print("Destinatarios:", ", ".join(c for c, _, _ in correos))

    if not args.enviar:
        print("\nVista previa: no se envió nada. Agrega --enviar para enviar.")
        return
    if input(f"\n¿Enviar {len(correos)} correos? Escribe 'si' para confirmar: ").strip().lower() not in ("si", "sí"):
        print("Cancelado.")
        return

    smtp, remitente = conectar()
    with smtp:
        for i, (correo, asunto, cuerpo) in enumerate(correos, 1):
            try:
                smtp.send_message(armar(remitente, correo, asunto, cuerpo))
            except smtplib.SMTPException as e:
                print(f"✗ {correo}: {e}. Vuelve a ejecutar para reintentar los que faltan.")
                return
            anotar(correo, nombre_plantilla)
            print(f"✓ {i}/{len(correos)} {correo}")
            time.sleep(1)  # Gmail limita la velocidad de envío
    print("Listo.")


if __name__ == "__main__":
    main()
