"""Copia el estado actual de todos los repositorios de entregas.

    python herramientas/recolectar_entregas.py herramientas/estudiantes.csv --trabajo P01

Ejecutar al inicio de la clase: lo que se descarga en ese momento es la entrega.
Guarda una copia de cada repositorio en herramientas/recolecciones/<fecha_hora>/<usuario>/
y un registro.csv con el commit, su fecha y si está la carpeta del trabajo.
"""

import argparse
import csv
import io
import tarfile
from datetime import datetime
from pathlib import Path

from github_api import ORG, ErrorGitHub, leer_estudiantes, pedir, repo_entregas

DESTINO = Path(__file__).parent / "recolecciones"


def descargar(repo, carpeta):
    """Descarga la rama principal de ORG/repo en carpeta. Devuelve (sha, fecha del último commit)."""
    commit = pedir("GET", f"/repos/{ORG}/{repo}/commits/HEAD")
    datos = pedir("GET", f"/repos/{ORG}/{repo}/tarball/{commit['sha']}", crudo=True)
    carpeta.mkdir(parents=True)
    with tarfile.open(fileobj=io.BytesIO(datos)) as tar:
        for miembro in tar.getmembers():
            # El tarball trae todo dentro de una carpeta <org>-<repo>-<sha>/: se la quitamos
            partes = Path(miembro.name).parts[1:]
            if not partes or not (miembro.isfile() or miembro.isdir()):
                continue
            miembro.name = str(Path(*partes))
            tar.extract(miembro, carpeta, filter="data")
    return commit["sha"], commit["commit"]["committer"]["date"]


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("csv", help="estudiantes.csv (usuario,nombre,nivel)")
    parser.add_argument("--trabajo", help="código del trabajo (P01, B2, Sprint1…): revisa que su carpeta tenga un notebook")
    parser.add_argument("--nivel", help="solo estudiantes de este nivel (Inicial o Intermedio)")
    args = parser.parse_args()

    momento = datetime.now().strftime("%Y-%m-%d_%H%M")
    raiz = DESTINO / (f"{momento}_{args.trabajo}" if args.trabajo else momento)
    registro = []
    for e in leer_estudiantes(args.csv, args.nivel):
        usuario = e["usuario"]
        fila = {"usuario": usuario, "nombre": e.get("nombre", ""), "commit": "", "fecha_commit": "", "estado": ""}
        try:
            fila["commit"], fila["fecha_commit"] = descargar(repo_entregas(usuario), raiz / usuario)
        except ErrorGitHub as err:
            fila["estado"] = f"error: {err}"
        else:
            if args.trabajo:
                notebooks = list((raiz / usuario / args.trabajo).glob("*.ipynb"))
                fila["estado"] = "entregado" if notebooks else "sin entrega"
            else:
                fila["estado"] = "copiado"
        registro.append(fila)
        print(f"{usuario:<24}{fila['estado']:<14}{fila['fecha_commit']}")

    raiz.mkdir(parents=True, exist_ok=True)
    with open(raiz / "registro.csv", "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=list(registro[0]) if registro else ["usuario"])
        escritor.writeheader()
        escritor.writerows(registro)
    print(f"\nCopia guardada en {raiz} (hora de recolección: {momento})")


if __name__ == "__main__":
    main()
