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


