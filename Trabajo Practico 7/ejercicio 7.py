parcial1_aprobados = {'Ana', 'Juan', 'Maria', 'Pedro', 'Sofia'}
parcial2_aprobados = {'Luis', 'Maria', 'Carlos', 'Sofia', 'Elena'}

print("--- Listas de aprobados ---")
print(f"Parcial 1: {parcial1_aprobados}")
print(f"Parcial 2: {parcial2_aprobados}")

aprobaron_ambos = set()
for alumno in parcial1_aprobados:
    if alumno in parcial2_aprobados:
        aprobaron_ambos.add(alumno)

print("\nAlumnos que aprobaron ambos parciales:")
print(aprobaron_ambos)

aprobaron_uno_solo = set()
for alumno in parcial1_aprobados:
    if alumno not in parcial2_aprobados:
        aprobaron_uno_solo.add(alumno)
for alumno in parcial2_aprobados:
    if alumno not in parcial1_aprobados:
        aprobaron_uno_solo.add(alumno)

print("\nAlumnos que aprobaron solo uno de los dos parciales:")
print(aprobaron_uno_solo)

todos_los_aprobados = parcial1_aprobados.copy()
for alumno in parcial2_aprobados:
    todos_los_aprobados.add(alumno)

print("\nLista total de alumnos que aprobaron al menos un parcial:")
print(todos_los_aprobados)
