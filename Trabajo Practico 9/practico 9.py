# practico 9

# 1) Función recursiva para calcular el factorial y mostrar la serie.
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 2) Función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# 3) Función recursiva que calcule la potencia de un número base elevado a un exponente.
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    return base * potencia(base, exponente - 1)

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario.
def decimal_a_binario(n):
    if n < 0:
        return "-" + decimal_a_binario(-n)
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que devuelva True si es un palíndromo o False si no lo es.
def es_palindromo(palabra):
    palabra = palabra.lower()
    if len(palabra) <= 1:
        return True
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    return False

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que devuelva la suma de todos sus dígitos.
def suma_digitos(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# 7) Escribí una función recursiva contar_bloques(n) que devuelva el total de bloques que necesita para construir toda la pirámide.
def contar_bloques(n):
    if n <= 0:
        return 0
    return n + contar_bloques(n - 1)

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que devuelva cuántas veces aparece ese dígito.
def contar_digito(numero, digito):
    if numero == 0 and digito == 0:
        return 1
    if numero == 0:
        return 0
    
    numero = abs(numero)
    contador = 1 if numero % 10 == digito else 0
    return contador + contar_digito(numero // 10, digito)

def main():
    """Función principal para ejecutar y probar todos los ejercicios."""
    print("--- Ejercicio 1: Factoriales ---")
    try:
        num_fact = int(input("Ingrese un número entero para calcular factoriales: "))
        if num_fact < 0:
            print("Por favor, ingrese un número no negativo.")
        else:
            for i in range(1, num_fact + 1):
                print(f"El factorial de {i} es {factorial(i)}")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

    print("\n--- Ejercicio 2: Serie de Fibonacci ---")
    try:
        pos_fib = int(input("Ingrese una posición para la serie de Fibonacci: "))
        if pos_fib < 0:
            print("Por favor, ingrese una posición no negativa.")
        else:
            serie = [str(fibonacci(i)) for i in range(pos_fib + 1)]
            print(f"La serie de Fibonacci hasta la posición {pos_fib} es: {' '.join(serie)}")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

    print("\n--- Ejercicio 3: Potencia Recursiva ---")
    try:
        base = int(input("Ingrese el número base: "))
        exponente = int(input("Ingrese el exponente: "))
        print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")
    except ValueError:
        print("Entrada no válida. Ambos deben ser números enteros.")

    print("\n--- Ejercicio 4: Decimal a Binario ---")
    try:
        num_dec = int(input("Ingrese un número entero para convertir a binario: "))
        print(f"El número {num_dec} en binario es: {decimal_a_binario(num_dec)}")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

    print("\n--- Ejercicio 5: Palíndromo ---")
    palabra_pal = input("Ingrese una palabra para verificar si es un palíndromo: ")
    if es_palindromo(palabra_pal):
        print(f"'{palabra_pal}' SÍ es un palíndromo.")
    else:
        print(f"'{palabra_pal}' NO es un palíndromo.")

    print("\n--- Ejercicio 6: Suma de Dígitos ---")
    try:
        num_sum = int(input("Ingrese un número para sumar sus dígitos: "))
        print(f"La suma de los dígitos de {num_sum} es: {suma_digitos(num_sum)}")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

    print("\n--- Ejercicio 7: Pirámide de Bloques ---")
    try:
        num_bloques = int(input("Ingrese el número de bloques en la base de la pirámide: "))
        print(f"El total de bloques para una base de {num_bloques} es: {contar_bloques(num_bloques)}")
    except ValueError:
        print("Entrada no válida. Debe ser un número entero.")

    print("\n--- Ejercicio 8: Contar Dígito ---")
    try:
        num_contar = int(input("Ingrese un número entero: "))
        dig_contar = int(input("Ingrese el dígito que desea contar (0-9): "))
        if 0 <= dig_contar <= 9:
            print(f"El dígito {dig_contar} aparece {contar_digito(num_contar, dig_contar)} veces en {num_contar}.")
        else:
            print("El dígito debe estar entre 0 y 9.")
    except ValueError:
        print("Entrada no válida. Ambos deben ser números enteros.")

if __name__ == "__main__":
    main()