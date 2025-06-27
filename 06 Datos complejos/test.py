

# Diccionario original: país -> capital
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}

# Creamos un nuevo diccionario: capital -> país
capitales = {}

# Recorremos el original y agregamos el par invertido
for pais, capital in paises.items():
    capitales[capital] = pais

print("Diccionario original (país -> capital):")
print(paises)
print("\nDiccionario invertido (capital -> país):")
print(capitales)
