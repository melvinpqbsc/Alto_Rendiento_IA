"""Acceso mínimo a la API de GitHub, solo con la biblioteca estándar.

Lo usan crear_repos.py y recolectar_entregas.py. El token se lee de la
variable de entorno GITHUB_TOKEN (ver herramientas/README.md).
"""

import csv
import json
import os
import sys
import urllib.error
import urllib.request

ORG = "Alto-Rendimiento-IA"
API = os.environ.get("GITHUB_API", "https://api.github.com")


class ErrorGitHub(Exception):
    def __init__(self, estado, mensaje):
        super().__init__(f"HTTP {estado}: {mensaje}")
        self.estado = estado


def token():
    valor = os.environ.get("GITHUB_TOKEN")
    if not valor:
        sys.exit("Falta el token: export GITHUB_TOKEN=... (ver herramientas/README.md)")
    return valor


def pedir(metodo, ruta, datos=None, crudo=False):
    """Hace una petición a la API. Devuelve el JSON (o los bytes si crudo=True); None si la respuesta está vacía."""
    cuerpo = json.dumps(datos).encode() if datos is not None else None
    req = urllib.request.Request(API + ruta, data=cuerpo, method=metodo)
    req.add_header("Authorization", f"Bearer {token()}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if cuerpo is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            contenido = resp.read()
    except urllib.error.HTTPError as e:
        detalle = e.read().decode(errors="replace")
        try:
            detalle = json.loads(detalle).get("message", detalle)
        except ValueError:
            pass
        raise ErrorGitHub(e.code, detalle) from None
    if crudo:
        return contenido
    return json.loads(contenido) if contenido else None


def existe_repo(nombre):
    try:
        pedir("GET", f"/repos/{ORG}/{nombre}")
        return True
    except ErrorGitHub as e:
        if e.estado == 404:
            return False
        raise


def leer_estudiantes(ruta, nivel=None):
    """Lee el CSV de estudiantes (columnas: usuario, nombre, nivel). Ignora filas vacías."""
    with open(ruta, encoding="utf-8", newline="") as f:
        filas = [
            {k.strip(): (v or "").strip() for k, v in fila.items()}
            for fila in csv.DictReader(f)
        ]
    filas = [f for f in filas if f.get("usuario")]
    if nivel:
        filas = [f for f in filas if f.get("nivel", "").lower() == nivel.lower()]
    return filas


def repo_entregas(usuario):
    return f"entregas-{usuario}"
