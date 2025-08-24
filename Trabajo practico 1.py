# 1)-Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2)- Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.

nombre = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola {nombre}, es un gusto conocerte!")

# 3)- Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados}

nombre, apellido, edad, lugar = input("Ingrese su nombre, apellido, edad y lugar de residencia (separados con coma por favor): ").split(',')

nombre = nombre.strip()
apellido = apellido.strip()
edad = int(edad.strip())
lugar = lugar.strip()

print(f"Hola {nombre} {apellido}, tienes {edad} años y vives en {lugar}")

# 4)- Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro

Radio = float(input("Por favor ingrese el radio de su circulo: "))
Pi = 3.14
Area = Pi * Radio ** 2
Perimetro = 2 * Pi * Radio
print(f"El Area de su circulo es {Area} y el Perimetro de su circulo es {Perimetro}")

# 5)- Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundo = input("Por favor ingrese los segundos: ")
horas = int(segundo) / 3600
print(f"La cantidad de segundos equivale a {horas} horas")

# 6)- Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

Numero = int(input("Ingrese el numero del cual desea crear la tabla: "))
print(f"{Numero} x 1 = {Numero * 1}")
print(f"{Numero} x 2 = {Numero * 2}")
print(f"{Numero} x 3 = {Numero * 3}")
print(f"{Numero} x 4 = {Numero * 4}")
print(f"{Numero} x 5 = {Numero * 5}")
print(f"{Numero} x 6 = {Numero * 6}")
print(f"{Numero} x 7 = {Numero * 7}")
print(f"{Numero} x 8 = {Numero * 8}")
print(f"{Numero} x 9 = {Numero * 9}")
print(f"{Numero} x 10 = {Numero * 10}")

#7)- Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

Numero1, Numero2 = input("Ingrese dos numeros enteros distintos de 0 (separador por coma): ").split(',')
Numero1 = float(Numero1)
Numero2 = float(Numero2)
suma = Numero1 + Numero2
division = Numero1 / Numero2
multi = Numero1 * Numero2
resta = Numero1 - Numero2
print(f"La suma de ambos es {suma}")
print(f"La dicision de ambos es {division}")
print(f"La multiplicacion de ambos es {multi}")
print(f"La resta de ambos es {resta}")

# 8)- Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altura = float(input("Por favor ingrese su altura en metros: "))
peso = float(input("Por favor ingrese su peso en KG: "))
IMC = peso / altura**2
print(f"Su indice de masa corporal es {IMC}.")

# 9)- Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

GradoC = float(input("Por favor ingrese los Grados celsius que desee convertir: "))
GradoF = 9 / 5 * GradoC + 32
print(f"La conversion de {GradoC} Celsius a Fahrenheit son {GradoF}")

# 10)- Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

Numero1, Numero2, Numero3 = input("Ingrese los 3 numeros (separados con coma): ").split(',')
Numero1 = float(Numero1)
Numero2 = float(Numero2)
Numero3 = float(Numero3)
Promedio = Numero1 + Numero2 + Numero3 / 3
print(f"El promedio de los 3 numeros es {Promedio}.")
