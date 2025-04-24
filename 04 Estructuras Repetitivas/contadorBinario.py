import time

########## ALERNATIVA 1 ###########

print("Contador binario del 0 al 15:")
for numero in range(16): # range(16) va del 0 al 15 inclusive
    n = numero
    restos = [] # Lista para guardar los restos de la division por 2

    # Si el numero es 0, su binario es directamente 0000
    if numero == 0:
        restos =[0]
    else:
        while n > 0:
            resto = n % 2  # Calculamos el resto de la division por 2
            restos.insert(0, resto) # Lo agregamos al principio de la lista
            n = n // 2 # Division entera por 2

    # Aseguramos que tenga 4 bits rellenando con ceros a la izquierda
    while len(restos) < 4:
        restos.insert(0, 0)
    binario = ''.join(str(bit) for bit in restos) # Convertimos la lista a string
    # print(restos)

    print(f"{numero} en binario es: {binario}")
    time.sleep(1)  # Esperamos 1 segundo antes de mostrar el siguiente numero


########## ALTERNATIVA 2 ###############

# Mostramos un mensaje inicial
print("Contador binario del 0 al 15:")

# Usamos un bucle para contar del 0 al 15
for numero in range(16): # range(16) va del 0 al 15 inclusive
    binario = format(numero, '04b') # Convertimos el numero a binario de 4 cifras
    print(f"{numero} en binario es: {binario}")
    time.sleep(1) # Esperamos 1 segundo antes de mostrar el siguiente numero