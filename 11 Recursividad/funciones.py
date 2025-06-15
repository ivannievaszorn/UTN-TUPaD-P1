def numero_entero_positivo(mensaje):
    while True:
        valor_ingresado = input(mensaje)
        try:
            numero_valido = int(valor_ingresado)
            if numero_valido > 0:
                return numero_valido
            else:
                print("Error. Ingresá un valor positivo")
        except ValueError:
            try:
                # ¿Es float pero no entero?
                float(valor_ingresado)
                print("Ingresaste un número con decimales. Solo se permiten enteros.")
            except ValueError:
                print("Error. Ingresar solo números enteros, sin letras ni símbolos.")

def es_numero(mensaje):
    while True:
        valor_ingresado = input(mensaje)
        try:
            numero_valido = int(valor_ingresado)
            return numero_valido
        except ValueError:
            try:
                # ¿Es float pero no entero?
                float(valor_ingresado)
                print("Ingresaste un número con decimales. Solo se permiten enteros.")
            except ValueError:
                print("Error. Ingresar solo números enteros, sin letras ni símbolos.")

def validar_digito(mensaje):
    while True:
        valor_ingresado = input(mensaje)
        try:
            numero_valido = int(valor_ingresado)
            if 0 <= numero_valido <= 9:
                return numero_valido
            else:
                print("Error. Ingresá un valor positivo")
        except ValueError:
            try:
                # ¿Es float pero no entero?
                float(valor_ingresado)
                print("Ingresaste un número con decimales. Solo se permiten enteros.")
            except ValueError:
                print("Error. Ingresar solo números enteros, sin letras ni símbolos.")