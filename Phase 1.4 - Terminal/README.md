# Lección 4.1 — Navegación por el sistema

## Objetivos

Al terminar esta lección serás capaz de:

- Navegar por el sistema de archivos desde la terminal.
- Saber siempre en qué carpeta te encuentras.
- Entrar y salir de directorios.
- Listar archivos y carpetas.
- Comprender la estructura del sistema de archivos.


## Qué es la terminal

La **terminal** es una aplicación que permite comunicarte directamente con el sistema operativo mediante **comandos escritos**. En lugar de hacer clic sobre carpetas y archivos, escribes instrucciones.

Ejemplo:

```text
Abrir la carpeta "Documentos"
```

se convierte en:

```bash
cd Documentos
```

Y:

```text
Mostrar los archivos de esta carpeta
```

se convierte en:

```bash
ls
```

## Por qué usar la terminal

La terminal es una herramienta fundamental porque es:

- Más rápida.
- Más precisa.
- Automatizable.
- Imprescindible para herramientas profesionales.

Git, Python, Docker, servidores Linux y muchas otras herramientas se utilizan principalmente desde la terminal.


## El sistema de archivos

Puedes imaginar el sistema de archivos como un árbol de carpetas.

```text
/
│
├── Users
│   └── Rodrigo
│       ├── Documents
│       ├── Downloads
│       ├── Desktop
│       └── DataPortfolio
│
└── Applications
```

Las carpetas contienen otras carpetas, y la terminal te permite moverte por este árbol. Veamos algunos comandos:

1. Dónde estoy: El comando más importante es **`pwd`**, que significa *Print Working Directory*, es decir, *muéstrame la carpeta en la que estoy*. 

    Ejemplo:

```bash
pwd
```

    Resultado:

```text
/Users/rodrigo
```

    En Windows sería algo similar a:

```text
C:\Users\Rodrigo
```

2. Listar archivos y carpetas: utiliza **`ls`**. El comando **no entra** dentro de las carpetas; simplemente muestra su contenido. El resultado sería algo como

```text
Desktop
Documents
Downloads
Pictures
DataPortfolio
```

3. Listado detallado: si quieres más información de la carpeta/archivo, se hace **`ls -l`** y se obtendrá algo parecido a:

```text
drwxr-xr-x Documents
drwxr-xr-x Downloads
-rw-r--r-- notas.txt
```

    Aquí puedes ver:

- Permisos.
- Propietario.
- Grupo.
- Tamaño.
- Fecha de modificación.


4. Ver archivos ocultos: Muchos archivos de configuración comienzan por un punto (`.`). Por ejemplo: `.git, .gitignore, .vscode`. Para mostrarlos, usamos **`ls -a`**. Es un comando muy utilizado cuando trabajes con Git.

5. Entrar en una carpeta: usamos **`cd`**, que significa *Change Directory*. Por ejemplo, `cd Documents` te mete dentro de la carpeta `Documents`. Esto se puede comprobar con `pwd`

6. Subir un nivel: Para volver a la carpeta anterior, se hace **`cd ..`**. Los dos puntos (`..`) representan la **carpeta padre**. Por ejemplo, antes estábamos en la carpeta `/Users/Rodrigo/Documents`. Después de hacer `cd ..` pasamos a `/Users/Rodrigo`

7. Ir a tu carpeta personal: Existe un atajo muy útil para ir al directorio personal `/Users/Rodrigo`, que es **`cd ~`**

9. Autocompletado: esta es una de las funciones más útiles, y se activa pulsando el tabulador

10. Limpiar la pantalla: Cuando la terminal tenga demasiada información, se puede escribir **`clear`** o simplemente `command + K` para limpiarla totalmente


## Resumen de comandos

| Comando | Función |
|----------|----------|
| `pwd` | Mostrar la carpeta actual |
| `ls` | Listar archivos y carpetas |
| `ls -l` | Mostrar información detallada |
| `ls -a` | Mostrar archivos ocultos |
| `cd carpeta` | Entrar en una carpeta |
| `cd ..` | Subir un nivel |
| `cd ~` | Ir al directorio personal |
| `clear` | Limpiar la pantalla |

## Errores comunes

- Escribir mal el nombre

```bash
cd Documnts
```

Resultado:

```text
No such file or directory
```

- Intentar entrar en una carpeta inexistente: aparecerá un mensaje de error.
- No saber dónde estás
