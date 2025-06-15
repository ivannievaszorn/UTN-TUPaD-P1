# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

from funciones import numero_entero_positivo, es_numero, validar_digito

# Funciones
def factorial(n):
    if n == 0:
        return 1
    else:
        resultado = n * factorial(n - 1)
        print(f"{n}! = {resultado}")
        return resultado
    
def pedir_y_mostrar_factoriales():
    print("\nCálculo de factoriales")
    print("----------------------")
    mensaje_pedir_numero_positivo = "Ingrese un numero entero positivo: "
    num = numero_entero_positivo(mensaje_pedir_numero_positivo)
    print(f"Factoriales entre 1 y {num}:")
    factorial(num)

# PROGRAMA PRINCIPAL
pedir_y_mostrar_factoriales()

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_serie_fibonacci(num, inicio=0):
    if inicio > num:
        return
    else:
        print(fibonacci(inicio))
        return mostrar_serie_fibonacci(num, inicio +1)
    
def pedir_y_mostrar_fibonacci():
    print("\nSerie de Fibonacci")
    print("------------------")
    mensaje_pedir_numero_positivo = "Ingrese un numero entero positivo: "
    num = numero_entero_positivo(mensaje_pedir_numero_positivo)
    print(f"Serie de Fibonacci hasta la posición {num}:")
    mostrar_serie_fibonacci(num)
    
# Programa principal
pedir_y_mostrar_fibonacci()


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 
# Prueba esta función en un algoritmo general

import math

# Funciones
def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente >0:
        return base * calcular_potencia(base, exponente - 1)
    else:
        return 1 / calcular_potencia(base, -exponente)
    
def mostrar_potencia():
    print("\n" + "-"*40)
    print("Cálculo de Potencia Recursiva")
    print("-"*40)
    base = es_numero("Ingresar la base: ")
    exponente = es_numero("Ingresar el exponente: ")
    resultado = calcular_potencia(base, exponente)
    print(f"{base} elevado a la potencia {exponente} es igual a: {resultado}")

# Llamada:
mostrar_potencia()

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto

def convertir_a_binario(numero):
    if numero <2:
        return str(numero)
    else:
        return convertir_a_binario(numero // 2) + str(numero % 2)

def pedir_y_mostrar_binario():
    print("\n" + "-"*40)
    print("Conversión a Binario")
    print("-"*40)
    numero_decimal = es_numero("Ingrese un número decimal: ")
    numero_en_binario = convertir_a_binario(numero_decimal)
    print(f"El numero {numero_decimal} en binario es {numero_en_binario}")

pedir_y_mostrar_binario()


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

import unicodedata

def limpiar_palabra():
    string = input("Ingrese la palabra (sin espacios ni tildes): ")
    # Elimina espacios y pone todo en minúscula
    string = string.replace(" ", "").lower()
    # Elimina tildes
    string = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('utf-8')
    return string

def es_palindromo(string):
    if len(string) == 0 or len(string) == 1:
        return True
    elif string[0] != string [-1]:
        return False
    else:
        return es_palindromo(string[1:-1])
    
def pedir_y_mostrar_palindromo():
    print("\n" + "-"*40)
    print("Chequeo de Palíndromo")
    print("-"*40)
    es_palindromo(limpiar_palabra())

# Programa principal
pedir_y_mostrar_palindromo()

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero // 10)

def pedir_y_mostrar_suma_digitos():
    print("\n" + "-"*40)
    print("Suma de Dígitos")
    print("-"*40)
    mensaje_pedir_numero_positivo = "Ingrese un numero entero positivo: "
    num = numero_entero_positivo(mensaje_pedir_numero_positivo)
    resultado = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es {resultado}")

pedir_y_mostrar_suma_digitos()

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)
    
print(contar_bloques(4))

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero < 10:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)
        
def pedir_y_mostrar_repeticion_de_digitos():
    print("\n" + "-"*40)
    print("Contador de Dígitos en un Número")
    print("-"*40)
    numero = numero_entero_positivo("Ingrese un numero entero positivo: ")
    digito = validar_digito("Ingrese un dígito entre 0 y 9: ")
    resultado = contar_digito(numero, digito)
    mostrar_resultado_digito(digito, resultado, numero)

def mostrar_resultado_digito(digito, resultado, numero):
    if resultado == 0:
        print(f"El dígito {digito} no se encuentra presente en el número {numero}")
    else:
        if resultado == 1:
            print(f"El dígito {digito} está presente una vez dentro del número {numero}")
        else:
            print(f"El dígito {digito} está presente {resultado} veces dentro del número {numero}")

pedir_y_mostrar_repeticion_de_digitos()