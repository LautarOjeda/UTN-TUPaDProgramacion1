#1-  Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
multiplos4 = list(range(4, 101, 4))
print("Números del 1 al 100 que son múltiplos de 4:", multiplos4)

#2- Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
lista=["Videojuegos","Libros","Musica","Gatos","Arroz"]
print("El penúltimo elemento de la lista es:", lista[-2])

#3)- 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

palabras = []
palabras.append("Miku")
palabras.append("Rin")
palabras.append("Len")
print("Lista de palabras:", palabras)

#4)- Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla.

animales = ["perro","gato","conejo","pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("Lista de animales modificada:", animales)

#5)- El programa lo que realiza es que, con la funcion "max" busca el valor maximo dentro de la lista (en este caso el 22), lo elimina y despues lo imprime habiendo eliminado el numero 22.

#6)-  Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros

numeros = list(range(10, 31, 5))
print("Los dos primeros números de la lista son:", numeros[:2])

#7)-Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan","polo","suran","gol"]
autos[1:3] = ["Nuevito","Full"]
print("Lista de autos modificada:", autos)

#8)-  Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)
print("Lista de dobles:", dobles)

#9)-  Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan","leche"],["arroz","fideos","salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print("Lista de compras modificada:", compras)

#10)- Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista = [15, True, [25.5, 57.9, 30.6], False]
print("Lista anidada:", lista)