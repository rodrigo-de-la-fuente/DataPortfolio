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


## 2. Manejar archivos
Python nos proporciona una forma **segura y limpia** de trabajar con archivos, y eso es con la estructura `with open()`:

```python
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
```

Así podemos leer o escribir archivos y cerrarlos automáticamente al terminar, incluso si ocurre un error. Vamos por partes:

- `with` es el administrador de contexto (*context manager*): Gestiona recursos de entrada/salida.
- `open()` es la función nativa para abrir ficheros.
- `as f` asigna el archivo abierto a una variable local.


### Modos de apertura de un archivo

Los modos comunes de apertura de un archivo son:

* `'r'`: Lectura (por defecto). Falla si el archivo no existe.
* `'w'`: Escritura. Sobrescribe el archivo o lo crea si no existe.
* `'a'`: Añade (*append*). Agrega contenido al final del archivo.
* `'r+'`: Lectura y escritura simultáneas.

## 3. Lectura

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

Cuando trabajemos con archivos grandes, procesar línea por línea puede ser mucho más adecuado que cargar todo el contenido de una vez. Esto será muy útil posteriormente cuando trabajemos con **datasets y grandes cantidades de datos**.


### `readlines()`

También podemos obtener las líneas como una lista:

```python
with open("datos.txt", "r") as archivo:
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

## 4. `with` no es exclusivo de archivos

`with` pertenece a una idea más general de Python:

> **Gestionar recursos automáticamente.**

Un archivo es un recurso, pero existen otros. Por ahora no necesitamos aprender todos los casos. Nos quedamos con la idea de que `with` permite que Python gestione correctamente determinados recursos y realice la limpieza necesaria al terminar el bloque. Más adelante encontraremos estructuras con `with` en diferentes contextos.


## 5. Una mejora importante: `encoding`

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


## 6. Algunas funciones útiles

Supongamos que tenemos `productos.txt` con:

```text
Pan,1.20
Leche,0.95
Huevos,2.50
```

Podemos leerlo:

```python
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

Aquí, `strip()` elimina los espacios y saltos de línea sobrantes y obtendríamos:

```text
Pan,1.20
Leche,0.95
Huevos,2.50
```

Pero todavía podemos hacer algo más:

```python
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio = linea.strip().split(",")
        print(f"{nombre}: {precio} €")
```

Y como resultado tendremos:

```text
Pan: 1.20 €
Leche: 0.95 €
Huevos: 2.50 €
```

Aquí ya estamos conectando varios conceptos que hemos aprendido:

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

---

# Lección 2.5.4 — Manejo de excepciones

Hasta ahora nuestros programas han funcionado suponiendo que todo sale bien. Pero un programa real tiene que enfrentarse a situaciones como:

* El usuario introduce texto cuando esperábamos un número.
* Intentamos abrir un archivo que no existe.
* Una carpeta ya existe.
* Intentamos dividir entre cero.
* Un índice no existe en una lista.
* Una clave no existe en un diccionario.

Python no puede simplemente continuar como si nada. Cuando ocurre una situación problemática durante la ejecución, Python genera una **excepción**.


## 1. ¿Qué es una excepción?

Observa:

```python
numero = int("hola")
```

Python no puede convertir `"hola"` en un entero. Por tanto, genera una excepción: `ValueError`. Y veremos algo parecido a:

```text
ValueError: invalid literal for int() with base 10: 'hola'
```

El programa se detiene. Conceptualmente:

```text
Programa
   │
   ▼
ejecución normal
   │
   ▼
¿ocurre un problema?
   │
   ├── NO ──→ continúa
   │
   └── SÍ ──→ excepción
                  │
                  ▼
             programa detenido
```


## 2. Excepción ≠ error de sintaxis

Es importante distinguir dos cosas:

### Error de sintaxis

```python
if numero > 10
    print(numero)
```

Falta `:`. Python ni siquiera puede interpretar correctamente el programa.

### Excepción durante la ejecución

```python
numero = int("hola")
```

El código es sintácticamente correcto, pero **algo sucede durante la ejecución que Python no puede realizar**.

```text
Sintaxis incorrecta
       ↓
Python no puede ejecutar correctamente el código

Excepción
       ↓
Python empieza a ejecutar
       ↓
encuentra una situación problemática
```


## 3. Algunos tipos de excepciones importantes

No necesitas memorizar todas las excepciones de Python pero sí reconocer algunas habituales:

* **`ValueError`**: El tipo de dato tiene una forma que no puede utilizarse para la operación.
  ```python
  int("hola")  # → ValueError
  ```
* **`TypeError`**: Intentamos realizar una operación incompatible con el tipo de dato.
  ```python
  "10" + 5  # → TypeError (no podemos sumar directamente un str y un int)
  ```
* **`ZeroDivisionError`**:
  ```python
  resultado = 10 / 0  # → ZeroDivisionError
  ```
* **`IndexError`**:
  ```python
  numeros = [10, 20, 30]
  print(numeros[5])  # No existe la posición 5 → IndexError
  ```
* **`KeyError`**:
  ```python
  persona = {"nombre": "Ana"}
  print(persona["edad"])  # No existe la clave "edad" → KeyError
  ```
* **`FileNotFoundError`**:
  ```python
  with open("archivo_inexistente.txt", "r") as archivo:
      contenido = archivo.read()  # Si el archivo no existe → FileNotFoundError
  ```
  *Este nos interesa especialmente por la lección que estamos estudiando.*


## 4. Qué hacer cuando aparece una excepción

Aquí aparece una idea fundamental: **`try`** y **`except`**. La estructura básica es:

