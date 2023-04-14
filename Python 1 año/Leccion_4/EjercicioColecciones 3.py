# Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte 

# Nombre: Gandal
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

print("Forma de hacerlo con diccionario")

señordelosanillos = {
   1: {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del norte"},
   2: {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"},
   3: {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo sindar"},}


señordelosanillos[4] = {"Nombre": "Frodo", "Clase": "Humano", "Raza": "Hobbit de la Comarca"},
señordelosanillos[5] = {"Nombre": "Gimli", "Clase": "Guerrero", "Raza": "Enano"},
señordelosanillos[6] = {"Nombre": "Saruman", "Clase": "Mago", "Raza": "Istar"},

for llave, valor in señordelosanillos.items():
    print(llave, valor)
    
    
    
    print("")
print("Otra forma de hacerlo con listas")
    
    
    
    
personajes = []

P1 = {"Nombre": "Aragon", "Clase": "Guerrero", "Raza": "Dúnadan del norte"}
personajes.append(P1)
P2 = {"Nombre": "Gandalf", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P2)
P3 = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo sindar"}
personajes.append(P3)


P4 = {"Nombre": "Frodo", "Clase": "Humano", "Raza": "Hobbit de la Comarca"}
personajes.append(P4)
P5 = {"Nombre": "Gimli", "Clase": "Guerrero", "Raza": "Enano"}
personajes.append(P5)
P6 = {"Nombre": "Saruman", "Clase": "Mago", "Raza": "Istar"}
personajes.append(P6)
print(personajes[0:1])
print(personajes[1:2])
print(personajes[2:3])
print(personajes[3:4])
print(personajes[4:5])
print(personajes[5:6])
