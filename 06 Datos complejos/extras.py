# 1) Creación y Manipulación

# Crea una lista de tus cinco frutas favoritas. 
# Luego utiliza append() para añadir una sexta fruta y remove() para eliminar la segunda fruta de la lista. 
# Imprime la lista resultante.

frutas = ["banana","manzana","pera","limon","naranja"]
frutas.append("Lima")
frutas.remove(frutas[1])

print(frutas)

# 2) Slicing Avanzado

# Dada la lista numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90], 
# utiliza slicing para obtener: los primeros tres elementos, los últimos dos elementos, 
# y los elementos en posiciones pares.

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
primeros_tres = numeros[:3]
ultimos_dos = numeros[-2:]
elementos_pares = numeros[::2]
print(primeros_tres)
print(ultimos_dos)
print(elementos_pares)

# 3) Conversión con split()

# Convierte la cadena "Python,Java,C++,JavaScript,PHP" en una lista de lenguajes de programación utilizando split(). 
# Luego añade "Ruby" a la lista e imprime los lenguajes por consola.

cadena = "Python,Java,C++,JavaScript,PHP"
lista_lenguajes = cadena.split(",")
print(lista_lenguajes)

# 4) Usando range()

# Genera una lista con los números impares del 1 al 20 utilizando range(). 
# Luego, crea otra lista que contenga sólo los números de la primera lista que son divisibles por 3.

lista_impares = list(range(1,21,2))

print(lista_impares)

divisibles_por_3 = []

for num in lista_impares:
    if num % 3 == 0:
        divisibles_por_3.append(num)

print(divisibles_por_3)