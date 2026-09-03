# Lección 2.1.1 — Sintaxis esencial de Python

## Objetivo

Al terminar 2.1.1, debes ser capaz de escribir y ejecutar pequeños programas Python correctamente, entender la estructura básica de un bloque de código y detectar errores sintácticos sencillos.

## 1. Concepto

La sintaxis es el conjunto de reglas que determinan **cómo debemos escribir código Python para que el intérprete pueda entenderlo**.

Python tiene una característica especialmente importante:

> **La estructura del código se expresa mediante la indentación.**

Por ejemplo:

```python
if temperature > 20:
    print("Hace calor")
```

La indentación indica que `print()` pertenece al bloque `if`. Esto es diferente de otros lenguajes que utilizan `{}` para delimitar bloques de código.


## 2. Comentarios

Los comentarios sirven para explicar el código y no son ejecutados por Python:

```python
# Este es un comentario
print("Hola")
```

También podemos colocar un comentario después de una instrucción:

```python
print("Hola")  # Mostramos un saludo
```

### Regla profesional

No debemos llenar el código de comentarios que simplemente repitan lo que hace el código.

❌ Poco útil:

```python
# Sumamos a y b
result = a + b
```

✅ Más útil:

```python
# Ajuste por inflación antes de comparar las ventas
adjusted_sales = sales * inflation_factor
```

El comentario debe explicar por qué hacemos algo, cuando el código por sí mismo no lo deja claro.

## 3. Indentación

La indentación es fundamental en Python. Habitualmente utilizaremos 4 espacios:

```python
if condition:
    instruction()
```

Así, este es un código correcto:

```python
if sales > 1000:
    print("Good sales")
```

Y este es un código incorrecto:

```python
if sales > 1000:
print("Good sales")
```

Python producirá un error porque `print()` debería estar indentado.

Cuando tenemos estructuras anidadas:

```python
if condition:
    if another_condition:
        print("Both conditions are true")
```

Visualmente quedaría:

```text
if
└── if
    └── print
```

> **La indentación no es decoración. Forma parte de la sintaxis de Python.**

## 5. : y bloques de código

Cuando una estructura va a contener un bloque de código, normalmente termina en `:`. Por ejemplo:

```python
if age >= 18:
    print("Adult")
```

Más adelante veremos los bucles `for`, `while`, los condicionales `if-else`, los objetos `class`... Todos utilizan esta idea:

```text
estructura:
    bloque de código
```

## 6. Mayúsculas y minúsculas

Python distingue entre mayúsculas y minúsculas. Esto: `name = "Rodrigo"`, no es lo mismo que: `Name = "Rodrigo"`, ni que: `NAME = "Rodrigo"`. Son tres nombres diferentes. Por eso debemos mantener una nomenclatura consistente. La convención habitual será:

```text
user_name
total_sales
mean_temperature
data_frame
```

No:

```text
userName
TotalSales
MeanTemperature
```

En Python utilizaremos principalmente ***snake_case***.

## 7. Varias instrucciones

Podemos escribir varias instrucciones en líneas diferentes:

```python
name = "Ana"
age = 25
print(name)
print(age)
```

Es preferible mantener una instrucción por línea. Aunque Python permite determinadas expresiones más compactas, no queremos escribir código innecesariamente difícil de leer.

## 8. La importancia de los errores

Durante esta fase vamos a adoptar una idea fundamental: Los errores forman parte del proceso normal de programación. Por ejemplo:

```python
print("Hello"
```

producirá un error de sintaxis. No debemos intentar memorizar todos los errores. Debemos aprender a:

```text
ERROR
  ↓
LEER EL MENSAJE
  ↓
LOCALIZAR EL PROBLEMA
  ↓
ENTENDERLO
  ↓
CORREGIRLO
  ↓
VOLVER A EJECUTAR
```

Esto será especialmente importante cuando empecemos a trabajar con datasets.


# Lección 2.1.2 — Tipos de datos

En la lección anterior aprendimos cómo escribir sintaxis válida en Python. Ahora necesitamos entender qué tipo de información estamos manejando. Esto es fundamental para Data Analytics, porque cuando trabajemos con datasets tendremos columnas que contienen números, texto, fechas, valores booleanos, valores ausentes... Y Python necesita saber qué tipo de dato tiene cada valor para poder operar correctamente con él.

## 1. Los tipos de datos básicos

Los principales tipos que utilizaremos son:

|Tipo|Nombre Python|Ejemplo|
|----|-------------|-------|
|Entero|`int`|`25`|
|Decimal|`float`|`3.14`|
|Texto|`str`|`"Python"`|
|Booleano|`bool`|`True`/`False`|
|Nulo|`NoneType`|`None`|

Podemos visualizarlo así:

