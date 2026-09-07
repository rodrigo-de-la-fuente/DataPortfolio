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


