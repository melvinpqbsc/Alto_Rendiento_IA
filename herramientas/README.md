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

## Pedir datos por correo

`enviar_correos.py` manda un correo individual a cada estudiante a partir de una plantilla de `plantillas/`. `pedir_usuario_github.txt` avisa que el curso empieza, pide el usuario de GitHub (por respuesta al correo) y los días disponibles (por un formulario, cuyo enlace se pasa con `--var formulario=...`). Para pedir otra cosa, copia esa plantilla y cambia el texto: la primera línea es el asunto, `{nombre}` es el primer nombre del estudiante, y cualquier columna del CSV o `--var clave=valor` se usa como `{clave}`.

El CSV puede ser la exportación del formulario de inscripción: guárdala en `herramientas/` (por ejemplo `herramientas/inscripcion.csv`, que no se sube porque todos los `.csv` de esta carpeta, salvo los de ejemplo, están en `.gitignore`). Las columnas de correo y nombre se detectan solas; si no, usa `--columna-correo` y `--columna-nombre`.

```bash
python herramientas/enviar_correos.py herramientas/inscripcion.csv herramientas/plantillas/pedir_usuario_github.txt \
    --var fecha_limite="2 de octubre" --var formulario=https://forms.gle/...
```

Eso es una **vista previa**: muestra un correo de ejemplo y la lista de destinatarios, sin enviar nada. Para enviar, agrega `--enviar` (pide confirmación). Cada envío queda en `correos_enviados.csv`: si algo falla a mitad de camino, volver a ejecutar manda solo los que faltan.

**Cuenta que envía: una cuenta de Gmail.** Gmail no acepta tu contraseña normal para enviar desde un script: necesitas una *contraseña de aplicación*.
1. Activa la [verificación en dos pasos](https://myaccount.google.com/signinoptions/two-step-verification) de la cuenta.
2. Crea la contraseña en [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) (16 letras). Guárdala fuera del repositorio.

Una cuenta de Hotmail/Outlook probablemente no sirva, porque Microsoft ya no acepta contraseñas para enviar por SMTP desde cuentas personales.

```bash
export SMTP_USUARIO=tu.cuenta@gmail.com
# SMTP_CLAVE es opcional: si no está, el script pide la contraseña de aplicación al enviar
```

Con las respuestas, completa `estudiantes.csv` (`usuario,nombre,nivel`) y sigue con la sección siguiente.

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
