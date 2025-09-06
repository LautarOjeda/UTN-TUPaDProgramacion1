#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100  (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 
num = int(input("Ingrese un numero entero: "))
if num >= 0:
    digitos = len(str(num))
    print(f"El numero {num} tiene {digitos} digitos.")
else:
    digitos = len(str(abs(num)))
    print(f"El numero {num} tiene {digitos} digitos.") 

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores  dados por el usuario, excluyendo esos dos valores.

Num1 = int (input("Ingrese el primer numero: "))
Num2 = int(input("Ingrese el segundo numero:"))
suma = 0
for i in range (Num1 + 1, Num2 + 1):
    suma += i
    print (f"Suma parcial: {suma} (sumando {i})")
print (f"Suma final: {suma}")

#4)- Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

Num = int(input("Ingrese un numero (0 para salir):"))
Suma= 0
while Num!= 0:
    Suma += Num
    print (f"Suma parcial: {Suma} (sumando {Num})")
    Num = int(input("Ingrese otro numero (0 para salir):"))
print (f"Suma final: {Suma}")

#5)- Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

import random
numero_aleatorio = random.randint(0,100)
Intento= 0
Adivina = -1
while Adivina != numero_aleatorio:
    Adivina = int(input("Adivine el numero entre 0 y 100:"))
    Intento += 1
    if Adivina < numero_aleatorio:
        print("El numero es mayor")
    elif Adivina > numero_aleatorio:
        print("El numero es menor")
print (f"Bien hecho! Adivinaste el numero {numero_aleatorio} en {Intento} intentos.")

#6)- Desarrolla un programa que imprima en pantalla todos los números pares comprendidos  entre 0 y 100, en orden decreciente.
for i in range (100, -1, -1):
    if i % 2 == 0:
        print(i)

#7)- Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario. 

Num= int(input("Ingrese un numero entero positivo:"))
Num= abs(Num)
Suma= 0
for i in range (Num + 1):
    Suma += i
    print (f"Suma parcial: {Suma} (sumando {i})")
print (f"Suma final: {Suma}")

#8)- Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son  negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
Pares = 0
Impares = 0
Negativos = 0
Positivos = 0
flag = 0

while flag < 10:
    Num = int(input("Ingrese un numero entero: "))
    if Num % 2 == 0:
        Pares += 1
    else:
        Impares += 1
    if Num < 0:
        Negativos += 1
    else:
        Positivos += 1
    flag += 1

print(f"Pares: {Pares}")
print(f"Impares: {Impares}")
print(f"Negativos: {Negativos}")
print(f"Positivos: {Positivos}")

# 9)-  Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la  media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe  poder procesar 100 números cambiando solo un valor). 

Suma = 0
flag = 0
cantidad = 10

while flag < cantidad:
    Num = int(input("Ingrese un numero entero: "))
    if Num < 0:
        Num = abs(Num)
    Suma += Num
    flag += 1

Media = Suma / cantidad
print(f"La media de los {cantidad} números ingresados es: {Media}")

#10)-  Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
Num = int(input("Ingrese un numero entero: "))
Num = abs(Num)
Num_Invertido = 0
while Num > 0:
    digito = Num % 10
    Num_Invertido = Num_Invertido * 10 + digito
    Num = Num // 10
print(f"El numero invertido es: {Num_Invertido}")

#Comentario, esta es una forma que vi, pero no estaba del todo seguro porque no entendia bien como funcionaba, pero al parecer al iniciar el bucle for a la variable "digito" Ya se le asigna automaticamente cada caracter de la cadena, lo pongo solo como por las dudas.
# Num = int(input("Ingrese un numero entero: "))
# Num_str = str(abs(Num))
# Num_invertido = ""

# for digito in Num_str:
#     Num_invertido = digito + Num_invertido
# print(f"El numero invertido es: {Num_invertido}")