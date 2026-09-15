productos = ["Pan", "Leche", "Huevos", "Café", "Arroz"]
precios = [1.20, 1.50, 2.30, 4.50, 1.80]

sum = 0
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - {precios[i]}€")
    sum += precios[i]

print('Total:',sum)
    