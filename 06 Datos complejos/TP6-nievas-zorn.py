# Actividades 

# 1) Dado el diccionario precios_frutas: 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300 

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800 

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios. 

listado_frutas = list(precios_frutas.keys())
print(listado_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe. Ejemplo:

contactos = {}
seguir = True

def pedir_nombre():
    while True:
        nombre = input("Ingresá el nombre del contacto (o 0 para cancelar): ")
        if nombre == "0":
            return nombre 
        if nombre.isalpha():
            return nombre
        else:
            print("Error. Solo podés ingresar letras. Intentá de nuevo.")

def pedir_numero():
    while True:
        numero = input("Ingresá el número (exactamente 10 dígitos, sin espacios): ")
        if numero.isdigit():
            if len(numero) == 10:
                return numero
            else:
                print("El número debe tener exactamente 10 dígitos.")
        else:
            print("Solo se permiten números enteros, sin letras ni símbolos.")

while seguir:
    print("\nAgenda telefónica")
    print("1. Guardar contacto")
    print("2. Consultar contacto")
    print("3. Salir")

    opcion = input("Elige una opción (1-3): ")

    match opcion:
        case "1":
            if len(contactos) < 5:
                nombre = pedir_nombre()
                if nombre == "0":
                    print("Carga cancelada.")
                numero = pedir_numero()
                contactos[nombre] = numero
                print("Contacto guardado.")
            else:
                print("Agenda llena. No se pueden agregar más contactos.")
        case "2":
            nombre = pedir_nombre()
            if nombre == "0":
                print("Consulta cancelada.")
            else:
                if nombre in contactos:
                    print(f"El número de {nombre} es {contactos[nombre]}")
                else:
                    print(f"No se encontró el contacto '{nombre}' en la agenda.")
        case "3":
            print("¡Hasta luego!")
            seguir = False
        case _:
            print("Opción inválida. Elegí 1, 2 o 3.")

# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra. Ejemplo:

from collections import Counter

frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

repeticiones = Counter(palabras)
print("Recuento: ",dict(repeticiones))


# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. Ejemplo:

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")

    notas_str = input(f"Ingresá las 3 notas de {nombre}, separadas por espacio: ")

    notas = tuple(int(nota) for nota in notas_str.split())

    alumnos[nombre] = notas


for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 


parcial1 = {"Ana", "Bruno", "Carlos", "Delfina", "Emilia"}
parcial2 = {"Delfina", "Emilia", "Fabio", "Gabriela"}

ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe. 

stock = {
    "leche": 12,
    "pan": 7,
    "queso": 5,
    "manteca": 3
}

producto = input("Ingresá el nombre del producto para consultar o agregar stock: ").lower()

if producto in stock:
    print(f"El stock de {producto} es {stock[producto]}")
    agregar = input("¿Querés agregar unidades? (s/n): ").lower()
    if agregar == "s":
        try:
            unidades = int(input("¿Cuántas unidades vas a agregar?: "))
            if unidades > 0:
                stock[producto] += unidades
                print(f"Nuevo stock de {producto}: {stock[producto]}")
            else:
                print("Debés ingresar un número positivo.")
        except ValueError:
            print("Error: ingresá solo números enteros.")
else:
    print(f"El producto '{producto}' no está registrado.")
    agregar_nuevo = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
    if agregar_nuevo == "s":
        try:
            nuevo_stock = int(input("¿Con cuántas unidades lo cargás?: "))
            if nuevo_stock > 0:
                stock[producto] = nuevo_stock
                print(f"Producto '{producto}' agregado con stock {nuevo_stock}.")
            else:
                print("Debés ingresar un número positivo.")
        except ValueError:
            print("Error: ingresá solo números enteros.")

# Podés mostrar el stock actualizado si querés:
print("\nStock actual:", stock)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
# Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "09:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "19:00"): "Cine con amigos"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato 00:00): ")

consulta = (dia, hora)

if consulta in agenda:
    print(f"En {dia} a las {hora} tenés: {agenda[consulta]}")
else:
    print(f"No hay actividad agendada para {dia} a las {hora}.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores. Ejemplo:

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario original (país -> capital):")
print(paises)
print("\nDiccionario invertido (capital -> país):")
print(capitales)