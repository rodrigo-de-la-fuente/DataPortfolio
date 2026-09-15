productos = [
    {"nombre": "Pan", "precio": 1.20, "stock": 20},
    {"nombre": "Leche", "precio": 1.50, "stock": 5},
    {"nombre": "Huevos", "precio": 2.30, "stock": 8},
    {"nombre": "Café", "precio": 4.50, "stock": 25},
    {"nombre": "Aceite", "precio": 7.50, "stock": 3}
]

precios = [producto['precio'] for producto in productos]
precio_total = sum(precios)
min_precio, max_precio = min(precios), max(precios)
precio_medio = precio_total / len(precios)
valor_stock = [producto['precio'] * producto['stock'] for producto in productos]
productos = sorted(productos, key=lambda x: x['precio'])