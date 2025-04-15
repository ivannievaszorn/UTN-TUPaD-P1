# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero=int(input("Ingrese un numero entero: "))

numero_absoluto = abs(numero)

cantidad_digitos = 0

while numero_absoluto > 0:
    numero_absoluto //= 10
    cantidad_digitos +=1

print("El numero ingresado tiene", cantidad_digitos, "digitos")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
suma = 0

if num1 == num2:
    print(f"No hay numeros entre {num1} y {num2}")
else:
    menor = min(num1,num2)
    mayor = max(num1,num2)

    for i in range (menor + 1, mayor):
        suma += i

print(f"La suma entre los numeros es {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

numero_secuencia = int(input("Ingrese un numero para sumar. Ingrese 0 para terminar: "))
suma = 0

while numero_secuencia != 0:
    suma += numero_secuencia
    numero_secuencia = int(input("Ingrese un otro numero para sumar. Ingrese 0 para terminar: "))

print(suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio = random.randint(0, 9)
numero_ingresado = int(input("Adivina un numero entre el 0 y el 9: "))
intentos = 1

while numero_ingresado != numero_aleatorio:
    intentos += 1
    numero_ingresado = int(input("Incorrecto! Intenta nuevamente: "))

if intentos >1:
    print(f"Correcto! Fueron necesarios {intentos} intentos!")
else:
    print(f"Correcto! Fue necesario solo un intento!")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range (100,-1,-2):
    print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

num = int(input("Ingrese un numero mayor a 0: "))
suma = 0

for i in range(1,num):
    suma += i

print(f"La suma entre 0 y el numero {num} es: {suma}")


# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cont = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

while cont <5:
    cont +=1
    num_entero_ingresado = int(input("Ingresar numero entero: "))
    if num_entero_ingresado%2==0:
        pares += 1
    else:
        impares +=1
    if num_entero_ingresado > 0:
        positivos +=1
    else:
        negativos +=1

print(f"Hay {pares} numeros pares, {impares} numeros impares, {positivos} numeros positivos y {negativos} numeros negativos")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_de_numeros = 100
cont = 0
suma = 0
media = 0

while cont < cantidad_de_numeros:
    cont += 1
    numero_entero_para_media = int(input("Ingrese numero entero: "))
    suma += numero_entero_para_media

media = suma / cantidad_de_numeros

print(f"La media entre los numeros ingresados es {media}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_a_invertir = int(input("Ingrese el numero a invertir: "))

numero_invertido = 0

while numero_a_invertir > 0:
    # Almacenamos el ultimo digito en la variable
    ultimo_digito = numero_a_invertir % 10 
    # Agregamos el ultimo digito al numero invertido
    numero_invertido = numero_invertido * 10 + ultimo_digito
    # Eliminamos el ultimo digito
    numero_a_invertir = numero_a_invertir // 10

print(f"El numero {numero_a_invertir} invertido es {numero_invertido}")