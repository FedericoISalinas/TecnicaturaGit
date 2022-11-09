# En esta clase veremos la sentancia if/else

condicion = 10
if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condicion Falsa')
else:
    print('Condicion sin especificar')

# combercon de numero a texto
num = int(input('Diguite un numero en e rango del 1 al 3: '))
numTexto = ''
if num == 1:
    numTexto = 'Número uno'
elif num == 2:
    numTecto = 'Número dos'
elif num == 3:
    numTexto = 'Número tres'
else:
    numTexto = 'Has ingresado un número fuera de rango'
print(f'El número ingresado es: {num} - {numTexto}')

condicion = True
if condicion:
    print('Condicion Verdadera')
else:
    print('Condicion Falsa')

print('Condicion Verdadera') if condicion else print('Condicion Falsa')