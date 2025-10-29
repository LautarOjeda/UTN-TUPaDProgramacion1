#4-
productos = []

try:
    with open('productos.txt', 'r') as archivo:
        for linea in archivo:
            if linea.strip():
                nombre, precio, cantidad = linea.strip().split(',')
                producto = {
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                }
                productos.append(producto)

    print("--- Productos cargados en una lista de diccionarios ---")
    print(productos)

except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no fue encontrado.")
    print("Por favor, ejecute primero el script 'crear_productos.py' para generarlo.")
