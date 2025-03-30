# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
 
print("Hola mundo!")
 
# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
 
usuario=input("Ingrese su usuario: ")
print(f"Hola {usuario}")
 
#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
residencia=input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
import math

radio=float(input("Ingrese el radio del circulo: "))
area=round((math.pi*radio**2), 2)
perimetro=round((2*math.pi*radio), 2)
print(f"El area del circulo es {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos=int(input("Ingrese la cantidad de segundos: "))
horas=round(segundos/3600,2)
if horas==1:
    print(f"{horas} hora")
else:
    print(f"{horas} horas")
# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
numero=int(input("Ingrese un número: "))
for i in range(1,11):
    print(f"{numero} x {i} = {i*numero}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1=int(input("Ingrese el primer número entero (Distinto de 0): "))
if numero1 != 0:
    numero2=int(input("Ingrese el segundo número entero (Distinto de 0): "))
    if numero2 != 0:
        suma=numero1+numero2
        division=numero1/numero2
        multiplicacion=numero1*numero2
        resta=numero1-numero2
        print(f"{numero1} + {numero2} = {suma}")
        print(f"{numero1} / {numero2} = {division}")
        print(f"{numero1} * {numero2} = {multiplicacion}")
        print(f"{numero1} - {numero2} = {resta}")
    else:
        print(f"El segundo numero ingresado es 0. Por favor, ingresa números enteros distintos de 0")
else:
    print(f"El numero ingresado es 0. Por favor, ingresa números enteros distintos de 0")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
# 𝐼𝑀𝐶 = 𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)2
altura=float(input("Ingrese su altura, en metros: "))
peso=float(input("Ingrese su peso, en kg: "))
imc=round(peso/(altura**2),2)
print(f"Su IMC es de {imc}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# Celsius = (Fahrenheit - 32) * 5/9

temp_c=float(input("Ingrese la temperatura en ºC: "))
temp_f=round((temp_c*(9/5)+32),2)
print(f"{temp_c} ºC equivale a {temp_f} ºF")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
numero3=int(input("Ingrese el tercer número: "))
promedio=round((numero1+numero2+numero3)/3 ,2)
print(f"El promedio es: {promedio}")
