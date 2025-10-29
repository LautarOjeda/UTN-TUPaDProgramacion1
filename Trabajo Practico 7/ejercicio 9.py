agenda = {}

print("--- Agenda de Eventos ---")

agenda[('Lunes', 10)] = "Reunión de proyecto"
agenda[('Miércoles', 16)] = "Cita con el dentista"
agenda[('Viernes', 20)] = "Cena con amigos"

print("Agenda inicial:")
print(agenda)

print("\n--- Consultar un evento ---")
dia_consulta = input("Ingrese el día que desea consultar: ").capitalize()
hora_consulta = int(input("Ingrese la hora que desea consultar: "))

evento_encontrado = agenda.get((dia_consulta, hora_consulta))

if evento_encontrado:
    print(f"Evento a las {hora_consulta}hs del {dia_consulta}: {evento_encontrado}")
else:
    print(f"No hay eventos programados para el {dia_consulta} a las {hora_consulta}hs.")

print("\nAgenda final:")
print(agenda)
