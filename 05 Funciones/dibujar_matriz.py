#Funciones

def leer_entero_validado(mensaje, min=float("-Inf"), max=float("Inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n

def leer_simbolo(mensaje):
    char = input(mensaje)
    while len(char) != 1:
        char = input("ERROR! Ingrese un único carácter: ")
    return char

def dibujar_linea(simbolo, cant_veces):
    linea = ""
    for i in range(cant_veces):
        linea += simbolo
    print(linea)

def dibujar_matriz(numero_filas, numero_columnas, simbolo):
    for i in range (numero_filas):
        dibujar_linea(simbolo, numero_columnas)

# Programa principal

alto = leer_entero_validado("Ingrese el alto: ", 1)
ancho = leer_entero_validado("Ingrese el ancho: ", 1)
simbolo_ingresado = leer_simbolo("Ingrese el carácter con el que desea dibujar la matriz: ")
dibujar_matriz(alto, ancho, simbolo_ingresado)