
from manejoArchivos import manejoArchivos
# MANEJO DE CONTEXTO WITH : sintaxis simplicficada, abre y cierra el archivo
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
    # print(archivo.read())
    # no hace falta ni el try, ni el finally
    # en el contexto de with lo qur se ejecuta de manea automatica
    # Utiliza diferentes metodos: enter este es el que abre
    # Ahora el siguiente metodo es el que cierra: exit

with manejoArchivos() as archivos:
    print(archivos.read())  