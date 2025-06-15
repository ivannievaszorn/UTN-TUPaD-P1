# 1. Escribe un bucle for que imprima los números pares del 2 al 20 (inclusive).
# 2. Usa un condicional o el paso del rango para lograrlo.

# for i in range (2,21,2):
#     print(i)

# print(f"//////////////////////////////////////////////")

# # • # ¿Cómo modificarías el código para imprimir solo impares?

# for i in range (2,21):
#     if i%2!=0:
#         print(i)

# # ¿Qué pasa si el rango fuera de 2 a 20 con paso 3?
# print("¿Qué pasa si el rango fuera de 2 a 20 con paso 3?")

# for i in range (2,21,3):
#     if i%2!=0:
#         print(i)

# print(f"//////////////////////////////////////////////")

# 1. Pide al usuario que ingrese números hasta que la suma supere 100.
# 2. Imprime la suma total al final.

# suma = 0
# cont = 0

# # El bucle while corta cuando la suma supere los 100. Validamos con el try y el except que ingrese unicamente valores numericos y evitar cortar la ejecucion.
# while suma <= 100: 
#     try:
#         numero = float(input("Ingrese número: "))
#         suma += numero
#     except ValueError:
#         print("Error: Solo se permiten números.")

# print(f"La suma total de los numeros ingresados es: {suma}")


####### Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime solo las que empiezan con "a". ########

# frutas = ["apple", "banana", "avocado"]

# for i in range(len(frutas)):
#     if frutas[i][0].lower() == "a":
#         print(frutas[i])


#### Forma sugerida por ChatGPT ####

# frutas = ["Apple", "banana", "avocado"]

# for fruta in frutas:
#     if fruta.lower().startswith("a"):
#         print(fruta)

# startswith(): Verifica si la cadena comienza con el prefijo especificado (en este caso, "a").
# En lugar de usar range(len(frutas)) para acceder a los índices, 
# se puede iterar directamente sobre los elementos de la lista, lo que hace el código más limpio.


# Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).

# num_tabla = int(input("Ingrese el numero para generar la tabla de multiplicar: "))
# resultados = []

# for i in range (1,11):
#     resultados.append(num_tabla*i) # Agregamos el resultado de la multiplicación como un valor en el array resultados.
#     print(f"{num_tabla} x {i} = {resultados[i-1]}")

#################################################################################################################

# Pide al usuario una cadena de texto.
# Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.

import unicodedata  # Importa un módulo que permite manejar caracteres Unicode (como tildes)

# Función que elimina acentos/tildes del texto
def quitar_acentos(texto):
    Normaliza el texto en forma 'NFD' y elimina los caracteres de tipo 'Mn' (marca no espaciadora)
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

Texto de ejemplo con vocales acentuadas
texto = input("Ingrese la frase para contar las vocales: ")

Pasa el texto a minúsculas y le quita los acentos
texto_sin_acentos = quitar_acentos(texto.lower())

Lista de vocales que queremos contar (ya sin tildes)
vocales = "aeiou"

Diccionario vacío donde se guardará la cantidad de cada vocal
conteo = {}

Recorremos cada vocal y contamos cuántas veces aparece en el texto
for vocal in vocales:
    conteo[vocal] = texto_sin_acentos.count(vocal)

Imprimimos el resultado final
print(conteo)

# Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que aparecen más de una vez (en este caso: [3, 1]).
# Preguntas de reflexión:
# ¿Por qué es importante mantener el orden de aparición?
# ¿Cómo resolverías esto sin usar estructuras adicionales?

# lista = [3, 1, 3, 5, 1]
# dict = {}

# # Contamos las ocurrencias de cada número
# for numero in lista:
#     if numero in dict:
#         dict[numero] += 1
#     else:
#         dict[numero] = 1

# # Creamos la nueva lista con los números que se repiten
# nueva_lista = []

# for numero, veces in dict.items():
#     if veces > 1:
#         nueva_lista.append(numero)

# print(nueva_lista)

