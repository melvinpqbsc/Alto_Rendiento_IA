# Herramientas del profesor

Cada estudiante tiene un repositorio **privado** de entregas en la organización [Alto-Rendimiento-IA](https://github.com/Alto-Rendimiento-IA): `entregas-<usuario>`. Allí guarda todos sus trabajos, una carpeta por trabajo (`B1/`, `P01/`, `Sprint1/`…). Estos scripts crean esos repositorios y copian su contenido a la hora de entrega. Solo usan la biblioteca estándar de Python (3.12 o más nuevo).

## Configuración inicial (una vez)

1. **Organización**: en *Settings → Member privileges → Base permissions*, elige **No permission**. Así nadie ve repositorios ajenos. Los estudiantes entran como colaboradores de su propio repositorio, no como miembros.
2. **Colab**: abre Colab, *Archivo → Abrir notebook → GitHub*, autoriza y, en la pantalla de autorización de GitHub, pulsa **Grant** junto a *Alto-Rendimiento-IA*. Si no aparece, en *Settings → Third-party access → OAuth application policy* aprueba *Google Colaboratory* (o quita la restricción). Sin esto los estudiantes no pueden guardar desde Colab en sus repositorios.
3. **Token**: crea un *fine-grained personal access token* en [github.com/settings/tokens](https://github.com/settings/personal-access-tokens/new) con *Resource owner* = `Alto-Rendimiento-IA`, acceso a *All repositories* y permisos **Administration: Read and write** y **Contents: Read and write**. Si la organización pide aprobar el token, apruébalo en *Settings → Personal access tokens*. En la terminal:

   ```bash
   export GITHUB_TOKEN=github_pat_...
   ```

4. **Lista de estudiantes**: copia `estudiantes.ejemplo.csv` como `estudiantes.csv` y complétala (`usuario,nombre,nivel`). `estudiantes.csv`, `parejas.csv` y `recolecciones/` están en `.gitignore`: tienen datos personales y no deben subirse al repositorio público.

## Crear los repositorios

```bash
python herramientas/crear_repos.py herramientas/estudiantes.csv --simulacion   # muestra qué haría
python herramientas/crear_repos.py herramientas/estudiantes.csv
```

Crea `entregas-<usuario>` con un README de instrucciones e invita al estudiante con permiso de escritura. Se puede volver a ejecutar cuando se sumen estudiantes: lo que ya existe no se toca. La invitación llega por correo y en [github.com/notifications](https://github.com/notifications); caduca a los 7 días, y volver a ejecutar el script la reenvía.

Para el proyecto final (mayo), con `parejas.csv` (`pareja,usuario1,usuario2`):

```bash
python herramientas/crear_repos.py herramientas/parejas.csv --proyecto
```

## Recolectar las entregas

Al inicio de la clase en que vence un trabajo:

```bash
python herramientas/recolectar_entregas.py herramientas/estudiantes.csv --trabajo P01 --nivel Intermedio
```

Descarga cada repositorio tal como está en ese momento a `herramientas/recolecciones/<fecha_hora>_P01/<usuario>/` y escribe `registro.csv` con el commit, su fecha y si la carpeta `P01/` tiene un notebook. Esa copia es la entrega: lo que se suba después no cuenta, sin depender de las fechas de los commits (que se pueden alterar desde git).
