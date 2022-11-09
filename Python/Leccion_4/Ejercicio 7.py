# operaciones en conjunto con listas
# escriba un programa que tenga 2 listas y que a continuacion 
# cree las siguientes listas (en las que no deben haber repeticion)

# 1 lista de palabras que aparecen en las listas
# 2 lista de palabars que aparecen en la primera lista solamente
# 3 lista de palabras que aparecen en la segunda lista solamente
# 4 lista de palabras que aparecen en ambas listas

lista1 = [1, 3, 2, 4, 6, 5, 5, 4, 2]

lista2 = [5, 5, 7, 6, 6, 7, 8]
print("")

# eliminamos los elementos repetidos de cada lista

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = list(conjunto1 | conjunto2) # unimos ambos conjuntos
solo1 = list(conjunto1 - conjunto2) # solo muestra el conjunto1
solo2 = list(conjunto2 - conjunto1) # solo muestra el conjunto2
coinciden = list(conjunto1 & conjunto2) # mostramos los elementos que coinciden en ambas listas
solo2.sort()

print(f"La lista de palabras que aparecen en las listas son: {union}")
print(f"La lista de palabras que aparecen en al primera lista solamente son: {solo1}")
print(f"La lista de palabras que aparecen en la segunda lista solamente son: {solo2}")
print(f"La lista de palabras que aparecen en ambas listas son: {coinciden}")