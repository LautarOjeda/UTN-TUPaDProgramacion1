#1-
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print("Diccionario original:")
print(precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("\nDiccionario con las nuevas frutas:")
print(precios_frutas)

#2-
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("\nDiccionario con precios actualizados:")
print(precios_frutas)

# 3-
lista_frutas = list(precios_frutas.keys())

print("\nLista de frutas:")
print(lista_frutas)

