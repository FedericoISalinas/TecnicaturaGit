# COLECCIONES EN PYTHON, en otros programas se las concoe como vectores o arreglos
# lista = Ariel, Liliana, Natalia, Osvaldo
# Dentro de la lista tengo 4 elementos, empiezo a contar desde el cero
nombres = ["Naty","Osvaldo","Lily","Ariel"] #naty = 0  osvaldo = 1   lily = 2   ariel = 3
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1]) # Muestra el ultimo elemento de la lista, la recorre inversamente
print(nombres[-2]) # Muestra el penultimo elemento de la lista, la recorre inversamente

#recuperar un rango de la lista
print(nombres[0:2]) # te va a mostrar desde el numero 0 hasta el numero 2 sin incluirlo

#vamos a ir del inicio de la lista al indice
print(nombres[ :3]) # si en la primera posicion dejamos un espacio nos muestra las 3 primeras posiciones

#desde el indice indicado hasta el final
print(nombres[1: ]) # indico que quiero que me muestre desde el indice 1 hasta el final de la lista

#Modificamos un valor de la lista
nombres[2] = "Liliana"
nombres[0] = "Natalia"
print(nombres)

#Iterar una lista
for nombre in nombres: #nombre es singular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")

#Preguntamos cuantos elementos tiene la lista
    
print(len(nombres)) 

# Agregamos un elemento
nombres.append("Marcelo") 
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4, 5])
nombres.append(7)

print(nombres)


#Insertamos un nuevo elemento en el lugar de indice que nosotros queramos
nombres.insert(0, "Alberto") #Indicamos con el entero en que indice queremos agregar el elemento
print(nombres)
nombres.insert(3, "Debora")
print(nombres)

#eliminamos un elemento de la lista
nombres.remove("Alberto")
print(nombres)

#eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)

#eliminar un indice especifico
# del nombres[2] # del significa delete(eliminar)
print(nombres)

#eliminar, borrar o limpiar todos los elementos
#nombres.clear()
print(nombres)

#eliminar la lista
# del nombres
# print(nombres)
# como ya eliminamos la lista anteriormente nos saldria error 

#definimos una tupla
cocina = ("cuchara","cuchillo","tenedor")
print(len(cocina))
print(cocina)

#acceder a un elemento, para esto utilizamos corchetes no parentesis

print(cocina[0])

#mostrar de manera inversa
print(cocina[-1])
print(cocina[-2])

#acceder a un rango
print(cocina[0:2])

#ejemplo
verduras = ("papa",) # una tupla necesita aunque sea un elemento con ,
print(verduras)
#de lo contrario solo seria un tipo string cadena

#recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=" ") # end=" " hace que se escriba todo en una sola linea

# cocina[0] = "plato"
# print(cocina) #me saldria un error ya que no puedo añadir un elemento a una tupla

cocinaLista= list(cocina) # para modificar una tupla necesitamos cambiar la tupla a una lista
cocinaLista [0] = "plato"
cocina = tuple(cocinaLista) # luego volvemos a cambiarla para seguir trabajando con la tupla
print("\n", cocina)

#del cocina     # puedo eliminar la tupla
#print(cocina)   


# Un elemento de tipo set es una coleccion y sin indices

# Tipo set

planetas = {"Marte", "Jupiter","Venus"}
print(len(planetas)) # Usamos la funcion len = length que significa largo

# Revisar si un elemento existe dentro de un set
print("Marte" in planetas)
print("Marte" not in planetas)

# Agregar un elemento
planetas.add("Tierra") # add es una funcion
print(planetas)

# Eliminar elementos, puede ocasionar un error si el elemento no existe
planetas.remove("Venus") # esta funcion ante un mal ingreso de la funcion peude ocasionar error
print(planetas)

planetas.discard("Tierra") # esta funcion no puede presentar ningun tipo de error si ingresamos mal un elemento
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
## del planetas
## print(planetas) # al eliminar nos muestra error

# Diccionario

# un diccionario esta compuesto por dos elementos
# Una la llave y un valor
# dict(key, value)

diccionario = {
    "IDE" : "Integrated Development Environment",
    "POO" : "Programacion Orientada a Objetos",
    "SABD" : "Sistema de Administracion de Base de Datos"


}
print(diccionario)
#Verificar la cantidad de elementos en un diccionario
print(len(diccionario))

#Acceder a un diccionario con la llave (key)
print(diccionario["IDE"])

# Otra forma de recuperar un elemento
print(diccionario.get("POO"))

# Modificamos los elementos
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)

# Como recorrer los elementos
for termino in diccionario: # Recorremos mostrando solo las llaves
    print(termino)

for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Solo muestra las llaves 
    print(termino)

for valor in diccionario.values(): # Solo nos muestra las llaves
    print(valor)

# Comprobar la existencia de algun elemento
print("IDE" in diccionario)

# Agregar un elemento
diccionario["PK"] = "Primary key"
print(diccionario)

# Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un diccionario
del diccionario 

#Concatenamos listas

lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = [7, 8, 9, 1]
lista4 = lista1 + lista2 + lista3
print(lista4)

#Agregar elementos a una lista

lista4.extend([10, 11, 12, 1])
print(lista4)

# ver el numero de indice dentro de una lista
print(lista4.index(2)) 

# ver cuantos valores hay repetidos dentro de la lista
print(lista4.count(1))

# para poner una lista al reves
lista4.reverse()
print(lista4)

# para que una lista se multiplique repitiendo sus elementos
lista4 = lista4 * 2
print(lista4)

