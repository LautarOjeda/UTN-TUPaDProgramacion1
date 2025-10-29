alumnos_notas = {}

print("--- Carga de notas de alumnos ---")

for _ in range(3):
    nombre_alumno = input("\nIngrese el nombre del alumno: ")
    notas_list = []
    for i in range(3):
        nota = float(input(f"Ingrese la nota {i + 1} de '{nombre_alumno}': "))
        notas_list.append(nota)
    
    alumnos_notas[nombre_alumno] = tuple(notas_list)

print("\n--- Promedio de cada alumno ---")
for alumno, notas in alumnos_notas.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de '{alumno}' es: {promedio:.2f}")
