#Ejercicios
#Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
#Ejemplo de ejecucion: 0, 3, 6, 9

#Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimelos
#Ejemplo de ejercicion: 2, 3, 4, 5, 6

#Ejercicio 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de en 1 en 1 
#Ejemplo de ejecucion: 3, 5, 7, 9
print("Rango de numeros de 0 a 10 divisible entre 3")
for i in range(11):
    if i % 3 == 0:
        print(i)
print("")
print("Rango con valores 2 a 6")
rango = range(2, 7)
for i in rango:
    print(i)
print("")
print("Rango de 3 a 10 con incremento de 2 en 2")
for i in range (3, 11, 2):
    print(i)

#Ejercicio 4: dada la siguiente tupla
print("")

tupla = (13, 1, 8, 3, 2, 5, 8) # definimos la tupla

#Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 3, 2]
lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)

print(lista)
