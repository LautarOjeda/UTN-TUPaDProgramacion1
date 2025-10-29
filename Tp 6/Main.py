#1-
from funcion_1 import (imprimir_hola_mundo, saludar_usuario, informacion_personal,
                       calcular_area_circulo, calcular_perimetro_circulo, segundos_a_horas, tabla_multiplicar,
                       operaciones_basicas, calcular_imc, celsius_a_fahrenheit, calcular_promedio)

def main():
    #1-
    imprimir_hola_mundo()

    #2-
    nombre_ingresado = input("Por favor, ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_ingresado)
    print(saludo)

    #3-
    print("\n--- Información Personal ---")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    #4-
    print("\n--- Cálculo de Círculo ---")
    while True:
        try:
            radio_str = input("Ingresa el radio del círculo: ")
            radio = float(radio_str)
            break
        except ValueError:
            print("Error: Por favor, ingresa un número válido para el radio.")
    
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

    #5-
    print("\n--- Conversor de Segundos a Horas ---")
    while True:
        try:
            segundos_str = input("Ingresa la cantidad de segundos a convertir: ")
            segundos = float(segundos_str)
            break
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
    
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.4f} horas.")

    #6-
    print("\n--- Tabla de Multiplicar ---")
    while True:
        try:
            numero_str = input("Ingresa un número para ver su tabla de multiplicar: ")
            numero_tabla = int(numero_str)
            break
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
    
    tabla_multiplicar(numero_tabla)

    #7-
    print("\n--- Operaciones Básicas ---")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    suma, resta, multi, div = operaciones_basicas(num1, num2)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multi}")
    print(f"División: {div}")

    #8-
    print("\n--- Calculadora de IMC ---")
    while True:
        try:
            peso_kg = float(input("Ingresa tu peso en kg: "))
            altura_m = float(input("Ingresa tu altura en metros: "))
            if peso_kg <= 0 or altura_m <= 0:
                print("El peso y la altura deben ser números positivos.")
                continue
            break
        except ValueError:
            print("Error: Ingresa valores numéricos válidos.")
    
    imc = calcular_imc(peso_kg, altura_m)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")

    #9-
    print("\n--- Conversor de Celsius a Fahrenheit ---")
    while True:
        try:
            celsius = float(input("Ingresa la temperatura en grados Celsius: "))
            break
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")
    
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F.")

    #10-
    print("\n--- Calculadora de Promedio ---")
    numeros_promedio = []
    for i in range(3):
        while True:
            try:
                num_str = input(f"Ingresa el número {i+1}: ")
                numero = float(num_str)
                numeros_promedio.append(numero)
                break
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")
    
    promedio = calcular_promedio(numeros_promedio[0], numeros_promedio[1], numeros_promedio[2])
    print(f"El promedio de los tres números es: {promedio:.2f}")

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("\nSe ha producido un error. Asegúrate de ingresar números cuando se solicitan.")
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
    finally:
        print("\n--- Fin del programa ---")
