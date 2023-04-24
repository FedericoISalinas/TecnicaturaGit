# 'utf8' : sirve para que nos muentre los acentos en el archivo txt
# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Programamos con diferentes tipos de archivos, ahora con txt. \n')
    archivo.write('Los acentos son importantes para las palabras. \n')
    archivo.write('como por ejemplo: accion, ejecucion y produccion. \n')
    archivo.write('La letra w significa write y es para escribir. \n')
    archivo.write('La lerea R significa read y es para leer. \n')
    archivo.write('La letra A significa append y es para cuando queremos anexar mas informacion. \n')
    archivo.write('La letra X sirve para crear un archivo. \n')
    archivo.write('La letra t significa text y es para espesificar el tipo de archivo. \n')
    archivo.write('La letra b sirve para crear un archivo de tipos binarios. \n')
    archivo.write('La letra w+ sirve para crear un escivir pero tambien para leer informacion. \n')
    archivo.write('La letra r+ sirve para crear un abrir, leer informacion. \n')
    archivo.write('Con esto terminamos.')

except Exception as e:
    print(e)
finally: # siempre se ejecuta
    archivo.close() #Con esto se debe cerrar el archivo
# archivo.write('Todo quedo perfecto') FUERA DEL PROGRAMA, ES UN ERROR