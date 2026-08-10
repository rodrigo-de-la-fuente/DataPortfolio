El flujo de productividad puede resumirse así:

```text
                 TERMINAL
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
   AUTOCOMPLETAR  HISTORIAL   CONTROL
        │           │           │
       TAB      ↑ / ↓ / Ctrl+R  Ctrl+C
        │           │           │
        └───────────┼───────────┘
                    ↓
             TRABAJAR MÁS RÁPIDO
```

Las bases fundamentales del módulo son:

```text
LECCIÓN 4.1
Navegación
    ↓
pwd · ls · cd · ~ · .. · TAB
    ↓
LECCIÓN 4.2
Archivos y carpetas
    ↓
mkdir · touch · cp · mv · rm
    ↓
LECCIÓN 4.3
Rutas y permisos
    ↓
. · .. · ~ · chmod · chown
    ↓
LECCIÓN 4.4
Comandos útiles
    ↓
cat · less · head · tail · find · grep · history
    ↓
LECCIÓN 4.5
Productividad
    ↓
TAB · ↑ ↓ · Ctrl+R · Ctrl+C · Ctrl+L
```


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


# Lección 4.2 — Operaciones con archivos y carpetas

## Objetivos

Al terminar esta lección serás capaz de:

- Crear carpetas.
- Crear archivos.
- Copiar archivos y directorios.
- Mover y renombrar elementos.
- Eliminar archivos y carpetas.
- Entender qué comandos son potencialmente peligrosos.

Al terminar esta lección serás capaz de **crear y gestionar la estructura de cualquier proyecto directamente desde la terminal**. Habrás aprendido las operaciones fundamentales:

```text
CREAR
  ↓
mkdir / touch
  ↓
COPIAR
  ↓
cp
  ↓
MOVER / RENOMBRAR
  ↓
mv
  ↓
ELIMINAR
  ↓
rm / rmdir
```

Estas operaciones serán especialmente útiles cuando combines la terminal con Git, Python, VS Code y la organización profesional de proyectos.

## Operaciones con archivos

### Creación de archivos

- Crear un archivo vacío: El comando más utilizado es `touch <filename>`. Por ejemplo: `touch README.md`.

- Crear varios archivos: Esta acción es especialmente útil al comenzar un proyecto. Para hacerlo usamos un solo comando; por ejemplo, `touch app.py requirements.txt .gitignore`.

### Copiar un archivo

Se usa `cp <origin_file> <destiny_file>`, y el archivo original permanecerá intacto. Por ejemplo, `cp README.md README_backup.md`. Ahora se tendrá:

```text
README.md
README_backup.md
```

### Mover un archivo

El comando es `mv`. Por ejemplo, para pasar el archivo `notas.txt` de la carpeta actual a `docs`, hacemos

```bash
mv notas.txt docs/
```

### Renombrar un archivo

El mismo comando `mv` sirve para cambiar nombres. Por ejemplo,

```bash
mv informe.txt informe_final.txt
```

Aquí no se crea una copia. Simplemente se cambia el nombre del archivo.


### Eliminar un archivo

Para eliminar un archivo usamos el comando `rm`. Por ejemplo,

```bash
rm archivo.txt
```
El archivo desaparecerá. Pero, ⚠️ **importante**: `rm` no mueve el archivo a la papelera sino que elimina directamente el archivo sin posibilidad de recuperación. Por tanto, ojo con este comando porque el archivo no pasa por la papelera de reciclaje, así que antes de usarlo es recomendable comprobar la ubicación del usuario haciendo `pwd` y `ls`.


## Operaciones con carpetas

### Creación de carpetas

- Crear una carpeta: Para crear una carpeta usaremos el comando `mkdir`, que significa *make directory*. El comando completo es `mkdir nombre_carpeta`.

- Crear varias carpetas a la vez: Aquí se usaría también `mkdir`. Simplemente habría que enumerar las carpetas que se quieren crear `mkdir datos notebooks src docs`. El resultado sería una estructura de carpetas como sigue:

```text
datos/
notebooks/
src/
docs/
```

- Crear carpetas anidadas: El comando es un poco más complejo, `mkdir -p proyecto/{data,src,docs}`. La opción `-p` permite crear la estructura de directorios necesaria aunque las carpetas superiores todavía no existan. Se obtendrá la estructura que sigue:

