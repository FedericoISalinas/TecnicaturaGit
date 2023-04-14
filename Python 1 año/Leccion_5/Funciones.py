# Comenzamos con funciones
# mi funcion () # no se puede llamar antes de definir una funcion
# definimos una funcion

def mi_funcion(): #Para identificar a la funcion usamos ()
    print("Saludos a todos los alumnos de la tecnicatura")
    
mi_funcion() # estamos llamando a la funcion
mi_funcion() # se puede llamar a una funcion N cantidad de veces
print("")
print("")
# desempaquetando de listas 

def funcion(name, lastName):
    print(name+" "+lastName)
person = ["Ariel", "Bentancud"]
funcion(person[0], person[1]) # pasamos uno por uno los datos de la lista a la funcion
funcion(*person) # pasamos todos los datos a la misma vez
person2 = ("Osvaldo", "Giordanini") # desempaquetamos a traves de una tupla
funcion(*person2)
person3 = {"lastName": "Lucero", "name": "Natalia"}
funcion(**person3)

numeros = [1, 2, 3, 4, 5] # aun con la lista vacia se ejecuta el else
for n in numeros:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termina")
    print("")
    print("")
    
# lista de comprension
lista1 = ["Pablo", "Rodrigo", "Ariel", "Osvaldo", "Paolo"]
lista2 = [p for p in lista1 if p[0] == "P"] # regresa una nueva lista con la condicion 
print(lista2)

print("")

botellas = [{"Nombre": "Quilmes", "Pais": "Argentina"},
            {"Nombre": "Corona", "Pais": "Mexico"},
            {"Nombre": "Stella Artois", "Pais": "Belgica"}
]

Argentina = [b for b in botellas if b["Pais"] == "Argentina"] # Recorre el diccionario buscando la condicion y crea un diccionario nuevo
print(botellas)
print(Argentina)
print("")
print("")

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que ven a traves del canal de YouTube")
    print(f"Nombre :{name}, Apellido :{lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Bentancud")
mi_funcion2("Analia", "Pedrosa")

print("")
print("")

# La palabra return en funciones
# creamos una funcion para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
print(f"El resultado de la suma es: {resultado}")
print(f"El resultado de la suma es: {sumar(55, 45)}")

def sumar2(a=0, b=0): # le damos un valor por default
    return a + b
resultado2 = sumar2()
print(f"Resultado de la suma: {resultado2}")
print(f"Resultado de la suma: {sumar2(22,66)}")

print("")
print("")

# Argumentos, variable en funciones
def listarNombres(*nombres): # Se va a convertir en una tupla
    for n in nombres:
        print(n)
listarNombres("Lucas","Jose","Claudia","Rosa","Maria")
listarNombres("Marcos","Javier","Fede","Gonzalo","Marcela") # Vamos agregando los elementos como argumentos
print("")
def listarTerminos(**terminos): # lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():
        print(f"{llave} : {valor}")
print("")
        

listarTerminos(PK="Primary Key", IDE = "Integrated Develpment Enviroment")
listarTerminos(Jugador = "Messi")
print("")
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Fede","Gonza","Franco"]
desplegarNombres(nombres2)
print("--------------")
desplegarNombres("Alberto")
desplegarNombres((10, 11)) # () convertimos para que recorre una TUPLA, si es de un solo elemento no olvidar la ,
desplegarNombres([22, 15]) # [] convertimos para que recorra una LISTA
print("")

# Funciones recursivas
num = int(input("Digite un numero para calcular el factorial: "))

def factorial(num):
    if num == 0: # caso base
        return 1
    else:
        return num * factorial(num-1) # caso recursivo
resultado = factorial(num) # lo hacemos en codigo duro4
print(f"El factorial del numero 5 es: {resultado}")