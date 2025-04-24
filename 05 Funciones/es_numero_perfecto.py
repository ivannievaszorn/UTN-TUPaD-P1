#Funciones

def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def informar_es_numero_perfecto(numero):
    if es_perfecto(numero):
        print(f"El numero {numero} es perfecto")
    else:
        print(f"El numero {numero} NO es perfecto")

def es_perfecto(numero):
    return sumatoria_divisores_propios(numero) == numero

def sumatoria_divisores_propios(numero):
    suma_divisores = 0
    for i in range(1, numero // 2 + 1):
        if es_multiplo(numero,i):
            suma_divisores += i
    return suma_divisores

def es_multiplo(numero, i):
    return numero % i == 0

#Programa principal
num = leer_entero_validado("Ingrese un numero entero: ", 1)
informar_es_numero_perfecto(num)