```text
proyecto
├── data
├── docs
└── src
```

### Copiar una carpeta

Para copiar un directorio completo se usa el comando `cp`:

```bash
cp -r carpeta_original copia
```

La opción `-r` significa *recursivo*, es decir, copia la carpeta y todo su contenido, incluyendo sus subcarpetas.

### Renombrar una carpeta

Se puede usar `mv` para cambiar el nombre de una carpeta:

```bash
mv proyecto proyecto_v2
```

### Eliminar carpetas

- Eliminar una carpeta vacía: Para eliminar un directorio vacío se hace `rmdir carpeta`. Este comando solo funciona si la carpeta está vacía.

- Eliminar una carpeta con contenido: Para eliminar una carpeta que contiene archivos o subcarpetas hacemos `rm -r <foldername>`. Esto eliminará la carpeta y todo su contenido gracias a la opción `-r`, que quiere decir `recursive` o recursivo.


## Resumen de comandos

| Comando | Función |
|---|---|
| `mkdir` | Crear una carpeta |
| `mkdir -p` | Crear una estructura de carpetas |
| `touch` | Crear un archivo vacío |
| `cp` | Copiar un archivo |
| `cp -r` | Copiar una carpeta y su contenido |
| `mv` | Mover un archivo o carpeta |
| `mv` | Renombrar un archivo o carpeta |
| `rm` | Eliminar un archivo |
| `rmdir` | Eliminar una carpeta vacía |
| `rm -r` | Eliminar una carpeta y su contenido |

---

## Buenas prácticas

- Comprueba siempre el resultado con `ls`.
- Utiliza nombres descriptivos para archivos y carpetas.
- Antes de borrar algo, verifica dónde estás con `pwd`.
- Ten especial cuidado con `rm -r`.
- Utiliza `TAB` para completar nombres de archivos y carpetas.
- No ejecutes comandos de borrado si no estás seguro de qué elementos afectarán.

---

# Lección 4.3 — Permisos y rutas

## Objetivos

Al terminar esta lección sabrás:

- Distinguir entre rutas absolutas y relativas.
- Comprender qué significan los permisos de un archivo.
- Cambiar permisos básicos.
- Entender el propietario y el grupo de un archivo.
- Interpretar errores relacionados con permisos.

Al terminar esta lección comprenderás dos conceptos fundamentales de la terminal:

```text
RUTAS
│
├── Absolutas
├── Relativas
├── .
├── ..
└── ~
```

y:

```text
PERMISOS
│
├── Propietario
├── Grupo
└── Otros
    │
    ├── r → Leer
    ├── w → Escribir
    └── x → Ejecutar / acceder
```

Estos conceptos serán especialmente importantes cuando trabajes con Git, Python, entornos virtuales, Docker y servidores Linux.


## Qué es una ruta

Una **ruta** o ***path*** indica dónde se encuentra un archivo o una carpeta. Por ejemplo, `/Users/rodrigo/Documents/DataPortfolio/README.md`. Cada carpeta conduce a la siguiente hasta llegar al archivo.

### Ruta absoluta

Una **ruta absoluta** empieza desde la raíz del sistema. En macOS y Linux comienza por `/`, como hemos visto arriba. No importa en qué carpeta te encuentres: esta ruta siempre apunta al mismo lugar.

### Ruta relativa

Una **ruta relativa** parte de la carpeta en la que te encuentras actualmente. Supongamos que estás en `/Users/rodrigo/Documents`. Entonces, para entrar en `DataPortfolio` basta con hacer `cd DataPortfolio` y no se necesita escribir toda la ruta.


## Carpeta actual, padre y personal/raíz

El símbolo `.` representa la carpeta actual. Por ejemplo, `ls .` significa "Lista el contenido de la carpeta actual."

En cambio, el símbolo `..` representa la carpeta que está un nivel por encima. Por ejemplo, `cd ..` sube una carpeta. Si estás en `/Users/rodrigo/Documents`, después de `cd ..` estarás en `/Users/rodrigo`

Finalmente, el símbolo `~` representa el directorio personal. En macOS suele ser `/Users/<diskname>`. Por tanto, `cd ~` lleva directamente a la carpeta personal.


## Combinando rutas relativas

