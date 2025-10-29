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

    nombre_buscado = input("Ingrese el nombre del producto a buscar: ")

    producto_encontrado = None
    for producto in productos:
        if producto['nombre'].lower() == nombre_buscado.lower():
            producto_encontrado = producto
            break

    if producto_encontrado:
        print("\n--- Producto Encontrado ---")
        print(f"Nombre: {producto_encontrado['nombre']}")
        print(f"Precio: ${producto_encontrado['precio']:.2f}")
        print(f"Cantidad: {producto_encontrado['cantidad']}")
    else:
        print(f"\nError: El producto '{nombre_buscado}' no fue encontrado.")

    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("\nEl archivo productos.txt ha sido actualizado.")

except FileNotFoundError:
    print("Error: El archivo 'productos.txt' no fue encontrado.")
    print("Por favor, ejecute primero el script 'crear_productos.py' para generarlo.")
