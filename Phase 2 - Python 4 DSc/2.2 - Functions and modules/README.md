# Lección 2.2.1 - Funciones y parámetros
Hasta ahora hemos aprendido a escribir instrucciones, manejar datos, crear variables, realizar operaciones y controlar el flujo del programa. Ahora vamos a aprender a agrupar código en unidades reutilizables.

## 1. Funciones

### El problema
Imagina que hacemos esto:

```python
print("==========")
print("Data Analyzer")
print("==========")

print("==========")
print("Data Analyzer")
print("==========")

print("==========")
print("Data Analyzer")
print("==========")
```

Funciona, pero estamos repitiendo código. Si mañana queremos cambiar `Data Analyzer` por `Movie Data Analyzer` tenemos que modificarlo varias veces. Una solución mucho mejor es crear una función.

### La solución
Una función es un bloque de código que:
* realiza una tarea concreta;
* puede recibir información;
* puede devolver un resultado;
* puede reutilizarse tantas veces como queramos.

Su estructura básica va precedida de la palabra clave `def`:

```python
def nombre_de_la_funcion():
    instrucciones
```

Como vemos, el cuerpo de la función habrá de ir indentado, como se hace con todas las estructuras de control de Python.

Ahora, podríamos construir una función que imprimiera múltiples veces `Data Analyzer` sin tener que repetir mucho código, solo llamando múltiples veces a esa función:

```python
def show_title():
    print("==========")
    print("Data Analyzer")
    print("==========")
```

Cuando la llamemos escribiendo `show_title()`, como resultado lanzará el mensaje:

```python
==========
Data Analyzer
==========
```

Así que hemos escrito la lógica una sola vez y sin embargo podemos reproducir las veces que queramos el resultado.

## 2. Parámetros
Los parámetros de una función son variables que podemos pasarle a la función al invocarla, para que las use. Los parámetros permiten que las funciones sean más flexibles y reutilizables.

La sintaxis básica para definir una función con parámetros en Python es la siguiente:

```python
def nombre_de_la_funcion(parametro1, parametro2, ...):
    # bloque de código de la función que utiliza los parámetros
```

Veamos un ejemplo:

```python
def saludar(nombre):
    print("Hola", nombre)

saludar("Luis")  # Salida: Hola Luis
```

Aquí definimos una función llamada `saludar` que toma un parámetro llamado `nombre`. Dentro de la función, se imprime un saludo “Hola” seguido del nombre que se pasa como argumento. Ahora, si llamo a la función con el parámetro `Luis`, esto provoca que la función se ejecute y muestre el mensaje `Hola Luis` como salida.

### Parámetros posicionales
Los parámetros posicionales son los parámetros más comunes. Se definen en el orden en que aparecen en la lista de parámetros de la función y se pasan a la función en el mismo orden.

```python
def suma(a, b):
    resultado = a + b
    return resultado

# Llamada a la función con parámetros posicionales
resultado_suma = suma(5, 3)
print(resultado_suma)  # Salida: 8
```

### Parámetros con valores predeterminados
Los parámetros con valores predeterminados son parámetros que tienen un valor asignado por defecto en la definición de la función.

```python
def saludar(nombre="Mundo"):
    print("Hola,", nombre)

# Llamada a la función sin proporcionar un valor para el parámetro
saludar()  # Salida: Hola, Mundo

# Llamada a la función con un valor para el parámetro
saludar("Luis")  # Salida: Hola, Luis
```

Si no se proporciona un valor para estos parámetros al llamar a la función, se utilizará el valor predeterminado.


### Parámetros con nombre
Los parámetros con nombre son parámetros que se pasan a la función utilizando su nombre (en lugar de su posición). Esto permite cambiar el orden de los parámetros o incluso omitir algunos de ellos.

```python
def saludar(nombre, saludo="Hola"):
    print(saludo + ",", nombre)

# Llamada a la función con parámetros con nombre
saludar(nombre="Ana")  # Salida: Hola, Ana
saludar(saludo="Buenos días", nombre="Pedro")  # Salida: Buenos días, Pedro
```

## 3. return
Los valores de retorno de una función son un valor que la función puede devolver (opcionalmente) como resultado, después de realizar sus operaciones. Los valores de retorno permiten que las funciones puedan realizar cálculos y operaciones, y luego pasen el resultado de vuelta al código que las llamó.

En Python, la instrucción `return` se utiliza para devolver un valor desde una función, al punto desde donde se llamó la función. Cuando se encuentra la instrucción `return`, la ejecución de la función se detiene y el valor especificado después de `return` se devuelve como resultado de la función.

