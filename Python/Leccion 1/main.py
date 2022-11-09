"""
miVariable = 3
print(miVariable)
miVariable = "a"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 14
y = 4
z = x + y
print(id(x))
# las literales se escriben con los los ultimos 3 numeros x184
print(id(y))
print(id(z))

# Tipos int, float, string, bool

x = 10
print(x)
print(type(x))
x = 48.5
print(x)
print(type(x))
x = "messi"
print(x)
print(type(x))
x = True
print(x)
print(type(x))

# Manejo de cadenas (string)

miGrupoFavorito = "Messi:"
caracteristicas = "enanito y fachero"
print("Mi jugador favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "10"
numero2 = "30"
print(numero1 + numero2)

numero1 = "10"
numero2 = "30"
print(int(numero1) + int(numero2))

# tipos Booleans (bool)
miBoolean = 3 > 2
print(miBoolean)

if miBoolean:
    print("el resultado es: Verdadero")
else:
    print("el resultado es: falso")

# procesar entrada del usuario
# funcion input

resultado = input("digite un numero: ")  # regresa un dato tipo string
print(resultado)

# conversion de la entrada de datos
numero1 = int(input("escribe el primer numero: "))
numero2 = int(input("escribe el segundo numero: "))
resultado = numero1 + numero2
print("el resultado de la suma es: ", resultado)



operandoA = 8
operandoB = 6
suma = operandoB + operandoA
print("resultado de la suma: ", suma)
print(f'el resultado de la suma es: {suma}')

resta = operandoA - operandoB
print(f'el resultado de la resta es: {resta}')

multiplicacion = operandoA * operandoB
print(f'el resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'el resultado de la division es: {division}')
division = operandoA // operandoB
print(f'el resultado de la division (int) es: {division}')

modulo = operandoA % operandoB
print(f'el resultado del residuo es: {modulo}')

exponente = operandoA ** operandoB
print(f'el resultado del exponente es: {exponente}')

# se solicita calcular el area y perimetro de un rectangulo
alto = int(input("escribe el alto del rectangulo: "))
ancho = int(input("escribe el ancho del rectangulo: "))
area = alto * ancho
perimetro = (alto + ancho) * 2
print(f'el area es: {area}')
print(f'el perimetro es: {perimetro}')


# operadores de asignacion y comparacion

miVariable3 = 7
print(miVariable3)

# operadores de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)

miVariable3 *= 3
print(miVariable3)

miVariable3 /= 2
print(miVariable3)

# operadores de comparacion

d = 4
b = 2
resultado = (d == b)
print(resultado)

# operador diferente

resultado = d != b
print(resultado)

# operador mayor que
resultado = d > b
print(resultado)

# operador menor que
resultado = d < b
print(resultado)

# operador mayor o igual
resultado = d >= b
print(resultado)

# operador menor o igual
resultado = d <= b
print(resultado)

# EJERCICIO NUMBER ONE

a = int(input("digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
    print(f"el valor de su numero es: {a} PAR")
else:
    print(f"el valor de su numero es: {a} IMPAR")


# exercise number two

b = int(input("Digite su edad: "))
if b >= 18:
    print(f"Edad {b}: Mayor de edad")
else:
    print(f"Edad {b}: Menor de edad")

# edadAdulto = 18
# edadPersona = int(input("Digite su edad: "))
# if edadPersona >= edadAdulto:
#    print(f"Su edad es: {edadPersona} es mayor de edad")
# else:
#    print(f"Su edad es: {edadPersona} es menor de edad")


# Operadores logicos and - or - not

a = False
b = False
resultado = a and b
print(resultado)

# or
resultado = a or b
print(resultado)

# not
resultado = not a
print(resultado)

# EJERCICIO: Valor dentro de un rango
valor = int(input("digite un numero del 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
rango = (valor >= valorMinimo and valor <= valorMaximo)
if rango:
    print(f"el valor {valor} esta dentro del rango.")
else:
    print(f"el valor {valor} esta fuera de rango")

# EJERCICIO: operadores or y not
vacaciones = False
diaDescanso = True
if not (vacaciones or diaDescanso):
    print("tiene trabajo que hacer")
else:
    print("puede asistir al juego")


# EJERCICIO: Rango entre 20 y 30 años
edad = int(input("Ingrese su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)

if (20 <= edad < 30) or (30 <= edad < 40):# sintaxis simplificada del operador and
    print(f"la edad esta dentro del rango de los (20\'0) a(30\'0) años")

# if veinte:
#    print(f"la edad {edad} esta dentro del rango de los (20\'0) años")
# elif treinta:
#    print(f"la edad {edad} esta dentro del rango de los (30\'0) años")
else:
    print(f"la edad esta fuera del rango de los (20\'0) a(30\'0) años")

# EJERCICIO: El mayor de dos numeros

numero1 = int(input("Digite el valor para el numero 1: "))
numero2 = int(input("Digite el valor para el numero 2: "))

if numero1 > numero2:
    print(f"el numero1: {numero1} es mayor")
elif numero1 == numero2:
    print(f"Los numeros digitados son iguales")
else:
    print(f"el numero2: {numero2} es mayor")

# EJERCICIO: Tienda de libros
print("Ingrese los datos del libro ")
nombreLibro = input("Digite el nombre del libro: ")
idLibro = int(input("Digite el id del libro: "))
precio = float(input("Digite el precio del libro:"))
envio = input("Indicar si el envío es gratuito (True/False): ")
if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = "el valor digitado es incorrecto, debe escribir True/False"
print(f'''
        Nombre: {nombreLibro}
        id: {idLibro}
        Precio: {precio}
        Envio gratuito: {envio}
"""

