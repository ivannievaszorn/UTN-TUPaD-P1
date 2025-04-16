# Ejercicio 10: Números primos
# Objetivo: Implementar un algoritmo con bucles anidados. Instrucciones:
# # Pide al usuario un número entero positivo.
# # Imprime todos los números primos menores o iguales a ese número.

numero = int(input("Ingrese un numero entero positivo: "))

if numero > 0:
    for num in range(2, numero + 1):
        es_primo = True
        for i in range (2, num):
            if num % i == 0:
                es_primo = False
        if es_primo:
            print(num)
else:
    print("Ingrese un número positivo")