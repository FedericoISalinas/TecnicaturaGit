import math # importamos la clase math para hacer uso de la funcion raiz cuadrada
# Dada la siguiente tupla

tupla = (13, 1, 8, 3, 2, 5, 8) 

# crear una lista que solo incluya los numeros menores a 5 
# e imprima por consola [1, 3, 2]

lista = []

# filtramos los elementos menores a 5 de la tupla

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)


# Ejercicio de matematicas
# Raiz cuadrada de un numero positivo

numero = int(input("Digite un numero positivo "))

while numero < 0:
    print("Error, deberia ser un numero positivo")
    numero = int(input("Digite un numero positivo"))
print(f"\nSu raiz cuadrada es : {math.sqrt(numero):.2f}")