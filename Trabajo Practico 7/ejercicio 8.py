stock_productos = {'tornillos': 100, 'tuercas': 150, 'arandelas': 300}

print("--- Gestión de Stock ---")
print(f"Stock inicial: {stock_productos}")

producto_consulta = input("\nIngrese el nombre del producto a consultar/agregar: ").lower()

if producto_consulta in stock_productos:
    print(f"Stock actual de '{producto_consulta}': {stock_productos[producto_consulta]}")
    
    unidades_a_agregar = int(input("Ingrese la cantidad de unidades a agregar al stock: "))
    stock_productos[producto_consulta] += unidades_a_agregar
    
    print(f"¡Stock actualizado! Nuevo stock de '{producto_consulta}': {stock_productos[producto_consulta]}")
else:
    print(f"El producto '{producto_consulta}' es nuevo.")
    
    stock_inicial = int(input("Ingrese el stock inicial para este nuevo producto: "))
    stock_productos[producto_consulta] = stock_inicial
    
    print(f"¡Producto nuevo agregado! Stock de '{producto_consulta}': {stock_productos[producto_consulta]}")

print(f"\nStock final: {stock_productos}")
