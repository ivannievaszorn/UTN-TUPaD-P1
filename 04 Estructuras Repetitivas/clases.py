# cont = 0
# while cont < 5:
#     print(cont, "Debo aprender ciclos")
#     cont += 1

# print("//////////////")

# for x in range (5):
#     print(x, "Debo aprender ciclos")

# print("/////////////////////////////")

# cont = 1
# while cont < 5:
#     print(cont, "Debo aprender ciclos")
#     cont += 1

# print("//////////////")

# for x in range (1,5):
#     print(x, "Debo aprender ciclos")

# print("/////////////////////////////")


# for x in range (100,90,-1):
#     print(x)


# cant_numeros = 5
# sumatoria = 0

# for cont in range (1, cant_numeros + 1):
#     print("Ingrese número", cont)
#     num = int(input())
#     sumatoria += num

# print("La sumatoria de los numeros es", sumatoria)

# cont = 1
# while cont <= 5:
#     print(cont, "Debo aprender ciclos")
#     cont += 1

    
# cont = 5
# while cont >= 1:
#     print(cont, "Debo aprender ciclos")
#     cont -= 1

# sueldo_anual = 0
# cont_meses = 1
# mes_limite = 1

# print("Ingrese el último mes a incluir en el cálculo del ingreso anual (1-12): ")
# mes_limite = int(input())

# if mes_limite >0:
#     while cont_meses <= mes_limite:
#         print("Ingrese su sueldo para el mes nº", cont_meses)
#         sueldo_mensual = float(input())
#         if sueldo_mensual > 0:
#             sueldo_anual += sueldo_mensual
#             cont_meses += 1
#         else:
#             print("El sueldo no puede ser negativo, ingrese un valor positivo")

#     print("Tu sueldo anual es", sueldo_anual)
# else:
#     print("Ingrese un numero válido")

# for i in range(3):
#     print(i)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
suma = 0

if num1 == num2:
    print(f"No hay numeros entre {num1} y {num2}")
else:
    menor = min(num1,num2)
    mayor = max(num1,num2)

    for i in range (menor + 1, mayor):
        suma += i

print(f"La suma entre los numeros es {suma}")