# dict.items():
# dict.items() es un método de los diccionarios en Python que devuelve una vista de los pares clave-valor del diccionario.
# En lugar de devolver solo las claves o solo los valores, devuelve una lista de tuplas en las que cada tupla tiene dos elementos:
# La clave (en este caso, el número de la lista original).
# El valor (en este caso, cuántas veces se repite ese número en la lista

# Cada tupla contiene dos elementos:
# La clave es el número (3, 1, 5).
# El valor es la cantidad de veces que aparece ese número en la lista (2, 2, 1).
# for numero, veces in dict.items()::
# Aquí estamos desestructurando las tuplas que devuelve dict.items().
# numero va a tomar el valor de la clave de cada tupla (el número de la lista original).
# veces va a tomar el valor de la cantidad de veces que ese número aparece en la lista (el valor del diccionario).


################################################################################################


# Imprime números del 1 al 100, pero:
# # Para múltiplos de 3 → "Fizz".
# # Para múltiplos de 5 → "Buzz".
# # Para múltiplos de ambos → "FizzBuzz


# for i in range (1,101):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     elif i%7 == 0:
#         print("Bazz")
#     else:
#         print(i)



#############################################################################################


# Dada una cadena (ej: "hola hola mundo"), devuelve un diccionario con la frecuencia de cada palabra (ej: {"hola": 2, "mundo": 1}).

# import string

# array_de_cadena = input("Ingrese la cadena: ").split() # split() divide caracteres por espacios.

# frecuencia_palabras = {}

# # Contamos las ocurrencias de cada palabra
# for palabra in array_de_cadena:
#     palabra = palabra.lower().strip(string.punctuation) # strip() quita los caracteres que le pase por parametro. string.punctuation trae los caracteres de puntuación.
#     if palabra in frecuencia_palabras:
#         frecuencia_palabras[palabra] += 1
#     else:
#         frecuencia_palabras[palabra] = 1

# print(frecuencia_palabras)
# print(string.punctuation) # Muestra todos los caracteres de la funcion string que usamos para buscar dentro del string y quitarlos con strip.



############################################################################################################################

# # Dada una cadena, crea una nueva cadena que solo contenga sus consonantes (ej: "Hola" → "Hl")

# import string

# # Lista de vocales que queremos contar (ya sin tildes)
# vocales = "aeiou"
# consonantes = []

# texto = input("Ingrese el texto: ").lower().strip(string.punctuation)

# for caracter in texto: 
#     if caracter.isalpha() and caracter not in vocales: #Verificamos si es alfabetico y no está en vocales.
#         consonantes.append(caracter) # Agregamos el caracter al array consonantes

# print("".join(consonantes))  # Para mostrar el resultado como una cadena.


##########################################################################################################################


# Ejercicio 10: Números primos
# Objetivo: Implementar un algoritmo con bucles anidados. Instrucciones:
# Pide al usuario un número entero positivo.
# Imprime todos los números primos menores o iguales a ese número.

# numero = int(input("Ingrese un numero entero positivo: "))

# while numero <=0:
#     numero = int(input("Error! Ingresó un numero negativo. Ingrese un numero entero positivo mayor a 1: "))

# for num in range(2, numero + 1):
#     es_primo = True
#     for i in range (2, num):
#         if num % i == 0:
#             es_primo = False
#     if es_primo:
#         print(num)


## Alternativa ##

# numero = int(input("Ingrese un numero entero positivo: "))

# if numero > 0:
#     if numero <= 2:
#         print("El número ingresado es 2 y es primo")
#     else:
#         for num in range(2, numero + 1):  # Recorrer los números hasta el número ingresado
#             es_primo = True
#             for i in range(2, int(num**0.5) + 1):  # Comprobar divisores solo hasta la raíz cuadrada de 'num'
#                 if num % i == 0:
#                     es_primo = False
#             if es_primo:
#                 print(num)  # Si es primo, lo imprimimos
# else:
#     print("Ingrese un número positivo")
