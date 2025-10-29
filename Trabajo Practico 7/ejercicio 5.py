print("--- Análisis de frases ---")

frase_usuario = input("Por favor, ingrese una frase: ")

frase_limpia = frase_usuario.lower().replace(',', '').replace('.', '').replace(';', '')
lista_palabras = frase_limpia.split()

palabras_unicas = set(lista_palabras)
print("\nPalabras únicas en la frase:")
print(palabras_unicas)

frecuencia_palabras = {}
for palabra in lista_palabras:
    frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1

print("\nFrecuencia de cada palabra:")
print(frecuencia_palabras)
