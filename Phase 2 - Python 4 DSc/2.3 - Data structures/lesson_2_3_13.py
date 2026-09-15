productos = [
    {
        "nombre": "Portátil",
        "categoria": "Informática",
        "precio": 900,
        "stock": 5
    },
    {
        "nombre": "Monitor",
        "categoria": "Informática",
        "precio": 300,
        "stock": 12
    },
    {
        "nombre": "Teclado",
        "categoria": "Periféricos",
        "precio": 80,
        "stock": 20
    },
    {
        "nombre": "Ratón",
        "categoria": "Periféricos",
        "precio": 25,
        "stock": 35
    }
]

print('Tenemos', len(productos),'productos')

mas_caro = max(producto['precio'] for producto in productos)
any_critical = any(producto['stock'] < 10 for producto in productos)
productos = [producto['nombre'] for producto in productos if producto['stock'] < 10]
print('El producto más caro cuesta', mas_caro, '€')
print('Hay algún producto con stock crítico?', any_critical)
print('Los productos con stock crítico son:', productos)