Supongamos que estás aquí:

```text
/Users/rodrigo/Documents/DataPortfolio/src
```

Puedes combinar rutas haciendo:

```bash
cd ../docs
```

Esto significa:

1. Subir un nivel: `cd ..`
2. Entrar en la carpeta `docs`.

Como resultado estaremos en:

```text
/Users/rodrigo/Documents/DataPortfolio/docs
```


## Ver permisos

Para ver información detallada sobre archivos y carpetas usamos `ls -l`. Un ejemplo de resultado sería:

```text
-rw-r--r--  1 rodrigo staff  820 README.md
```

La primera parte representa los permisos: `-rw-r--r--`. Estos se dividen en tres grupos:

```text
rw- | r-- | r--
 ↑      ↑      ↑
Dueño  Grupo  Otros
```

Y cada grupo puede tener tres permisos:

| Símbolo | Significado |
|---|---|
| `r` | Read → leer |
| `w` | Write → escribir/modificar |
| `x` | Execute → ejecutar |
| `-` | Permiso no concedido |


Pero antes de los permisos aparece un carácter que indica el tipo de elemento:

| Símbolo | Significado |
|---|---|
| `d` | Directorio |
| `-` | Archivo normal |
| `l` | Enlace simbólico |

Por ejemplo, en el permiso `drwxr-xr-x` la `d` indica que es un directorio. En cambio, en `-rw-r--r--` no hay nada: indica que es un archivo normal.

 Ejemplo: `drwxr-xr-x`

Descomponemos:

```text
d rwx r-x r-x
│ │   │   │
│ │   │   └── Otros
│ │   └────── Grupo
│ └────────── Propietario
└──────────── Directorio
```

Estamos en un directorio sobre el cual el propietario tiene todos los permisos: lectura (`r`), escritura (`w`) y ejecución (`x`) si lo precisara. En cambio, el grupo (`r-x`) no tiene derechos de escritura, al igual que otros usuarios.

### Qué significa `x` en una carpeta

En un archivo, `x` significa que puede ejecutarse como programa. En un directorio, `x` significa que puedes **acceder a él**. Por ejemplo, sin permiso `x` no podrías entrar normalmente en una carpeta mediante `cd carpeta`

### Cambiar permisos

El comando `chmod` significa ***change mode*** y permite modificar los permisos de un archivo o directorio.

- Añadir permisos: para añadir un permiso se hace `chmod +` seguido de la letra asociada al tipo de permiso que se quiere añadir. Por ejemplo, si quisiéramos añadir permisos de ejecución al archivo `script.h`, haríamos

```bash
chmod +x script.sh
```

Así, si antes los permisos eran `-rw-r--r--`, después quedarán `-rwxr-xr-x`.

- Quitar permisos: También se puede hacer lo contrario, es decir, eliminar un permiso. Para ello se hace `chmod -` seguido de la letra asociada al tipo de permiso que se quiere añadir. Si al archivo anterior quisiéramos quitarle el permiso de ejecución, haríamos

```bash
chmod -x script.sh
```

### Permisos mediante números

Existe otra forma de definir permisos utilizando números. Cada permiso tiene asociado un valor:

| Permiso | Valor |
|---|---:|
| `r` | 4 |
| `w` | 2 |
| `x` | 1 |

Los valores se suman. Por ejemplo, `rwx = 4 + 2 + 1 = 7`, `r-x = 4 + 0 + 1 = 5` y `r-- = 4 + 0 + 0 = 4`, de forma que el código `754` equivale al permiso `rwxr-xr--`

- `chmod 755`. Cuando se ejecuta `chmod 755 script.sh` se está estableciendo `rwx r-x r-x`.

- Otro permiso muy habitual en archivos de texto es `chmod 644`, que equivale a `rw- r-- r-- `.


### Propietario y grupo

Cuando se ejecuta `ls -l` se puede encontrar algo como `-rw-r--r--  1 rodrigo staff  820 README.md`. Aquí, `rodrigo` es el **propietario** y `staff` es el **grupo**.

### `chown`

El comando `chown` permite cambiar el propietario de un archivo. Por ejemplo, `sudo chown usuario archivo.txt` es un comando utilizado principalmente en administración de sistemas y servidores. En los proyectos personales normalmente no se necesitará modificar el propietario.