# metodos de ordenamiento
# forma ascendente
lista4.sort()
print(lista4)

# forma descendente
lista4.sort(reverse=True)
print(lista4)

#Repaso de tupla, que nos muestra
tupla = (4, "Hola", 6.78, [1, 2, 3], 4, "Hola")
print(tupla)

print(4 in tupla) # Accion booleana, su respuesta es booleana
# lo que podemos usar dentro de tuplas son : count, index, len
# se puede convertir de tupla a lista   

# Repaso de set o conjunto
# para defunir un conjunto
conjunto = set()
conjunto1 = {"bye", }
conjunto.add(7)
conjunto.add("Hola")
conjunto1.add("Hola")
print(conjunto)
print(conjunto1)

print(3 not in conjunto1) # preguntamos si el numero 3 NO esta en el conjunto1

#como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto) # nos devuelve un valor booleano

# operaciones en conjuntos
conjunto2 = conjunto | conjunto1 # la linea los une
print(conjunto2)

conjunto2 = conjunto1 & conjunto # & muestra que elemento tienen en comun los conjuntos 
print(conjunto2)

conjunto2 = conjunto1 - conjunto 
print(conjunto2)


conjunto2 = conjunto - conjunto1 # asigna el valor que esta en el conjunto y no en el conjunto1
print(conjunto2)

conjunto2 = conjunto1 ^ conjunto # asigna los valores que estan en los dos conjuntos pero no se comparten
print(conjunto2) 

# determinar si un conjunto esta dentro de otro conjunto 
conjunto2 = conjunto | conjunto1
print(conjunto1.issubset(conjunto2)) # Booleana, primer valor subconjunto, segundo conjunto
print(conjunto.issubset(conjunto2))
print(conjunto2.issubset(conjunto))
print(conjunto2.issuperset(conjunto)) # Booleana, primer valor conjunto, segundo subconjunto
print(conjunto.issuperset(conjunto2))

# Como saber si ambos conjuntos son disconexos, o si comparten elementos en comun

print(conjunto.isdisjoint((conjunto1))) # no hay cosas en comun

# convertir un conjunto totalmente en inmutable

conjunto = frozenset() #esto hace que el conjunto sea inmutable
print("")
# Repaso de ;

diccionarioNuevo = {"Azul": "Blue", "Rojo": "Red", "Verde" : "Green", "Amarillo" : "Yellow"}
print(diccionarioNuevo)
print("")
# como eliminar
del (diccionarioNuevo["Azul"])
print(diccionarioNuevo)
print("")

# los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {"Ariel" : {"edad" : 40, "Altura": 1.83}, "Osvaldo" : [45, 1.85], "Natalia" : [35, 167]}
print(diccionario2)
print("")

seleccionArgentina = {
    10 : {"Nombre": "Messi", "Edad" : 35, "Altura": 1.70, "Precio" : "50 millones", "Posicion" : "Extremo Derecho" },
    11 : {"Nombre": "Di Maria", "Edad" : 34, "Altura" : 1.80, "Precio" : "12 millones", "Posicion": "Extremo Derecho"},
    24 : {"Nombre": "Dybala", "Edad" : 28, "Altura" : 1.77, "Precio" : "35 millones", "Posicion": "Mediapunta"},
    19 : {"Nombre": "Otamendi", "Edad" : 34, "Altura" : 1.83, "Precio" : "5 millones", "Posicion": "Defensa central"},
    1 : {"Nombre": "Armani", "Edad" : 35, "Altura" : 1.89, "Precio" : "3,5 millones", "Posicion": "Portero"},}

print(seleccionArgentina)
print("")


seleccionArgentina["3"] = {"Nombre": "Tagliafico", "Edad" : 29, "Altura" : 1.72, "Precio" : "7 millones", "Posicion": "Defensa"},
seleccionArgentina["8"] = {"Nombre": "Acuña", "Edad" : 30, "Altura" : 1.72, "Precio" : "15 millones", "Posicion": "Defensa"},
seleccionArgentina["18"] = {"Nombre": "Salvio", "Edad" : 32, "Altura" : 1.71, "Precio" : "7 millones", "Posicion": "Centrocampista"},
seleccionArgentina["23"] = {"Nombre": "Martinez", "Edad" : 29, "Altura" : 1.95, "Precio" : "22 millones", "Posicion": "Portero"},
for llave, valor in seleccionArgentina.items():
    print(llave, valor)

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end= " ") # , end= " " sirve para concatenar lo de abajo con lo de arriba
print(len(seleccionArgentina))

print("")

# Metodo pilas usando listas

pila = [1, 2 ,3]

# agregar elementos a una pila por el final
pila.append(4)
pila.append(5)
print(pila)

# sacando elementos de una pila por el final
elementoBorrado = pila.pop() # quita el ultimo elemento y lo almacena guardandolo en la variable
print(f"sacamos el elemento {elementoBorrado} ")
print(f"la pila ahora quedo asi {pila}") # con la f podemos llamar a la funcion {pila}

print("")

# conlas con listas
# estructura de datos tipo fifo (first input / first output)
cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]
cola.append("Natalia")
cola.append("Jose")
print(cola)

#sacar elementos de la cola
seRetira = cola.pop(0)
print(f"Atendido {seRetira} ")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido {seRetira} ")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido {seRetira} ")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido {seRetira} ")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido {seRetira} ")
print(cola)

seRetira = cola.pop(0)
print(f"Atendido {seRetira} ")
print(cola)


