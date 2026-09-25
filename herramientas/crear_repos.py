"""Crea los repositorios privados de entregas e invita a cada estudiante.

    python herramientas/crear_repos.py herramientas/estudiantes.csv
    python herramientas/crear_repos.py --proyecto herramientas/parejas.csv

Por cada estudiante crea Alto-Rendimiento-IA/entregas-<usuario> (privado, con un
README de instrucciones) y lo invita con permiso de escritura. Con --proyecto crea
Alto-Rendimiento-IA/proyecto-<pareja> e invita a los dos integrantes.

Se puede volver a ejecutar sin problema: los repositorios que ya existen no se
tocan, y las invitaciones se reenvían solo a quien todavía no es colaborador.
"""

import argparse
import base64
import csv

from github_api import ORG, ErrorGitHub, existe_repo, leer_estudiantes, pedir, repo_entregas

README_ENTREGAS = """# Entregas de {usuario}

Repositorio privado: solo lo ven tú y el profesor.

Guarda aquí cada trabajo en su propia carpeta, con el código del cronograma:
`B1/`, `P01/`, `Sprint1/`, etc. Desde Colab: *Archivo → Guardar una copia en GitHub*,
repositorio `{org}/{repo}`, rama `main`, ruta `P01/P01_nombre_del_notebook.ipynb`.

Al inicio de cada clase el profesor copia este repositorio: lo que esté aquí en ese
momento es tu entrega. Instrucciones completas en
https://github.com/melvinpqbsc/Alto_Rendiento_IA#antes-de-empezar-github
"""

README_PROYECTO = """# Proyecto: {pareja}

Repositorio privado compartido por {integrantes} y el profesor.
"""


def crear_repo(nombre, descripcion, readme, simulacion):
    if existe_repo(nombre):
        print(f"  = {ORG}/{nombre} ya existe")
        return
    if simulacion:
        print(f"  + crearía {ORG}/{nombre}")
        return
    pedir("POST", f"/orgs/{ORG}/repos", {
        "name": nombre,
        "description": descripcion,
        "private": True,
        "has_issues": False,
        "has_wiki": False,
        "has_projects": False,
    })
    pedir("PUT", f"/repos/{ORG}/{nombre}/contents/README.md", {
        "message": "Instrucciones de entrega",
        "content": base64.b64encode(readme.encode()).decode(),
    })
    print(f"  + {ORG}/{nombre} creado")


def invitar(nombre, usuario, simulacion):
    if simulacion:
        print(f"    invitaría a {usuario}")
        return
    try:
        respuesta = pedir("PUT", f"/repos/{ORG}/{nombre}/collaborators/{usuario}", {"permission": "push"})
    except ErrorGitHub as e:
        print(f"    ✗ no se pudo invitar a {usuario}: {e}")
        return
    # 201 con cuerpo: invitación nueva; 204 sin cuerpo: ya era colaborador
    print(f"    {'invitación enviada a' if respuesta else 'ya es colaborador:'} {usuario}")


def existe_usuario(usuario):
    try:
        pedir("GET", f"/users/{usuario}")
        return True
    except ErrorGitHub as e:
        if e.estado == 404:
            return False
        raise


def avisar_permiso_base():
    try:
        org = pedir("GET", f"/orgs/{ORG}")
    except ErrorGitHub:
        return
    permiso = org.get("default_repository_permission")
    if permiso not in (None, "none"):
        print(f"⚠ Los miembros de {ORG} tienen permiso base '{permiso}' y pueden ver todos los repositorios.")
        print("  Cámbialo a 'No permission' en Settings → Member privileges → Base permissions.\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv", help="estudiantes.csv (usuario,nombre,nivel) o, con --proyecto, parejas.csv (pareja,usuario1,usuario2)")
    parser.add_argument("--proyecto", action="store_true", help="crear repositorios de proyecto por pareja")
    parser.add_argument("--simulacion", action="store_true", help="mostrar qué haría, sin crear ni invitar nada")
    args = parser.parse_args()

    avisar_permiso_base()

    if args.proyecto:
        with open(args.csv, encoding="utf-8", newline="") as f:
            parejas = [{k.strip(): (v or "").strip() for k, v in fila.items()} for fila in csv.DictReader(f)]
        for p in parejas:
            if not p.get("pareja"):
                continue
            nombre = f"proyecto-{p['pareja']}"
            integrantes = [u for u in (p.get("usuario1"), p.get("usuario2")) if u]
            print(nombre)
            crear_repo(nombre, f"Proyecto final: {', '.join(integrantes)}",
                       README_PROYECTO.format(pareja=p["pareja"], integrantes=" y ".join(integrantes)), args.simulacion)
            for usuario in integrantes:
                invitar(nombre, usuario, args.simulacion)
        return

    for e in leer_estudiantes(args.csv):
        nombre = repo_entregas(e["usuario"])
        print(f"{e['usuario']} ({e.get('nombre', '')}, {e.get('nivel', '')})")
        if not existe_usuario(e["usuario"]):
            print(f"  ✗ no existe el usuario de GitHub '{e['usuario']}': revisa el CSV")
            continue
        crear_repo(nombre, f"Entregas de {e.get('nombre') or e['usuario']}",
                   README_ENTREGAS.format(usuario=e["usuario"], org=ORG, repo=nombre), args.simulacion)
        invitar(nombre, e["usuario"], args.simulacion)


if __name__ == "__main__":
    main()
