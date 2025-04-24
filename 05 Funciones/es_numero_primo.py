#Funciones declaradas
def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def obtener_resto(num1, num2):
    return num1 - num2 * (num1 // num2) # Sin usar operador %

def es_multiplo(x, y):
    return obtener_resto(x, y) == 0

def es_primo(numero):
    cont = 2
    mitad = numero // 2
    while cont <= mitad and not es_multiplo(numero, cont):
        cont += 1
    return cont > mitad

def informar_si_numero_es_primo(numero):
    if es_primo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} NO es primo")

# Programa principal
num = leer_entero_validado("Ingrese un número natural", 1)
informar_si_numero_es_primo(num)