# Lección 2.5.1 — Leer y escribir archivos

Hasta ahora hemos trabajado principalmente con variables, estructuras de datos, funciones y clases. Ahora vamos a aprender a hacer que nuestros programas lean información de archivos y guarden información en ellos. Esta subfase introduce una capacidad fundamental para pasar de trabajar con datos escritos directamente en el código a trabajar con datos almacenados externamente.


## 1. ¿Por qué necesitamos archivos?

Imagina este programa:

```python
productos = [
    ("Pan", 1.20),
    ("Leche", 0.95),
    ("Huevos", 2.50)
]
```

Los datos están dentro del programa. Esto funciona, pero tiene un problema: si cerramos el programa, los datos siguen existiendo **solo porque están escritos en el código**. En un programa real queremos poder tener algo como:

```text
DataPortfolio/
│
├── data/
│   └── productos.txt
│
└── src/
    └── main.py
```

Y que `main.py` pueda leer:

```text
Pan,1.20
Leche,0.95
Huevos,2.50
```

De esta manera:

```text
ARCHIVO
   │
   │ leer
   ▼
PROGRAMA
   │
   │ procesar
   ▼
RESULTADO
```

Y también al revés:

```text
PROGRAMA
   │
   │ guardar
   ▼
ARCHIVO
```

Esto es el comienzo de algo muy importante en Data / AI:

> **Entrada de datos → Procesamiento → Salida de datos**


## 2. Abrir un archivo

Python utiliza la función:

```python
open()
```

Por ejemplo:

```python
archivo = open("datos.txt", "r")
```

Aquí estamos diciendo:
* `"datos.txt"` → Archivo que queremos abrir.
* `"r"` → Modo de lectura (*read*).

Después podemos leer su contenido.

## 3. Leer un archivo

### Leer todo el contenido

Podemos utilizar:

```python
contenido = archivo.read()
```

#### Ejemplo:

```python
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
```

Si `datos.txt` contiene:

```text
Hola
Este es mi archivo
Python puede leerlo
```

Obtendremos:

```text
Hola
Este es mi archivo
Python puede leerlo
```


### Leer línea por línea

Otra posibilidad es:

```python
archivo = open("datos.txt", "r")
for linea in archivo:
    print(linea)
```

Esto es especialmente interesante cuando tenemos archivos grandes.

Por ejemplo:

```text
Ana
Pedro
María
Juan
```

Python puede procesar:

```text
Ana
 ↓
Pedro
 ↓
María
 ↓
Juan
```

Sin necesidad conceptual de convertir todo el archivo en una única cadena.

Esto será muy útil posteriormente cuando trabajemos con **datasets y grandes cantidades de datos**.


### `readlines()`

También podemos obtener las líneas como una lista:

```python
archivo = open("datos.txt", "r")
lineas = archivo.readlines()
print(lineas)
```

**Resultado:**

```python
[
    "Ana
",
    "Pedro
",
    "María
",
    "Juan
"
]
```

Observa el `
`. Representa un **salto de línea**.


### Leer una cantidad determinada de caracteres

`read()` también puede recibir un número:

```python
contenido = archivo.read(10)
```

Esto significa: *Lee los primeros 10 caracteres.*

Por ejemplo, si el archivo contiene:

```text
Python es fantástico
```

Ejecutar:

```python
contenido = archivo.read(6)
```

Produciría:

```text
Python
```


## 4. Escribir en un archivo

Para escribir utilizamos el modo `"w"` (*write*).

### Ejemplo:

```python
archivo = open("resultado.txt", "w")
archivo.write("Hola mundo")
archivo.close()
```

Se creará el archivo `resultado.txt` con:

```text
Hola mundo
```


### Cuidado con `"w"`

Hay algo **muy importante** que debes recordar.

Si hacemos:

```python
open("resultado.txt", "w")
```

Y el archivo ya existe, **su contenido será sobrescrito**.

Por ejemplo, si tenemos `resultado.txt` con:

```text
Hola
Adiós
```

Y ejecutamos:

```python
archivo = open("resultado.txt", "w")
archivo.write("Nuevo contenido")
archivo.close()
```

Ahora tendremos:

```text
Nuevo contenido
```

El contenido anterior desaparece.


## 5. Añadir contenido: `"a"`

Para añadir información al final del archivo utilizamos `"a"` (*append*).

### Ejemplo:

```python
archivo = open("resultado.txt", "a")
archivo.write("
Nueva línea")
archivo.close()
```

Si teníamos:

```text
Hola
Adiós
```

Ahora tendremos:

```text
Hola
Adiós
Nueva línea
```


## 6. Cerrar el archivo

Cuando utilizamos `open()` estamos abriendo un recurso. Por eso debemos cerrarlo:

