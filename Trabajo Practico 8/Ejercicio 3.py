#3-
try:
    with open('productos.txt', 'r') as archivo:
        print("--- Lista de Productos ---")
        for linea in archivo:
            if linea.strip():
                nombre, precio, cantidad = linea.strip().split(',')
                print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

    print("\n--- Agregar Nuevo Producto ---")
    nuevo_nombre = input("Ingrese el nombre del producto: ")
    nuevo_precio = input("Ingrese el precio: ")
    nueva_cantidad = input("Ingrese la cantidad: ")

    with open('productos.txt', 'a') as archivo:
        archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

    print(f"\n¡Producto '{nuevo_nombre}' agregado exitosamente!")

except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no fue encontrado.")
    print("Por favor, ejecute primero el script 'crear_productos.py' para generarlo.")
