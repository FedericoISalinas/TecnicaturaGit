# Modificar los elementos de una lista
# Llenar una lista con numeros del 1 al 10, luego modificar los elementos de la lista
# multiplicandolos por un valor ingresado por el usuario

lista = list(range(1, 11))
print("Lista original")
for i in lista:
    print(i, end="-")
valor = int(input("\nDigite un valor a multiplicar: "))

# Multiplicamos todos los elementos de la lista

for indice, i in enumerate(lista): # enumerate me deja manipular los elementos que recorre en la lista, porque el i solamente lo muestra
    lista[indice] *= valor # el iterador solo recorre los indices, en esta linea se multiplica
print(f"\nLista final con los elementos multiplicados por el {valor}")
for i in lista:
    print(i, end="-")