```python
archivo.close()
```

### Ejemplo completo:

```python
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()
```

La secuencia conceptual es:

```text
open()
   ↓
trabajar con el archivo
   ↓
close()
```

En la siguiente lección veremos una forma mucho más segura y profesional de hacer esto.

## 7. Un pequeño ejemplo orientado a Data

Supongamos que tenemos `productos.txt` con:

```text
Pan,1.20
Leche,0.95
Huevos,2.50
```

Podemos leerlo:

```python
archivo = open("productos.txt", "r")
for linea in archivo:
    print(linea.strip())
archivo.close()
```

> `strip()` elimina los espacios y saltos de línea sobrantes.

Obtendríamos:

```text
Pan,1.20
Leche,0.95
Huevos,2.50
```

Pero todavía podemos hacer algo más interesante:

```python
archivo = open("productos.txt", "r")
for linea in archivo:
    nombre, precio = linea.strip().split(",")
    print(f"{nombre}: {precio} €")
archivo.close()
```

**Resultado:**

```text
Pan: 1.20 €
Leche: 0.95 €
Huevos: 2.50 €
```

Aquí ya estamos conectando varios conceptos que has aprendido:

```text
ARCHIVO
   │
   ▼
leer líneas
   │
   ▼
strings
   │
   ▼
split()
   │
   ▼
variables
   │
   ▼
procesamiento
   │
   ▼
resultado
```

---

# Lección 2.5.2 — `with open()`: trabajar con archivos de forma segura

En la lección anterior aprendimos a hacer esto:

```python
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()
```

Funciona, pero Python nos proporciona una forma **más segura y limpia** de trabajar con archivos:

```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
```

La idea fundamental de esta lección es:

> **`with open()` se encarga de cerrar el archivo automáticamente cuando terminamos de trabajar con él.**


## 1. El problema de `open()` + `close()`

Con el método anterior nosotros somos responsables de recordar:

```python
archivo.close()
```

Por ejemplo:

```python
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()
```

Pero imagina que entre `read()` y `close()` ocurre un error:

```python
archivo = open("datos.txt", "r")
contenido = archivo.read()
resultado = 10 / 0
archivo.close()
```

El programa encuentra el error antes de llegar a:

```python
archivo.close()
```

Por tanto, el archivo podría quedar abierto.

Aquí aparece `with`.


## 2. La estructura `with open()`

La sintaxis es:

```python
with open("archivo.txt", "r") as archivo:
    # trabajar con archivo
```

Por ejemplo:

```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)
```

Observa que el bloque que pertenece al `with` se identifica mediante **indentación**, al igual que ocurría con las estructuras de control `if`, `for`, `while`, y con `def` en las funciones.

Conceptualmente:

```text
with open()
      │
      ▼
abre el archivo
      │
      ▼
ejecuta el bloque
      │
      ▼
termina el bloque
      │
      ▼
cierra automáticamente el archivo
```

Incluso si dentro del bloque ocurre un error, Python puede encargarse de realizar la limpieza correspondiente. Por eso `with` es preferible a gestionar manualmente `close()`.


## 3. Leer un archivo

La forma habitual será:

```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)
```

Y no necesitamos:

```python
archivo.close()
```


### Leer línea por línea

También podemos hacer:

```python
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

Por ejemplo, si tenemos:

```text
Pan
Leche
Huevos
```

Obtendremos:

```text
Pan
Leche
Huevos
```

## 4. Escribir un archivo

También funciona con `"w"`:

```python
with open("resultado.txt", "w") as archivo:
    archivo.write("Hola mundo")
```

Al terminar el bloque:

```text
with
 ↓
escribir
 ↓
fin del bloque
 ↓
