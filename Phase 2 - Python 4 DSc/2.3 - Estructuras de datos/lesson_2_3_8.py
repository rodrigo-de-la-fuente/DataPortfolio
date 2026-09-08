pedido = {
    "cliente": "Rodrigo",
    "productos": [
        ("Pan", 2, 1.20),
        ("Leche", 1, 1.50),
        ("Huevos", 2, 2.30),
        ("Café", 1, 4.50)
    ]
}

print(f"Cliente: {pedido['cliente']}")

for nombre, cantidad, precio in pedido["productos"]:
    total = cantidad * precio
    print(f"{nombre} - {cantidad} - {precio:.2f}€")