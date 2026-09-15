def calcular_suma(*numeros):
    return sum(numeros), len(numeros)

suma, cantidad = calcular_suma(1, 2, 3, 4, 5, 10)
print(suma, cantidad)