archivo cerrado automáticamente
```


## 5. Añadir información

Podemos utilizar `"a"`:

```python
with open("resultado.txt", "a") as archivo:
    archivo.write("
Nueva línea")
```


## 6. Nuestro ejemplo de productos

En la lección anterior podríamos haber hecho:

```python
archivo = open("productos.txt", "w")
archivo.write("Pan,1.20
")
archivo.write("Leche,0.95
")
archivo.write("Huevos,2.50
")
archivo.close()
```

Ahora podemos escribirlo de forma más segura:

```python
with open("productos.txt", "w") as archivo:
    archivo.write("Pan,1.20
")
    archivo.write("Leche,0.95
")
    archivo.write("Huevos,2.50
")
```

Y posteriormente:

```python
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```


## 7. `with` no es exclusivo de archivos

`with` pertenece a una idea más general de Python:

> **Gestionar recursos automáticamente.**

Un archivo es un recurso, pero existen otros. Por ahora no necesitamos aprender todos los casos. Nos quedamos con la idea de que `with` permite que Python gestione correctamente determinados recursos y realice la limpieza necesaria al terminar el bloque. Más adelante encontraremos estructuras con `with` en diferentes contextos.


## 8. Una mejora importante: `encoding`

Cuando trabajamos con archivos de texto, es buena práctica especificar la codificación:

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

Y al escribir:

```python
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Información")
```

`UTF-8` permite trabajar correctamente con caracteres como:

```text
á é í ó ú
ñ
€
```

Esto es especialmente importante trabajando con datos reales.


## 9. `read()` frente a iterar por líneas

Tenemos dos estrategias principales a la hora de leer un archivo...

### Leer todo el archivo

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

Obtenemos un único `str`.

```text
archivo
   ↓
"todo el contenido"
```

### Leer línea por línea

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        ...
```

Conceptualmente:

```text
archivo
   ↓
línea 1
línea 2
línea 3
línea 4
...
```

Cuando trabajemos con archivos grandes, procesar línea por línea puede ser mucho más adecuado que cargar todo el contenido de una vez.

---

# Lección 2.5.3 — Módulos `os` y `pathlib`

Hasta ahora hemos trabajado con archivos como si estuvieran directamente disponibles:

```python
with open("datos.txt", "r", encoding="utf-8") as archivo:
    ...
```

Pero en un proyecto real aparecen preguntas como:

* ¿Dónde está ese archivo?
* ¿Existe la carpeta?
* ¿Qué archivos hay dentro?
* ¿Cómo creo una carpeta?
* ¿Cómo construyo correctamente una ruta?
* ¿Cómo obtengo el nombre o extensión de un archivo?

Para eso Python proporciona herramientas como `os` y, especialmente, `pathlib`.

## 1. ¿Qué es una ruta?

Una ruta (*path*) indica dónde se encuentra algo en nuestro ordenador. Por ejemplo:

```text
DataPortfolio/
└── data/
    └── productos.txt
```

La ruta relativa de `productos.txt` sería:

```text
data/productos.txt
```

En Python podemos utilizarla:

```python
with open("data/productos.txt", "r", encoding="utf-8") as archivo:
    ...
```

Como ya vimos en la fase 1.4, una ruta puede estar dada de dos maneras:

* **Relativa:** `data/productos.txt` (depende de dónde se esté ejecutando el programa).
* **Absoluta:** Por ejemplo, en macOS: `/Users/rodrigo/DataPortfolio/data/productos.txt` (indica una ubicación completa desde la raíz del sistema).


## 2. El módulo `os`

`os` es un módulo de Python que permite interactuar con el sistema operativo. Lo importamos:

```python
import os
```

Por ejemplo:

```python
print(os.getcwd())
```

`getcwd()` significa: **Get Current Working Directory**. Nos dice cuál es el directorio de trabajo actual.

Podríamos obtener algo parecido a:

```text
/Users/rodrigo/DataPortfolio
```

Esto es muy útil para entender **desde dónde está buscando Python nuestros archivos**.


### Comprobar si la ruta existe

Para comprobar si una ruta existe antes de intentar utilizarla, usamos:

```python
os.path.exists()
```

Por ejemplo:

```python
import os

print(os.path.exists("datos.txt"))
```

Dará como resultado un `bool`.


### ¿Es un archivo o una carpeta?

Podemos distinguir si una ruta corresponde a un archivo o una carpeta haciendo `os.path.isfile("datos.txt")` y `os.path.isdir("data")`.

Por ejemplo:

```python
import os

print(os.path.isfile("datos.txt"))
print(os.path.isdir("data"))
```


### Crear carpetas

Podemos crear una carpeta haciendo:

```python
os.mkdir("data")
```

Esto crea:

```text
proyecto/
└── data/
```

Pero `mkdir()` tiene una limitación: si necesitamos crear varios niveles que todavía no existen, puede resultar incómodo. Aquí es donde `pathlib` empieza a resultar especialmente interesante.

## 3. `pathlib`: trabajar con rutas de forma moderna

Podemos representar una ruta mediante un objeto `Path`:

```python
from pathlib import Path

ruta = Path("data/productos.txt")
```

Ahora `ruta` no es simplemente un `str`. Es un objeto que representa una ruta:

```text
Path
 │
 └── data/productos.txt
```

Esto nos permite utilizar métodos muy útiles.


### Comprobar si la ruta existe

Para hacer la comprobación usamos 

```python
from pathlib import Path

ruta = Path("data/productos.txt")
print(ruta.exists())
```

También:

```python
print(ruta.is_file())
print(ruta.is_dir())
```

Por tanto:

```text
Path
 │
 ├── exists()
 ├── is_file()
 └── is_dir()
```

---

### Crear carpetas

Podemos hacer:

```python
from pathlib import Path

carpeta = Path("data")
carpeta.mkdir()
```

Y se crea `data/`.

También podemos crear carpetas intermedias:

```python
carpeta = Path("data/processed/results")
carpeta.mkdir(parents=True)
```

Esto puede crear:

```text
data/
└── processed/
    └── results/
```

`parents=True` permite crear las carpetas padre que sean necesarias.

### Construir rutas

Aquí encontramos una de las grandes ventajas de `pathlib`. Podemos hacer:

```python
from pathlib import Path

carpeta = Path("data")
archivo = carpeta / "productos.txt"
```

Ahora `archivo` representa `data/productos.txt`. Esto es mucho mejor que construir manualmente `"data/" + "productos.txt"`. ¿Por qué? Porque `pathlib` se ocupa de construir correctamente las rutas según el sistema operativo.

## 4. `Path` + `open()`

Podemos utilizar directamente un `Path` con `open()`:

```python
from pathlib import Path

ruta = Path("data/productos.txt")

with open(ruta, "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
```

Esto conecta perfectamente lo aprendido en las dos lecciones anteriores. Incluso podemos usar los métodos de `Path`. Para leer:

```python
from pathlib import Path

ruta = Path("datos.txt")
contenido = ruta.read_text(encoding="utf-8")
```

Y para escribir:

```python
ruta.write_text("Hola mundo", encoding="utf-8")
```

Así:

```text
Path
 │
 ├── read_text()
 │
 └── write_text()
```

Aunque seguiremos utilizando `with open()` para aprender y controlar explícitamente el proceso de lectura/escritura.


### Obtener información de una ruta

Supongamos:

```python
from pathlib import Path

ruta = Path("data/productos.csv")
```

Podemos obtener:

* **Nombre (`ruta.name`):** `productos.csv`
* **Sufijo/extensión (`ruta.suffix`):** `.csv`
* **Nombre sin extensión (`ruta.stem`):** `productos`
* **Carpeta padre (`ruta.parent`):** `data`

Visualmente:

```text
data / productos.csv
 ↑          ↑
parent      name

productos  ← stem
.csv       ← suffix
```

### Buscar archivos dentro de una carpeta

Una operación muy útil:

```python
from pathlib import Path

carpeta = Path("data")

for archivo in carpeta.iterdir():
    print(archivo)
```

Si tenemos:

```text
data/
├── productos.csv
├── clientes.csv
├── ventas.csv
└── README.md
```

Podremos obtener:

```text
data/productos.csv
data/clientes.csv
data/ventas.csv
data/README.md
```


### Buscar determinados archivos

Podemos utilizar `glob()`. Por ejemplo:

```python
from pathlib import Path

carpeta = Path("data")

for archivo in carpeta.glob("*.csv"):
    print(archivo)
```

Esto significa: *Busca todos los archivos que terminen en `.csv`.*

Resultado:

```text
data/productos.csv
data/clientes.csv
data/ventas.csv
```

Pero no `README.md`. Esto será especialmente útil cuando empieces a trabajar con carpetas que contienen múltiples datasets.


## 5. `os` frente a `pathlib`

No hay que memorizar una enorme cantidad de funciones. La idea general es:

| Necesidad | `os` | `pathlib` |
| :--- | :--- | :--- |
| **Directorio actual** | `os.getcwd()` | `Path.cwd()` |
| **Existe** | `os.path.exists()` | `.exists()` |
| **Es archivo** | `os.path.isfile()` | `.is_file()` |
| **Es carpeta** | `os.path.isdir()` | `.is_dir()` |
| **Crear carpeta** | `os.mkdir()` | `.mkdir()` |
| **Construir rutas** | `os.path.join()` | `/` |
| **Buscar archivos** | `os.listdir()` | `.iterdir()` / `.glob()` |

Para código Python moderno, hay que tener una preferencia clara:

> **Cuando trabajemos específicamente con rutas, `pathlib` será nuestra herramienta principal.**

No significa que `os` sea inútil. Al contrario: sigue siendo un módulo importante y lo encontraremos constantemente en código Python.


## 6. Rutas relativas

Supongamos:

```text
DataPortfolio/
├── data/
│   └── productos.csv
│
└── src/
    └── main.py
```

Si `main.py` está dentro de `src`, la ruta `Path("data/productos.csv")` no necesariamente apunta a `DataPortfolio/data/productos.csv`. Depende del **directorio de trabajo desde el que ejecutamos el programa**. Por eso es importante entender que existen dos conceptos diferentes:

> **¿Dónde está mi archivo Python? ≠ ¿Desde dónde estoy ejecutando Python?**

Esto suele generar bastantes errores cuando se empieza a trabajar con proyectos.

