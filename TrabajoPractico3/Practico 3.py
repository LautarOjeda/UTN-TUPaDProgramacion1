#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print ("Es mayor de edad")

#2)-Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

Nota= int(input("Ingrese su nota; "))
if Nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#3)-Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num= int(input("Ingrese un numero par: "))
if num % 2 ==0:
    print ("Ha ingresado un numero par")
else: 
    print ("Por favor, ingrese un numero par")

#4)-Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál categoria pertenece segun su edad.

edad= int(input("Ingrese su edad: "))
if edad<12:
    print ("Usted es un niño")
elif edad >=12 and edad <18:
    print ("Usted es un adolescente")
elif edad >=18 and edad <30:
    print ("Usted es un adulto joven")
else:
    print ("Usted es un adulto")

#5)-Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantall el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por antalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

Password: str= input("Ingrese una contraseña entr 8 y 14 caracteres: ")
if len(Password) >=8 and len(Password) <=14:
    print ("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6)-escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
aleatorios= [random.randint(1, 100) for i in range(50)]
from statistics import mode, median, mean
lista= (aleatorios)

moda= mode(lista)
mediana= median(lista)
media= mean(lista)

print (moda)
print (mediana)
print (media)

if media > mediana and mediana > moda:
    print ("Sesgo positivo.")
elif media < mediana and mediana < moda:
    print ("Sesgo negativo")
elif media == mediana and mediana == moda:
    print ("Sin sesgo.")
else:
    print ("No se puede determinar el sesgo.")

#7)-Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

Frase= str= input("Ingrese una frase o palabra: ")
if Frase and Frase[-1].lower() in "aeiou":
    print (Frase + "!")
else:
    print (Frase)

#8 Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee

nombre= str =input ("Ingrese su nombre: ")
opcion= int (input("Ingrese 1 si quiere su nombre en mayusculas,2 si lo quiere en minusculas o 3 si quiere la primera letra en mayuscula: "))

if opcion == 1:
    print ("Su nombre en mayusculas es: " + nombre.upper())
elif opcion == 2:
    print ("Su nombre en minusculas es: " + nombre.lower())
elif opcion == 3:
    print ("Su nombre con la primera letra en mayuscula es: " + nombre.capitalize())
else:
    print ("Opcion incorrecta.")

# 9- Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:

magnitud= float (input("Ingrese la magnitud del terremoto: "))

if magnitud < 3.0:
    print ("Muy leve")
elif magnitud >= 3.0 and magnitud < 4.0:
    print ("Leve")
elif magnitud >= 4.0 and magnitud < 5.0:
    print ("Moderado")
elif magnitud >= 5.0 and magnitud < 6.0:
    print ("Fuerte")
elif magnitud >= 6.0 and magnitud < 7.0:
    print ("Muy fuerte")
elif magnitud >= 7.0:
    print ("Extremo")
else:
    pass

# 10- Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio= str(input("Ingrese en que hemisferio se encuentra (N/S): ")).strip().upper()
mes= int(input("Ingrese el mes (1-12): "))
dia= int(input("Ingrese el dia (1-31): "))

fecha = (mes, dia)

if (fecha >= (12,21) or fecha <= (3,20)):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (fecha >= (3, 21) and fecha <= (6, 20)):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (fecha >= (6, 21) and fecha <= (9, 20)):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (fecha >= (9, 21) and fecha <= (12, 20)):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

if hemisferio == "N":
    print(f"En el hemisferio norte es {estacion_norte}.")
elif hemisferio == "S":
    print(f"En el hemisferio sur es {estacion_sur}.")
else:
    print("Hemisferio no válido.")

