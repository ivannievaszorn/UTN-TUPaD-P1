# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")    


# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
# Niño/a: menor de 12 años. 
# Adolescente: mayor o igual que 12 años y menor que 18 años. 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# Adulto/a: mayor o igual que 30 años. 

edadUsuario=int(input("Ingrese su edad: "))
if edadUsuario < 12:
    print("Niño/a")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("Adolescente")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

password = input("Ingrese contraseña de entre 8 y 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete: https://docs.python.org/es/3.8/library/statistics.html. 
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una distribución normal 
# a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana # y, a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: # cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

# 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese la frase o palabra: ")
ultimo_caracter=frase[-1]
# En la validación podría haber manejado exclusivamente minusculas usando .lower() pero prefiero que muestre la vocal tal cual la ingresó el usuario.
if ultimo_caracter in ("a", "e", "i", "o", "u","A", "E", "I", "O", "U"):
    print(ultimo_caracter)
else:
    print(frase)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=input("Ingrese su nombre: ")
opcion=int(input("Ingrese un 1 si deseas su nombre en mayusculas, 2 en minusculas, y 3 con la primera letra mayuscula: "))

match opcion:
    case 1:
        print(nombre.upper())
    case 2:
        print(nombre.lower())
    case 3:
        print(nombre.title())

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter # e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremono: "))

if 3 > magnitud:
    print("Muy leve")
elif 3 <= magnitud < 4:
    print("Leve")
elif 4 <= magnitud < 5:
    print("Moderado")
elif 5 <= magnitud < 6:
    print("Fuerte")
elif 6 <= magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo")


# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

hemisferio = input("Ingrese el hemisferio (N o S): ").strip().lower()
if hemisferio in ("norte", "n"):
    hemisferio = "n"
elif hemisferio in ("sur", "s"):
    hemisferio = "s"
else:
    print("Hemisferio inválido.")

mes_input=input("Ingrese el mes del año: ").strip().lower()
if mes_input.isdigit():
    mes = int(mes_input)
else:
    mes = meses.get(mes_input)

if mes is None or not (1 <= mes <= 12):
    print("Mes invalido")
    exit()

dia=int(input("Ingrese el día del mes: "))
estacion = ""

if mes in (1,2):
    if hemisferio == "s":
        estacion = "Verano"
    else:
        estacion= "Invierno"

elif mes == 3:
    if dia <= 20:
        if hemisferio == "s":
            estacion = "Verano"
        else:
            estacion = "Invierno"
    else:
        if hemisferio == "s":
            estacion = "Otoño"
        else:
            estacion = "Primavera"

elif mes == (4, 5):
    if hemisferio == "s":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

elif mes == 6:
    if dia <=20:
        if hemisferio == "s":
            estacion = "Otoño"
        else:
            estacion = "Primavera"
    else:
        if hemisferio == "s":
            estacion = "Invierno"
        else:
            estacion = "Verano"

elif mes == (7,8):
    if hemisferio == "s":
        estacion = "Invierno"
    else:
        estacion = "Verano"

elif mes == 9:
    if dia <=20:
        if hemisferio == "s":
            estacion = "Invierno"
        else:
            estacion = "Verano"
    else:
        if hemisferio == "s":
            estacion = "Primavera"
        else:
            estacion = "Otoño"

elif mes == (10,11):
    if hemisferio == "s":
        estacion = "Primavera"
    else:
        estacion = "Otoño"

elif mes == 12:
    if dia >= 21:
        if hemisferio == "s":
            estacion = "Verano"
        else:
            estacion= "Invierno"
    else:
        if hemisferio == "s":
            estacion = "Primavera"
        else:
            estacion = "Otoño"

print(estacion)