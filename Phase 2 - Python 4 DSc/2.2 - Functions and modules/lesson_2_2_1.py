def calcular_maximo(lista: list) -> float:
    lista.sort()
    return lista[-1]

numeros = [4, 8, 2, 15, 7]
resultado = calcular_maximo(numeros)
print(resultado)