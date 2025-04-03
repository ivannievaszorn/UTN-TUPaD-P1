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