## Errores relacionados con permisos

- `Permission denied`: Si aparece este mensaje, significa que no hay permisos suficientes para realizar esa acción.

- `No such file or directory`: Si aparece este mensaje normalmente significa que el archivo/carpeta no existe, o bien que se ha escrito mal el nombre o se está en una ubicación diferente.
- 

## ⚠️ Buenas prácticas

- Utiliza rutas relativas dentro de tus proyectos cuando sea conveniente.
- Comprueba tu ubicación con `pwd` si tienes dudas.
- Evita modificar permisos sin entender qué efecto tendrán.
- No utilices `sudo` automáticamente cuando aparezca `Permission denied`.
- Primero intenta comprender por qué no tienes permisos.
- Ten especial cuidado con cambios de permisos en archivos del sistema.

## Resumen de comandos

| Comando | Función |
|---|---|
| `pwd` | Mostrar la ruta actual |
| `cd` | Cambiar de directorio |
| `ls -l` | Mostrar permisos e información detallada |
| `chmod +x archivo` | Añadir permiso de ejecución |
| `chmod -x archivo` | Quitar permiso de ejecución |
| `chmod 755 archivo` | Establecer `rwxr-xr-x` |
| `chmod 644 archivo` | Establecer `rw-r--r--` |
| `chown` | Cambiar el propietario |

---


# Lección 4.4 — Comandos útiles para el día a día

## Objetivos

Al terminar esta lección sabrás:

- Visualizar el contenido de archivos.
- Leer archivos largos de forma cómoda.
- Mostrar las primeras o últimas líneas de un archivo.
- Buscar archivos y texto.
- Consultar el historial de comandos.
- Consultar la documentación de un comando.
- Combinar comandos mediante `|`.

Así, podrás utilizar la terminal no solo para **moverte y gestionar archivos**, sino también para **investigar y analizar el contenido de tus proyectos**.

El flujo conceptual es:

```text
NAVEGAR
   ↓
pwd / cd / ls
   ↓
LOCALIZAR
   ↓
find
   ↓
LEER
   ↓
cat / less / head / tail
   ↓
BUSCAR INFORMACIÓN
   ↓
grep
   ↓
COMBINAR
   ↓
|
```

Todas estas herramientas serán especialmente útiles cuando trabajes con proyectos Python, Git, logs, servidores y grandes cantidades de archivos.

## Mostrar el contenido de un archivo

El comando más sencillo es `cat`, que significa **concatenate**, aunque normalmente se utiliza para mostrar el contenido de archivos. Supongamos que hacemos `cat README.md`. El resultado será:

```text
# DataPortfolio

Repositorio con proyectos de análisis de datos.
```

¿Cuándo utilizar `cat`? Es especialmente útil para archivos pequeños como `README.md`, `.gitignore`, `requirements.txt` o archivos de configuración. Pero si el archivo es muy largo es preferible utilizar `less`. Este comando permite consultar archivos grandes sin mostrar todo el contenido de golpe ya que permite desplazarte con flechas por el documento, avanzar y retroceder, buscar texto, y salir pulsando `q`

## Mostrar las primeras líneas: `head`

Si solo quieres consultar el principio de un archivo, el comando `head` es el más adecuado. Por defecto muestra las primeras 10 líneas, aunque se pueden indicar cuántas líneas se quieren ver haciendo `head -20 archivo.txt`. Esto muestra las primeras 20 líneas.


## Mostrar las últimas líneas: `tail`

Si solo quieres consultar el final de un archivo, el comando `tail` es el más adecuado. Por defecto muestra las últimas 10 líneas. Esto es especialmente útil para consultar archivos de registro (*logs*).

## Seguir un archivo en tiempo real

Una variante muy útil de `tail` es `tail -f`. La opción `-f` significa *follow*, es decir, mientras el archivo se va modificando, la terminal muestra las nuevas líneas automáticamente. Se usa mucho para supervisar aplicaciones, servidores, archivos de registro, procesos que están ejecutándose. Para detenerlo hay que pulsar `Ctrl + C`


## Buscar archivos con `find`

El comando `find` permite buscar archivos y carpetas. La estructura completa del comando es `find . -name "*.py"`. Significa:

