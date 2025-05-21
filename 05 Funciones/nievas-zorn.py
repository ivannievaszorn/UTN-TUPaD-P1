# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. 
# Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_de_usuario = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_de_usuario)
print(saludo)

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def edad_valida():
    while True:
        try:
            edad = int(input("Ingresá tu edad: "))
            if edad > 0:
                return edad
            else:
                print("Error. Ingresá un valor positivo")
        except ValueError:
            print("Error. Ingresar un valor numérico")

def pedir_datos():
    nombre = input("Ingresar nombre: ")
    apellido = input("Ingresar apellido: ")
    edad = edad_valida()
    residencia = input("Ingresar residencia: ")
    return nombre, apellido, edad, residencia

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre, apellido, edad, residencia = pedir_datos()
print(informacion_personal(nombre, apellido, edad, residencia))

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.


import math

def calcular_area_circulo(radio):
    area=round((math.pi*radio**2), 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro=round((2*math.pi*radio), 2)
    return perimetro

def pedir_radio():
    while True:
        try:
            radio = float(input("Ingrese el radio del circulo: "))
            if radio >0:
                return radio
            else:
                print("Error. El radio debe ser un valor positivo.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico")

radio = pedir_radio()
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas=round(segundos/3600,2)
    return horas

def pedir_segundos():
    while True:
        try:
            segundos = float(input("Ingresar segundos: "))
            if segundos >0:
                return segundos
            else:
                print("Error. El numero debe ser positivo.")
        except ValueError:
            print("Error: Debe ingresar un valor numérico")
            
segundos = pedir_segundos()
horas = segundos_a_horas(segundos)

print(f"{segundos} equivale a {horas} hora(s)")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {i*numero}")

def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Error. Debe ingresar un valor numérico.")

tabla_multiplicar(pedir_numero())

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def pedir_numeros():
    while True:
        try:
            numero_uno = int(input("Ingrese el primer número: "))
            numero_dos = int(input("Ingrese el segundo número: "))
            return numero_uno, numero_dos
        except ValueError:
            print("Error. Debe ingresar un valor numérico.")

def operaciones_basicas(numero_uno, numero_dos):
    suma = numero_uno + numero_dos
    multiplicacion = numero_uno * numero_dos
    division = numero_uno / numero_dos
    resta = numero_uno - numero_dos
    return suma, multiplicacion, division, resta

numero_uno, numero_dos = pedir_numeros()
suma, multiplicacion, division, resta  = operaciones_basicas(numero_uno, numero_dos)

print(f"{numero_uno} + {numero_dos} = {suma}")
print(f"{numero_uno} * {numero_dos} = {multiplicacion}")
print(f"{numero_uno} / {numero_dos} = {division}")
print(f"{numero_uno} - {numero_dos} = {resta}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.


def pedir_altura_peso():
    while True:
        try:
            altura = float(input("Ingrese su altura, en metros: "))            
            peso = float(input("Ingrese su peso, en kg: "))
            if altura > 0 and peso > 0:
                return altura, peso
            else:
                print("Error. Debe ingresar un numero positivo")
        except ValueError:
            print("Error. Debe ingresar un valor numérico.")

def calcular_imc(altura, peso):
    imc=round(peso/(altura**2),2)
    return imc

def evaluar_tipo_de_imc(imc, altura):
    if imc >= 30:
        estado = "Obesidad"
        peso_maximo_sobrepeso = round(29.9*(altura**2),2)
        peso_maximo_normal = round(24.9*(altura**2),2)
    elif 25 <= imc < 30:
        estado = "Sobrepeso"
        peso_maximo_normal = round(24.9*(altura**2),2)
    elif 18.5 <= imc < 25:
        estado = "Normal"
    else:
        peso_minimo = round(18.5*(altura**2),2)
        estado = "Bajo peso"

    match estado:
        case "Bajo peso":
            print(f"Tu IMC es {imc}, que significa: {estado}. El peso mínimo, para tu altura, para que el IMC de 'normal' es de {peso_minimo} kg")
        case "Normal":
            print(f"Tu IMC es {imc}, que significa: {estado}. Estás dentro del peso normal para tu altura")
        case "Sobrepeso":
            print(f"Tu IMC es {imc}, que significa: {estado}. El peso máximo, para tu altura, para que el IMC de 'normal' es {peso_maximo_normal} kg")
        case "Obesidad":
            print(f"Tu IMC es {imc}, que significa: {estado}. El peso máximo, para tu altura, para llegar a 'Sobrepeso' es de {peso_maximo_sobrepeso} kgs y para llegar a 'normal' es de {peso_maximo_normal} kg")


# Programa principal
altura, peso = pedir_altura_peso()
imc = calcular_imc(altura, peso)

print(f"Tu IMC es {imc}")
evaluar_tipo_de_imc(imc, altura)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def pedir_temp_celsius():
    while True:
        try:
            temp_c = float(input("Ingrese la temperatura en Celsius: "))
            return temp_c
        except ValueError:
            print("Error. Debe ingresar un valor numérico.")

def celsius_a_fahrenheit(celsius):
    temp_f = round((celsius * 1.8) + 32, 2)
    return temp_f

# Programa principal
temp_c = pedir_temp_celsius()
temp_f = celsius_a_fahrenheit(temp_c)

print(f"La temperatura {temp_c}ºC equivale a {temp_f}ºF")

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