```markdown
                    DATOS
                      │
       ┌──────────────┼──────────────┐
       ↓              ↓              ↓
    NÚMEROS         TEXTO        LÓGICOS
       │              │              │
   ┌───┴───┐          │          True / False
   ↓       ↓          ↓
  int    float       str
   │       │          │
  10     3.14      "Python"
```

## 2. int — números enteros

Representan números sin decimales:

```python
age = 28
movies = 150
year = 2026
```

Podemos comprobar el tipo haciendo `type(x)`:

```python
print(type(age))
```

Que da como resultado:

```python
<class 'int'>
```

## 3. float — números decimales

Representan números con decimales:

```python
temperature = 23.5
price = 19.99
rating = 8.7
print(type(rating))
```

Resultado:

```python
<class 'float'>
```

## 4. str — cadenas de texto
Un str representa texto. Podemos utilizar comillas simples: `name = 'Python'`, o dobles: `name = "Python"`. Ambas son válidas. Por ejemplo:

```python
movie = "Interstellar"
```

Podemos comprobarlo:

```python
print(type(movie))
```

Resultado:

```python
<class 'str'>
```

**Importante**: Aunque parezcan números, esto: `year = "2026"` es texto, no un número. Mientras que: `year = 2026` es un int.

## 5. bool — valores booleanos
Un booleano solamente puede tener dos valores: `True` y `False`. Por ejemplo:

```python
is_available = True
is_finished = False
```

Podemos comprobarlo:
```python
print(type(is_available))
```

Resultado:

```python
<class 'bool'>
```

## 6. None — ausencia de valor
Python tiene un valor especial: `None`. Representa la ausencia de un valor. Por ejemplo,

```python
result = None
```

Esto no significa `0` ni `""` ni `False`. Significa que actualmente no hay ningún valor. Esto será especialmente importante cuando trabajemos con datos reales, porque los datasets suelen contener valores ausentes.

## 7. type()
Una de las herramientas más importantes de esta lección es `type()`, que nos permite averiguar qué tipo de dato tenemos como ya hemos ido viendo.

## 8. Python es dinámicamente tipado
En Python no necesitamos declarar explícitamente el tipo de una variable. Podemos hacer `age = 30` y Python entiende que `age → int`, y posteriormente hacemos `age = "thirty"` y entonces ahora `age → str`. O sea, el tipo puede cambiar. Esto se denomina **tipado dinámico**. No obstante, que Python lo permita no significa que debamos cambiar arbitrariamente los tipos. En proyectos profesionales queremos que nuestros datos tengan sentido.

## 9. Conversión entre tipos
Podemos convertir algunos datos.

### int(), float()

```python
age = int("30")
print(age)
print(type(age))
```

produce

```python
30
<class 'int'>
```

También podemos hacer lo mismo con `float()`:

```python
price = float("19.99")
```


### str()
De la misma manera, podemos convertir un número a texto:

```python
year = 2026
year_text = str(year)
print(type(year_text))
```

Entonces tendremos:

```python
<class 'str'>
```

### bool()
También podemos convertir valores a booleanos:

```python
print(bool(1))
print(bool(0))
```

Que da como resultado:

```python
True
False
```

# Lección 2.1.3 — Variables y operadores

Ya conocemos los tipos de datos. Ahora vamos a aprender a almacenarlos, modificarlos y operar con ellos.
Esta lección es especialmente importante porque prácticamente todo programa Python consiste en:

```text
DATOS
  ↓
VARIABLES
  ↓
OPERACIONES
  ↓
RESULTADOS
```

La idea central de esta lección es que una variable almacena información y los operadores nos permiten transformar o comparar esa información.

## 1. ¿Qué es una variable?
Una variable es un nombre que utilizamos para referirnos a un valor. Por ejemplo, 

```python
age = 30
```

Esto podemos imaginarlo como una etiqueta:

```text
┌─────────────┐
│     age     │
│      ↓      │
│     30      │
└─────────────┘
```

Otro ejemplo:

```python
dataset_name = "movies.csv"
number_of_movies = 1500
average_rating = 7.8
```

Entonces tenemos:

```text
dataset_name       → "movies.csv"    → str
number_of_movies   → 1500            → int
average_rating     → 7.8             → float
```

## 2. Crear y modificar variables
Podemos modificar el valor de una variable haciendo lo siguiente:

```python
count = 10
count = 20
```

Al final:

```python
print(count)
```

produce `20`. El segundo valor sustituye al anterior. También podemos modificarla utilizando su valor actual:

```python
count = 10
count = count + 5
```

Así que ahora `count = 15`

## 3. Reglas para nombrar variables
Un nombre de variable puede contener letras y números, pero no puede comenzar por un número. Así que...

✅ Correcto:
```python
movie_count = 100
year_2026 = 2026
average_rating = 8.2
```

❌ Incorrecto:
```python
2movies = 100
```