La sintaxis básica de `return` es la siguiente:

```python
def nombre_de_la_funcion(parametros):
    # bloque de código de la función
    return valor_a_devolver
```

En Python una función puede devolver varios valores, por ejemplo si hacemos

```python
def calcular_estadisticas(datos):
    minimo = min(datos)
    maximo = max(datos)
    media = sum(datos) / len(datos)

    return minimo, maximo, media
```

Python está devolviendo realmente una tupla `(minimo, maximo, media)`. Y podemos hacer desempaquetado:

```python
minimo, maximo, media = calcular_estadisticas(datos)
```

# Lección 2.2.2 - Parámetros de longitud variable

Python permite definir funciones que aceptan un número variable de parámetros utilizando `*args` y `**kwargs`.

## 1. *args
`*args` se utiliza para pasar una lista de argumentos posicionales. Por ejemplo:

```python
def suma_numeros(*args):
    resultado = sum(args)
    return resultado

# Llamada a la función con una cantidad variable de argumentos
resultado_suma = suma_numeros(1, 2, 3, 4, 5)
print(resultado_suma)  # Salida: 15
```

El operador `*` se utiliza cuando queremos desempaquetar los elementos de una lista y pasarlos como argumentos a una función.

```python
def sumar(a, b, c):
    return a + b + c

valores = [1, 2, 3]
print(sumar(*valores))  # Resultado: 6
```
Aquí `valores` es una lista que contiene [1, 2, 3]. Al llamar `sumar(*valores)`, los elementos de la lista se desempaquetan y se pasan como argumentos a la función sumar. Es decir, es equivalente a llamar `sumar(1, 2, 3)`.

## 2. **kwargs
`**kwargs` se utiliza para pasar un diccionario de argumentos de palabra clave (*keywords arguments*).

```python
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(clave + ":", valor)

# Llamada a la función con argumentos con nombre
imprimir_info(nombre="Luis", edad=30, ciudad="Madrid")
# Salida:
# nombre: Luis
# edad: 30
# ciudad: Madrid
```

El operador `**` se utiliza de manera similar a `*`, pero en este caso para desempaquetar los elementos de un diccionario y pasarlos como argumentos a una función. Aquí, las claves del diccionario se convierten en nombres de parámetros y los valores del diccionario se asignan a esos parámetros. Por ejemplo:

```python
diccionario = {"a": 1, "b": 2, "c": 3}
print(sumar(**diccionario))  # Resultado: 6
```

Aquí, `diccionario` es un diccionario que contiene `{"a": 1, "b": 2, "c": 3}`. Al llamar `sumar(**diccionario)`, los elementos del diccionario se desempaquetan y se pasan como argumentos a la función `sumar`. La clave "a" se asigna al parámetro `a`, la clave "b" se asigna a `b` y la clave "c" se asigna a `c`. Es decir, es equivalente a llamar `sumar(a=1, b=2, c=3)`


# Lección 2.2.3 - Alcance (*scope*) de variables

Python clasifica los alcances o *scopes* de acuerdo con el modelo LEGB (*Local-Enclosing-Global-Built in*), que determina el orden en que se buscan las variables:

- **Local**: Variables definidas dentro de una función o bloque, accesibles únicamente dentro de ese contexto. Se crean al inicio de la ejecución de la función y desaparecen cuando esta termina. Por ejemplo:

```python
def saludo():
    mensaje = "¡Hola, mundo!"  # Variable local
    print(mensaje)

saludo()
print(mensaje)  # Esto generará un error porque 'mensaje' es local a la función.
```

En este caso, la variable `mensaje` se define y utiliza dentro de la función saludo. Fuera de esta función, la variable no existe y no se puede acceder.

- ***Enclosing***: Se refiere a las variables definidas en una función exterior que encapsula otra función. Estas variables no son locales para la función más interna, pero tampoco son globales.

```python
def funcion_exterior():
    mensaje = "Hola desde la función exterior"  # Variable en el alcance 'enclosing'

    def funcion_interior():
        print(mensaje)  # La función interior accede a la variable de la exterior

    funcion_interior()

funcion_exterior()
```

La salida del script será `Hola desde la función exterior`. En este caso, `mensaje` no es ni local para `funcion_interior` ni global, sino que pertenece al alcance de `funcion_exterior`. Este es un ejemplo de una variable con alcance *enclosing*.

- **Global**: Variables definidas en el nivel superior del script o programa, fuera de cualquier función. Son accesibles en todo el archivo, pero pueden ser modificadas dentro de una función solo si se usa la palabra clave global.

