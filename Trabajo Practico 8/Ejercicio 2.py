#2-

try:
    with open('productos.txt', 'r') as archivo:
        print("--- Lista de Productos ---")
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(',')
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no fue encontrado.")
    print("Por favor, ejecute primero el script 'crear_productos.py' para generarlo.")
