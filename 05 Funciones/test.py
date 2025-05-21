# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.

def pedir_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el numero 1: "))
            num2 = float(input("Ingrese el numero 2: "))
            num3 = float(input("Ingrese el numero 3: "))
            return num1, num2, num3
        except ValueError:
            print("Error. Debe ingresar un valor numérico.")

def calcular_promedio(a, b, c):
    round((a + b + c) / 3 , 2)
    return promedio

# Programa principal
num1, num2, num3 = pedir_numeros()
promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio es: {promedio}")