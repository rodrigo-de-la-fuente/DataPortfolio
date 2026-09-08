productos = [
    ("Pan", 1.20),
    ("Leche", 1.50),
    ("Huevos", 2.30),
    ("Café", 4.50),
    ("Arroz", 1.80)
]

for nombre, precio in productos:
    print(f"{nombre} - {precio * 1.21:.2f}€")