```python
try:
    # código que puede producir una excepción
except:
    # qué hacer si ocurre
```

Por ejemplo:

```python
try:
    numero = int("hola")
except:
    print("No se pudo convertir el valor")
```

En lugar de terminar abruptamente con el traceback, podemos controlar la situación.

### Especificar qué excepción esperamos

Aunque usar un `except` genérico funciona:

```python
try:
    numero = int("hola")
except:
    print("Ha ocurrido un error")
```

No es la mejor práctica. Es preferible indicar qué excepción queremos manejar:

```python
try:
    numero = int("hola")
except ValueError:
    print("El valor no es un número válido")
```

Esto es mucho más preciso.

Conceptualmente:

```text
try
 │
 └── intenta ejecutar
          │
          ▼
      ¿ValueError?
          │
       ┌──┴──┐
      NO     SÍ
       │      │
       ▼      ▼
   continúa  except
```

### Por qué no utilizar siempre `except` genérico

Porque podemos ocultar errores que realmente queremos conocer. Por ejemplo:

```python
try:
    resultado = 10 / 0
except:
    print("Algo ha ocurrido")
```

Funciona, pero hemos perdido información importante. Es mejor:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre cero")
```

Ahora sabemos exactamente qué problema estamos tratando.


## 5. Obtener información de la excepción

Podemos guardar la excepción en una variable:

```python
try:
    numero = int("hola")
except ValueError as error:
    print(error)
```

Podemos obtener algo como:

```text
invalid literal for int() with base 10: 'hola'
```

La variable `error` contiene información sobre la excepción. También podemos utilizar nombres cortos como `except ValueError as e:`, pero `error` suele resultar más descriptivo para alguien que está aprendiendo.


## 6. Varias excepciones

Una misma operación puede producir distintos tipos de excepción. Por ejemplo:

```python
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(resultado)
except ValueError:
    print("Debes introducir un número válido")
except ZeroDivisionError:
    print("No puedes introducir cero")
```

Aquí tenemos dos posibles problemas:

```text
input()
  │
  ▼
int()
  │
  ├── texto inválido → ValueError
  │
  ▼
división
  │
  └── 0 → ZeroDivisionError
```

Cada uno recibe un tratamiento diferente.


## 7. `try` debe contener lo necesario

No debemos meter todo el programa dentro de un único `try`. Por ejemplo, esto puede ocultar demasiado:

```python
# Malas prácticas: try demasiado grande
try:
    numero = int(input("Número: "))
    print(numero)
    ...
    ...
    ...
```

Es mejor que el `try` abarque **únicamente** la operación que puede producir la excepción:

```python
entrada = input("Introduce un número: ")

try:
    numero = int(entrada)
except ValueError:
    print("Entrada no válida")
```

Esto deja mucho más claro qué estamos controlando.


## 8. Excepciones y archivos

Ahora podemos conectar esta lección con la anterior:

```python
from pathlib import Path

ruta = Path("data/productos.txt")

try:
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")
```

Ahora nuestro programa no se rompe simplemente porque el archivo no esté.


## 9. Ejemplo completo

Imaginemos:

```python
from pathlib import Path

def main():
    ruta = Path("data/productos.txt")

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
        print(contenido)

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")

if __name__ == "__main__":
    main()
```

La estructura conceptual es:

```text
                 programa
                    │
                    ▼
              intentar leer
                    │
             ┌──────┴──────┐
             │             │
           éxito          error
             │             │
             ▼             ▼
         mostrar       FileNotFoundError
         contenido           │
                             ▼
                      mensaje controlado
```


Esta distinción es muy importante: 
> **Capturar la excepción no significa ignorarla**

No queremos hacer:

```python
except:
    pass
```

Esto significa prácticamente: *"Si ocurre algo, no hagas nada"*. Puede hacer que un programa parezca funcionar cuando en realidad está fallando. En cambio, preferimos:

```python
except FileNotFoundError:
    print("El archivo no existe.")
```

O, en un programa más elaborado, registrar el error, solicitar otra entrada, utilizar un valor alternativo, etc.


## 10. Crear nuestros propios mensajes

Las excepciones permiten que el programa sea más comprensible para el usuario.

**Sin manejo:**
```text
Traceback (most recent call last):
...
FileNotFoundError: ...
```

**Con manejo:**
```text
No se encontró el archivo productos.txt.
```

Esto es especialmente importante en aplicaciones que otras personas van a utilizar.


## 11. Excepciones como parte del flujo del programa

Una excepción no tiene por qué significar *"El programa está completamente roto"*. Puede significar: **"Ha ocurrido una situación que el programa debe saber gestionar."**

```text
Usuario
  │
  ▼
introduce dato
  │
  ▼
¿dato válido?
  │
 ┌┴──────────────┐
 │               │
Sí              No
 │               │
 ▼               ▼
continuar    manejar excepción
```

Esto convierte nuestros programas en sistemas más robustos.


## 12. Excepciones frente a `if`

A veces podemos comprobar una situación antes de realizar una operación.

### Con `if`
```python
from pathlib import Path

ruta = Path("datos.txt")

if ruta.exists():
    with open(ruta, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
else:
    print("El archivo no existe.")
```

### Con `try` / `except`
```python
try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
```

¿Cuál debemos utilizar? Depende de la situación.
* **Comprobación explícita (`if`):** Apropiada cuando queremos tomar una decisión basándonos en una condición conocida.
* **Excepción (`try`/`except`):** Apropiada cuando una operación puede fallar y queremos gestionar ese fallo directamente al ejecutarla.

