def calcular_media(numeros):
    suma = 0

    for numero in numeros:
        suma += numero

    media = suma / len(numeros)

    return media


datos = [7, 9, 10, 8, 6]

resultado = calcular_media(datos)

print(resultado)