Tampoco podemos utilizar espacios: ❌ `movie count = 100`
En su lugar utilizamos: ✅ `movie_count = 100`

En Python utilizaremos normalmente ***snake_case***:

```python
number_of_movies = 500
average_movie_rating = 7.8
dataset_name = "movies.csv"
```
Esto será importante para que nuestro proyecto mantenga un estilo profesional.

## 4. Operadores

### Operadores aritméticos
Python permite realizar operaciones matemáticas directamente mediante los operadores `+` (suma), `-` (resta), `*` (multiplicación), `/` (división), `//` (división entera), `%` (resto), `**` (potencia).


### Operadores de comparación
También podemos comparar valores usando `==`, `!=`, `>`, `<`, `>=`, `<=`. Todos ellos producen un booleano. Más adelante utilizaremos estos resultados para filtrar datasets.

### = frente a ==
Esta diferencia es fundamental. `=` significa asignación:

```python
rating = 8.5
```

Estamos diciendo "Guarda 8.5 en rating".

En cambio, `==` significa comparación:

```python
rating == 8.5
```
Aquí estamos preguntando "¿rating es igual a 8.5?".

Por tanto:
```text
=   → asignar
==  → comparar
```

### Operadores lógicos
Podemos combinar condiciones mediante:
and
or
not
and
Ambas condiciones deben cumplirse:
rating > 8 and year > 2010
or
Al menos una debe cumplirse:
genre == "Drama" or genre == "Comedy"
not
Invierte el resultado:
not is_loaded
Estos operadores serán esenciales en la próxima lección cuando estudiemos estructuras de control.
10. Operadores de asignación
Existe una forma abreviada de modificar variables.
Tenemos:
count = count + 1
Podemos escribir:
count += 1
Lo mismo ocurre con:
count -= 1
count *= 2
count /= 2
Ejemplo:
movies = 100

movies += 50
print(movies)
Resultado:
150
11. Operaciones con texto
Los operadores también pueden utilizarse con str.
Concatenación
first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)
Resultado:
John Smith
También podemos repetir texto:
print("Python " * 3)
Resultado:
Python Python Python
Pero cuidado:
"10" + "20"
no es una suma matemática.
Produce:
1020
porque son cadenas de texto.
12. Precedencia de operaciones
Python sigue las reglas matemáticas habituales.
result = 10 + 5 * 2
Primero:
5 × 2 = 10
Después:
10 + 10 = 20
Por tanto:
print(result)
produce:
20
Podemos utilizar paréntesis para controlar el orden:
result = (10 + 5) * 2
Ahora:
15 × 2 = 30
13. Variables y análisis de datos
Aquí empieza a aparecer una idea importante de nuestro proyecto.
Supongamos:
total_revenue = 250000
number_of_movies = 500
Podemos calcular:
revenue_per_movie = total_revenue / number_of_movies
Tenemos:
                 total_revenue
                       │
                       ÷
                       │
                 number_of_movies
                       │
                       ↓
                revenue_per_movie
Y podemos utilizar ese resultado posteriormente:
if revenue_per_movie > 400:
    print("High revenue per movie")
Estamos empezando a construir el flujo que utilizaremos durante toda la fase:
DATOS
  ↓
VARIABLES
  ↓
OPERACIONES
  ↓
RESULTADO
  ↓
DECISIÓN
14. Una advertencia importante
No debemos utilizar nombres ambiguos:
❌
x = 250000
y = 500
z = x / y
Aunque funcione, dentro de un proyecto grande será difícil entenderlo.
Mejor:
total_revenue = 250000
number_of_movies = 500
revenue_per_movie = total_revenue / number_of_movies
El segundo código prácticamente se explica solo.
Esto conecta con uno de los principios de nuestra Fase 2:
Código legible antes que código ingenioso.
15. Mini reto — 2.1.3
Crea:
lesson_2_1_3.py
Imagina que nuestro dataset contiene información sobre películas.
Define:
total_movies = ...
total_revenue = ...
total_runtime = ...
Y calcula:
1. duración media por película
2. ingresos medios por película
3. si los ingresos medios superan una cantidad que tú determines
Después muestra los resultados con print().
Por ejemplo, conceptualmente:
average_runtime = ...
average_revenue = ...

print(...)
print(...)

print(average_revenue > ...)
Condición del reto
No utilices números aleatorios sin sentido. Inventa un pequeño dataset hipotético coherente.
16. Lo que debes dominar
Al terminar 2.1.3 debes saber:
VARIABLES
   ↓
nombre = valor
ARITMÉTICA
+  -  *  /  //  %  **
COMPARACIÓN
==  !=  >  <  >=  <=
LÓGICA
and  or  not
ASIGNACIÓN
=  +=  -=  *=  /=
Y, sobre todo, entender:
=   → asigno un valor
==  → comparo dos valores