- `.` → empieza a buscar desde la carpeta actual.
- `-name` → busca por nombre.
- `"*.py"` → archivos cuyo nombre termine en `.py`.

Podría devolver:

```text
./src/app.py
./src/utils.py
./tests/test_app.py
```

### Qué significa `*`

El símbolo `*` es un **comodín** (*wildcard*). Por ejemplo, `*.py` significa "Cualquier nombre que termine en `.py`". Otros ejemplos: `*.csv` significa "Todos los archivos CSV"; `*.md` significa "Todos los archivos Markdown"; y `test*` significa "Todo aquello cuyo nombre empiece por `test`".


## Buscar texto con `grep`

El comando `grep` permite buscar texto dentro de archivos. Por ejemplo, `grep "pandas" requirements.txt` da como resultado `pandas==2.3.0`

Para buscar texto en todo un proyecto se puede usar la opción `-r`: `grep -r "DataFrame"`. La búsqueda se realizará sobre el árbol del proyecto, es decir, también buscará dentro de las subcarpetas:

```text
Carpeta actual
│
├── archivo
├── carpeta
│   ├── archivo
│   └── carpeta
│       └── archivo
└── ...
```

En este contexto, la opción `-r` (recursiva) quiere decir "aplicar la misma operación en todos los niveles de una estructura". Por ejemplo,

```bash
grep -r "Git" .
```

significa "Busca `Git` aquí y también dentro de todas las subcarpetas."


## Consultar el historial

La terminal guarda los comandos que has ejecutado. Puedes consultarlos con `history`, y el resultado quedaría algo como

```text
301 git status
302 git add .
303 git commit -m "Actualizar README"
304 python app.py
```

Esto resulta muy útil para recuperar comandos anteriores.

### Buscar en el historial

Cuando tengas muchos comandos guardados puedes utilizar `Ctrl + R`. Aparecerá algo parecido a:

```text
(reverse-i-search)
```

Empieza a escribir una palabra, por ejemplo `git`. La terminal buscará comandos anteriores que contengan esa palabra.


## Consultar el manual

La mayoría de los comandos importantes tienen documentación incorporada. Puedes consultarla mediante `man comando`. Por ejemplo, para abrir el manual de `ls`,

```bash
man ls
```

Para salir de él, presionamos `q`.


## Ayuda rápida

Algunos comandos también ofrecen ayuda rápida mediante la opción `comando --help`. Esto muestra las opciones disponibles para ese comando. Pero... **no todos los comandos de macOS utilizan `--help`. Cuando no funcione, puedes consultar `man`.**


## Combinar comandos con `|`

Una de las características más potentes de la terminal es el **pipe**, `|`. Este símbolo permite utilizar la salida de un comando como entrada de otro. Por ejemplo, `ls | grep ".py"` lista los archivos y después filtra la lista.


## Resumen de comandos

| Comando | Función |
|---|---|
| `cat` | Mostrar un archivo completo |
| `less` | Leer archivos largos |
| `head` | Mostrar las primeras líneas |
| `tail` | Mostrar las últimas líneas |
| `tail -f` | Seguir un archivo en tiempo real |
| `find` | Buscar archivos y carpetas |
| `grep` | Buscar texto |
| `grep -r` | Buscar texto recursivamente |
| `history` | Mostrar el historial |
| `man` | Abrir el manual de un comando |
| `comando --help` | Mostrar ayuda |
| `\|` | Conectar comandos |


## Buenas prácticas

- Utiliza `cat` para archivos pequeños.
- Utiliza `less` para archivos largos.
- Aprende a utilizar `grep`: te ahorrará mucho tiempo en proyectos grandes.
- Utiliza `find` para localizar archivos rápidamente.
- Utiliza `Ctrl + R` para recuperar comandos antiguos.
- Consulta `man` cuando no recuerdes cómo funciona un comando.
- Utiliza `Ctrl + C` para detener procesos que estén ejecutándose.

---

# Lección 4.5 — Atajos y productividad en la terminal

## Objetivos

Al terminar esta lección sabrás:

- Editar comandos sin tener que volver a escribirlos.
- Utilizar el historial de forma eficiente.
- Autocompletar rutas y nombres.
- Cancelar procesos.
- Limpiar y controlar la terminal.
- Trabajar de forma más rápida y eficiente desde la línea de comandos.


