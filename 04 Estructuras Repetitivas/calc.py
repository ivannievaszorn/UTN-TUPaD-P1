suma = 0
multiplicacion = 0
division = 0
resta = 0

mensaje_menu = "Operaciones disponibles:\n1- Suma\n2- Resta\n3- Multiplicación\n4- División\n5- Salir"

print(mensaje_menu)
operacion = int(input("Seleccione una operación (1-5): "))

while operacion <1 or operacion >5:
    print("Error! Ingrese un numero entre 1 y 5: ")
    print(mensaje_menu)
    operacion = int(input("Seleccione una operación (1-5): "))

while operacion !=5:
    num1 = float(input("Ingrese un numero entero: "))
    num2 = float(input("Ingrese otro numero entero: "))
    match operacion:
        case 1:
            suma = num1 + num2
            print(suma)
        case 2:
            resta = num1 - num2
            print(resta)
        case 3:
            multiplicacion = num1 * num2
            print(multiplicacion)
        case 4:
            if num2 !=0:
                division = num1 / num2
                print(division)
            else:
                print("No se puede dividir por cero")
    operacion = int(input("Ingrese otra operación o presione 5 para salir: "))