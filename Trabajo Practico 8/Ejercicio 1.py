#1-

productos = [
    "Manzana,1.50,100\n",
    "Leche,0.99,50\n",
    "Pan,0.75,200\n"
]

with open('productos.txt', 'w') as archivo:
    archivo.writelines(productos)

print("El archivo 'productos.txt' ha sido creado/reiniciado exitosamente.")