```python
mensaje = "Hola desde el alcance global"  # Variable global

def imprimir_mensaje():
    print(mensaje)  # Accediendo a la variable global

imprimir_mensaje()

print(mensaje)  # También accesible fuera de las funciones
```

La salida del script será `Hola desde el alcance global` `Hola desde el alcance global`. En este caso, `mensaje` se define fuera de cualquier función, por lo que es global y puede ser utilizada tanto dentro como fuera de las funciones.

- ***Built-in***: Variables y funciones predefinidas de Python que están disponibles en cualquier parte del código, como `len()`, `range()` y `print()`.

```python
from math import sqrt  # 'sqrt' es una función built-in del módulo 'math'

numero = 16
raiz_cuadrada = sqrt(numero)  # Usamos la función built-in para calcular la raíz cuadrada
print(f"La raíz cuadrada de {numero} es {raiz_cuadrada}")
```

La salida será `La raíz cuadrada de 16 es 4.0`. En este caso, utilizamos una función *built-in* del módulo estándar `math`, que amplía las funcionalidades predefinidas de Python.

Una regla con la que hay que quedarse de cara a hacer funciones es:
> **Una función debe depender lo menos posible del estado global del programa**


## 1. Algunas indicaciones

### Cuidado con modificar variables globales
Aquí aparece una cuestión importante:

```python
contador = 0

def incrementar():
    contador = contador + 1
```

Esto no funciona como podríamos esperar. Python interpreta `contador = contador + 1` como una asignación de una variable local llamada `contador`, pero estamos intentando utilizarla antes de haberla creado localmente, así que obtendremos un error.

### `global`
Para solucionar el problema anterior, Python permite indicar explícitamente que queremos utilizar la variable global usando la palabra reservada `global`:

```python
contador = 0

def incrementar():
    global contador
    contador = contador + 1
```

Ahora:

```python
incrementar()
print(contador)
```

produce `1`. Podemos hacerlo varias veces:

```python
incrementar()
incrementar()

print(contador)
```

Obteniendo como resultado `3`. Pero en nuestro código profesional intentaremos evitar `global` siempre que sea posible porque hace que las funciones dependan de variables externas y modifica el estado del programa de forma menos controlada. Es mucho mejor normalmente:

```python
def incrementar(contador):
    return contador + 1
```

Ahora la función `recibe → procesa → devuelve` y no modifica algo escondido fuera de ella.

### Variables locales con el mismo nombre
Ahora supongamos que tenemos el siguiente script:

```python
nombre = "Rodrigo"

def cambiar_nombre():
    nombre = "Juan"
    print(nombre)

cambiar_nombre()

print(nombre)
```

El resultado será

```text
Juan
Rodrigo
```

¿Por qué? Porque existen dos variables diferentes llamadas `nombre`, y la variable local no sustituye a la global:

```text
GLOBAL
nombre = "Rodrigo"
       │
       │
       │    LOCAL
       └──► nombre = "Juan"
```

# Lección 2.2.4 - Módulos y paquetes

## 1. Módulos
Aquí empezaremos a sacar nuestras funciones de *main.py* y a repartir el código en archivos y módulos con responsabilidades claras, que es un paso importante para convertir nuestro proyecto en algo realmente profesional. Hasta ahora hemos trabajado con funciones dentro del mismo archivo, pero imagina que nuestro programa empieza a crecer, pasando de 20 líneas a 500 líneas... a 1000... a 2000... Esto rápidamente se vuelve difícil de mantener. La solución es dividir nuestro código en **módulos**. En Python, un módulo es, básicamente, un archivo .py que contiene código que podemos reutilizar. Por ejemplo:

```text
proyecto/
│
├── main.py
└── calculos.py
```

Y podemos poner nuestras funciones en *calculos.py*. Y después utilizarlas desde *main.py*. Así que cada módulo tiene una responsabilidad. Por ejemplo,

```text
data_loader.py
      │
      └── cargar datos

cleaning.py
      │
      └── limpiar datos

statistics.py
      │
      └── analizar datos

visualization.py
      │
      └── crear gráficos

main.py
      │
      └── coordinar todo
```

A esto se le llama ***separation of concerns (SoC)***.


### `import`

- Importar el módulo: Cuando escribimos `import calculos` le estamos diciendo a Python "Quiero utilizar el módulo calculos". Después accedemos a sus elementos mediante, p.ej., `calculos.sumar()`. Es decir: `módulo.función()`.

- Importar funciones del módulo: No siempre necesitamos importar el módulo completo. Podemos hacer `from calculos import sumar` y ahora podemos escribir directamente `resultado = sumar(10, 5)` en lugar de `resultado = calculos.sumar(10, 5)`. La sintaxis entonces será:

