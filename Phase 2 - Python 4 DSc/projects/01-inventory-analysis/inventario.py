productos = [
    {
        "nombre": "Portátil Lenovo",
        "categoria": "Informática",
        "precio": 799.99,
        "stock": 4
    },
    {
        "nombre": "Monitor Samsung",
        "categoria": "Informática",
        "precio": 249.99,
        "stock": 12
    },
    {
        "nombre": "Teclado Logitech",
        "categoria": "Periféricos",
        "precio": 59.99,
        "stock": 25
    },
    {
        "nombre": "Ratón Logitech",
        "categoria": "Periféricos",
        "precio": 29.99,
        "stock": 3
    },
    {
        "nombre": "Auriculares Sony",
        "categoria": "Audio",
        "precio": 89.99,
        "stock": 8
    },
    {
        "nombre": "Webcam Logitech",
        "categoria": "Periféricos",
        "precio": 69.99,
        "stock": 15
    }
]

# Mostrar el catálogo (p.ej.: Portátil Lenovo — 799.99 € — Stock: 4)
for producto in productos:
    print(f"{producto['nombre']} — {producto['precio']} € — Stock: {producto['stock']}")

# Calcular el número total de productos
total_productos = len(productos)
print(f"\nNúmero de productos diferentes: {total_productos}")

# Valor del inventario
valor_total_inventario = sum(producto['precio'] * producto['stock'] for producto in productos)
print(f"\nValor total del inventario: {valor_total_inventario:.2f} €")

# Productos con stock bajo (menos de 10 unidades)
productos_bajo_stock = [producto for producto in productos if producto['stock'] < 10]
print("\nProductos con stock bajo:")
for producto in productos_bajo_stock:
    print(f"- {producto['nombre']}")

# Stock crítico (menos de 5 unidades)
if any(producto['stock'] < 5 for producto in productos):
    print("\nALERTA: Existe al menos un producto con stock crítico")
else:
    print("\nNo hay productos con stock crítico")

# Producto más caro
producto_mas_caro = max(productos, key=lambda x: x['precio'])
print(f"\nProducto más caro: {producto_mas_caro['nombre']} — {producto_mas_caro['precio']} €")

# Ordenar catálogo
catalogo_ordenado = sorted(productos, key=lambda x: x['precio'], reverse=True)
for i, producto in enumerate(catalogo_ordenado):
    print(f"{i+1}. {producto['nombre']} — {producto['precio']} €")