## Autocompletado con `TAB`

El autocompletado es una de las funciones más útiles de la terminal. Supongamos que existe una carpeta llamada:

```text
DataPortfolio
```

Puedes escribir:

```bash
cd Dat
```

y pulsar:

```text
TAB
```

La terminal completará automáticamente:

```bash
cd DataPortfolio
```

Esto evita tener que escribir nombres largos y reduce los errores.

Pero supongamos que tienes:

```text
Desktop
Documents
Downloads
```

Escribes:

```bash
cd D
```

y pulsas `TAB`.

Como existen varias opciones, la terminal puede no saber cuál quieres. Si vuelves a pulsar `TAB`, mostrará las coincidencias:

```text
Desktop
Documents
Downloads
```

Solo tendrás que escribir alguna letra más.


## Flechas `↑` y `↓`

La terminal guarda los comandos que has ejecutado. Con `↑` recuperas el comando anterior. Por ejemplo:

```bash
git status
```

Después:

```bash
git add .
```

Y después:

```bash
git commit -m "Actualizar README"
```

Puedes pulsar `↑` para recuperar cualquiera de ellos sin volver a escribirlo.

Con:

```text
↓
```

avanzas de nuevo por el historial.

- Cancelar un proceso: Si un programa está ejecutándose y quieres detenerlo, haz `Ctrl + C`. La ejecución se interrumpirá.

- Limpiar la pantalla: Puedes limpiar la pantalla con `clear` o con el atajo `Ctrl + L` o `Ctrl + K`. El resultado visual es el mismo: se limpia el contenido visible de la terminal.

- Mover el cursor: Puedes desplazarte por el comando actual utilizando `← →`. Esto permite corregir una parte del comando sin tener que escribirlo de nuevo.

- Ir al principio de la línea: Utiliza el atajo `Ctrl + A` y el cursor irá directamente al principio de la línea actual.

- Ir al final de la línea: Utiliza el atajo `Ctrl + E` y el cursor irá directamente al final de la línea.

- Borrar una palabra: Utiliza el atajo `Ctrl + W` para borrar la palabra anterior al cursor.

- Copiar y pegar: En macOS, presiona **⌘ + C** para copiar texto seleccionado, y **⌘ + V** para pegarlo.

- Arrastrar archivos a la terminal: Puedes arrastrar un archivo desde Finder hasta la terminal y la terminal escribirá automáticamente su nueva ruta. Esto es especialmente útil cuando la ruta es larga o complicada.

- El prompt: El ***prompt*** es la parte de la terminal que indica que está preparada para recibir un nuevo comando. Puede tener un aspecto parecido a `rodrigo@MacBook-Pro DataPortfolio %` dependiendo de la configuración de la terminal. Normalmente contiene información como el usuario, el nombre del ordenador y el directorio actual. Cuando aparece el prompt, significa que puedes escribir el siguiente comando.

- Trabajar con el historial: La terminal mantiene un historial de los comandos ejecutados. Puedes verlo con `history`, pero para el trabajo diario normalmente será más rápido utilizar `↑` o `Ctrl + R`


## Resumen de atajos

| Atajo | Acción |
|---|---|
| `TAB` | Autocompletar nombres y rutas |
| `↑` | Recuperar el comando anterior |
| `↓` | Avanzar por el historial |
| `Ctrl + R` | Buscar en el historial |
| `Ctrl + C` | Cancelar un proceso o una línea |
| `Ctrl + L` | Limpiar la pantalla |
| `Ctrl + A` | Ir al principio de la línea |
| `Ctrl + E` | Ir al final de la línea |
| `Ctrl + W` | Borrar la palabra anterior |
| `← →` | Mover el cursor |


## Buenas prácticas

- Utiliza `TAB` para completar nombres y rutas.
- Utiliza `↑` y `↓` para recuperar comandos recientes.
- Utiliza `Ctrl + R` cuando necesites buscar un comando antiguo.
- Utiliza `Ctrl + C` para detener procesos que estén ejecutándose.
- Utiliza `Ctrl + L` para mantener limpia la terminal.
- Evita reescribir comandos largos si puedes recuperarlos del historial.
- Comprueba siempre el comando antes de pulsar `Enter`, especialmente cuando incluya operaciones destructivas como `rm`.


---

