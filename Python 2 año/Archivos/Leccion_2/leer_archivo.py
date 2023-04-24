# cuando el archivo (prueba) que queremos mostrar no esta en la misma ruta
# que la carpeta (leccion2) se deve pner la ruta
archivo = open('prueba.txt', 'r', encoding='utf8') 
# print(archivo.read())
# print(archivo.read(5)) #te lee loas primeras 5 letras del texto
# print(archivo.read(10)) #Continuamos desde la linea anterior
# print(archivo.readline()) # Te lee solo la primera linia 
# print(archivo.readline()) # Te lee la seguna linia

# vamos a iterar el archivo, cada unas de las lineas
#for linea in archivo:
    # print(linea) # se actualiza mediante agregemos informacion al archivo
    # print(archivo.readlines()) # nos muentra todo como una lista, no hace fslta que estre dentro del for, igual se muestra
    # print(archivo.readlines()[1]) # te muestra el primer parrafo como lista

# Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close() # cramo el primer archivo
archivo2.close() # cerramos el segundo archivo

print('Se ah terminado el proceso de leer y copiar archivos')