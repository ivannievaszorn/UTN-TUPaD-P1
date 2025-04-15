# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_a_invertir = int(input("Ingrese el numero a invertir: "))

numero_invertido = 0

while numero_a_invertir > 0:
    # Almacenamos el ultimo digito en la variable
    ultimo_digito = numero_a_invertir % 10 
    # Agregamos el ultimo digito al numero invertido
    numero_invertido = numero_invertido * 10 + ultimo_digito
    # Eliminamos el ultimo digito
    numero_a_invertir = numero_a_invertir // 10

print(f"El numero {numero_a_invertir} invertido es {numero_invertido}")