```python
from modulo import funcion1, funcion2
```

- Crear **alias** de paquetes: para ello seguimos la sintaxis `import <paquete> as <alias>`. Los alias permiten escribir menos, manteniendo una convención reconocible.

- Usar **imports absolutos**: aquí indicamos explícitamente toda la ruta. Seguimos la sintaxis `from <paquete>.<modulo> import <funcion>`.

- Usar **imports relativos**: Las importaciones relativas utilizan puntos iniciales. Un único punto inicial (`.`) indica una importación relativa, empezando por el paquete actual. Dos o más puntos iniciales (`..`) indican una importación relativa a los elementos primarios del paquete actual, un nivel por punto después del primero. Por ejemplo, dado el siguiente diseño de paquete:

```text
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```

En subpackage1/moduleX.py o subpackage1/__init__.py, las siguientes son importaciones relativas válidas:

```python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```

**⚠️ IMPORTANTE**: ¡Debemos evitar llamar a nuestros archivos igual que librerías estándar o librerías que vayamos a utilizar!



## 2. Paquetes
Un paquete nos permite organizar varios módulos relacionados dentro de una carpeta. Por ejemplo, en

```text
analytics/
    │
    ├── statistics.py
    ├── cleaning.py
    └── visualization.py
```

`analytics` es nuestro paquete, y cada archivo `.py` es un módulo.

### `__init__.py`
El archivo `__init__.py` dentro de una carpeta de Python tradicionalmente se utilizaba para indicar que una carpeta debía tratarse como un paquete. Siguiendo el ejemplo anterior:

```text
analytics/
├── __init__.py
├── statistics.py
└── cleaning.py
```

Sin embargo, en versiones modernas de Python existen también los ***namespace packages***, por lo que `__init__.py` no siempre es estrictamente necesario. Sin embargo, en nuestros proyectos lo utilizaremos porque:

- hace explícita la intención de la carpeta;
- facilita la organización;
- permite inicializar/configurar el paquete;
- es una convención muy habitual.


## 3. `if __name__ == __main__`
Cada módulo tiene un atributo `__name__`. Python asigna a esta variable el nombre del módulo, que el sistema de importación de Python utiliza para identificar cada módulo de forma única. Sin embargo, si este se encuentra en el entorno de código de nivel superior —lo que significa que es el módulo utilizado como punto de entrada del programa—, Python asigna al atributo `__name__` la cadena «__main__».

Veamos un ejemplo:

```python
# exploring_name_main.py
import random
print(__name__)
print(random.__name__)
```

El resultado será:

```text
__main__
random
```

Esto es así porque el script `exploring_name_main.py` se encuentra en el entorno de código de nivel superior, ya que es el punto de entrada del programa. Por lo tanto, la variable __name__ se establece en la cadena «__main__». En cambio, el módulo `random` se importa y no se encuentra en el entorno de código de nivel superior, por tanto su atributo __name__ se establece en el nombre del módulo.

Ahora creamos un nuevo script llamado `more_exploration.py`, que importa el primer script:

```python
# more_exploration.py
import exploring_name_main
```

Si corremos el script en la terminal, el resultado será el siguiente:

```text
exploring_name_main
random
```

Dado que `exploring_name_main.py` ya no es el punto de entrada del programa, su atributo __name__ se establece con el nombre del script en lugar de «__main__».

Así que este condiconal, presente en todos los módulos de Python permite que un archivo tenga dos funciones:

```text
ARCHIVO PYTHON
      │
      ├── Puede ser IMPORTADO
      │      │
      │      └── Proporciona funciones
      │
      └── Puede ser EJECUTADO
             │
             └── Ejecuta código de prueba
```

Por ejemplo:

```python
# operaciones.py
def calcular_media(datos):
    return sum(datos) / len(datos)

if __name__ == "__main__":
    ventas = [100, 150, 200]
    resultado = calcular_media(ventas)
    print(resultado)
```

Aquí vemos claramente dos acciones separables:

```text
def calcular_media()
    │
    └── ¿QUÉ hace el programa?

if __name__ == "__main__":
    │
    └── ¿CUÁNDO debe arrancar?
```

Así que podemos probar el módulo directamente, pero cuando otro archivo lo importa (haciendo `from operaciones import calcular_media`) solo obtiene la función y no ejecuta automáticamente el código de prueba.

**⚠️ IMPORTANTE: El condicional `if __name__ == __main__` No es obligatorio ponerlo siempre.** Se convierte en una buena práctica especialmente cuando queremos que un archivo pueda ser importado sin ejecutar automáticamente su lógica principal.

