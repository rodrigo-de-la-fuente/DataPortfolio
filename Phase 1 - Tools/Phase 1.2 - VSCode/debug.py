def calcular_media(numeros):
    suma = 0

    for numero in numeros:
        suma += numero

    media = suma / len(numeros)

    return media


datos = [12, 15, 18, 21, 24]

resultado = calcular_media(datos)

print(resultado)