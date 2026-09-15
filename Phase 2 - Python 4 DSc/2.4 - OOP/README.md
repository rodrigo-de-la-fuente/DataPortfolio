# Lección 2.4.1 - Clases y objetos

## 1. Introducción
Hasta ahora hemos trabajado principalmente con estructuras como:

```python
productos = [
    {
        "nombre": "Portátil Lenovo",
        "categoria": "Informática",
        "precio": 799.99,
        "stock": 4
    },
    {
        "nombre": "Ratón Logitech",
        "categoria": "Informática",
        "precio": 29.99,
        "stock": 20
    }
]
```

Pero imagina que nuestro programa empieza a crecer y que queremos representar muchos productos, cada uno con nombre, categoría, precio, stock, comportamiento propio... Podríamos acabar manejando diccionarios por doquier. La Programación Orientada a Objetos POO (OOP en inglés) nos permite crear un modelo propio para representar ese concepto.

Este modo o paradigma de programación nos permite organizar el código de una manera que se asemeja bastante a como pensamos en la vida real, utilizando las famosas **clases**. Estas nos permiten agrupar un conjunto de variables y funciones que veremos a continuación.

Cosas de lo más cotidianas como un perro o un coche pueden ser representadas con clases. Estas clases tienen diferentes características, que en el caso del perro podrían ser la edad, el nombre o la raza. Llamaremos a estas características, **atributos**.

Por otro lado, las clases tienen un conjunto de funcionalidades o cosas que pueden hacer. En el caso del perro podría ser andar o ladrar. Llamaremos a estas funcionalidades **métodos**.

Por último, pueden existir diferentes tipos de perro. Podemos tener uno que se llama Toby o el del vecino que se llama Laika. Llamaremos a estos diferentes tipos de perro **objetos**. Es decir, el concepto abstracto de perro es la clase, pero Toby o cualquier otro perro particular será el objeto.

La programación orientada a objetos está basada en 6 principios o pilares básicos:

- Herencia
- Cohesión
- Abstracción
- Polimorfismo
- Acoplamiento
- Encapsulamiento

## 2. Definiendo una clase vacía
Lo primero es crear una clase, para ello usaremos el ejemplo del perro:

```python
# Creando una clase vacía
class Perro:
    pass
```

Se trata de una clase vacía y sin mucha utilidad práctica, pero es la mínima clase que podemos crear. Nótese el uso del `pass` que no hace realmente nada, pero daría un error si después de los `:` no tenemos contenido. Ahora ya podemos crear objetos a partir de la clase:

## 3. Objetos
Ahora que tenemos la clase, podemos crear un objeto de la misma. Podemos hacerlo como si de una variable normal se tratase. Nombre de la variable igual a la clase con `()`. Dentro de los paréntesis irían los parámetros de entrada si los hubiera:

```python
# Creamos un objeto de la clase perro
toby = Perro()
tany = Perro()
```

Y ahora tenemos:

```text
        CLASE
        Perro
          │
    ┌─────┴──────┐
    ↓            ↓
   toby         tany
  OBJETO       OBJETO
```

Así pues...
> **la clase nos permite crear una representación programática de algo que existe en nuestro problema**


Una clase puede tener dos tipos de elementos fundamentales:

```texto
OBJETO
│
├── Atributos → lo que ES / lo que TIENE
│
└── Métodos   → lo que PUEDE HACER
```


## 1. Definiendo atributos
A continuación vamos a añadir algunos atributos a nuestra clase. Antes de nada es importante distinguir que existen dos tipos de atributos:

- **Atributos de instancia**: Pertenecen a la instancia de la clase o al objeto. Son atributos particulares de cada instancia, en nuestro caso de cada perro.

- **Atributos de clase**: Se trata de atributos que pertenecen a la clase, por lo tanto serán comunes para todos los objetos.

Empecemos creando un par de atributos de instancia para nuestro perro, el `nombre` y la `raza`. Para ello creamos un método `__init__` que será llamado automáticamente cuando creemos un objeto. Se trata del **constructor**:

```python
class Perro:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza
```

Ahora que hemos definido el método *init* con dos parámetros de entrada, podemos crear el objeto pasando el valor de los atributos. Usando `type()` podemos ver como efectivamente el objeto es de la clase `Perro`.



