# Insertar elementos y ordenarlos
# pedir numeros y meterlos en una lista, cuando el usuario introduzca un numnero 0 
# nuestro programa dejaria de insertar
# por ultimo, mostrar los numeros ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input("Digite un numero :"))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
        
lista.sort()
print(f"\n Lista ordenada: \n{lista}")