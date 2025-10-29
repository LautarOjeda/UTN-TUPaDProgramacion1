# 4)-
agenda_telefonica = {}

print("--- Carga de contactos ---")
print("Por favor, ingrese 5 contactos.")

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de teléfono de '{nombre}': ")
    
    agenda_telefonica[nombre] = numero
    print("¡Contacto guardado!\n")

print("\n--- Consulta de contactos ---")
nombre_a_buscar = input("Ingrese el nombre del contacto que desea buscar: ")


numero_encontrado = agenda_telefonica.get(nombre_a_buscar)

if numero_encontrado:
    print(f"El número de teléfono de '{nombre_a_buscar}' es: {numero_encontrado}")
else:
    print(f"El contacto '{nombre_a_buscar}' no se encuentra en la agenda.")
