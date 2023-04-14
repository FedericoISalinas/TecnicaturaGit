
#Eliminar duplicados dentro de una lista

lista = [1,2,2,"Fede","Fede",1,2,1,3,4,6,"Mesa",5]
conjunto = set(lista) # convertimos la lista a un conjunto de tipo set
lista = list(conjunto) # convertimos el conjunto a una lista
print(lista)

# simplificado

lista = list(set(lista)) # se puede pasar de lista a conjunto, a su vez a lista nuevamente