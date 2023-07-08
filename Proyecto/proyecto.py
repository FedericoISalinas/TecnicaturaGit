
import psycopg2
import basededatos




separador = "-" * 40
#Hacer un programa que registre datos ingresados por el usuario de las placas de video.
#El programa debe tener un menu con las siguientes opciones:
#1. Agregar placa de video
#2. Eliminar placa de video
#3. Mostrar todas las placas de video
#4. Mostrar el consumo en watts de cada placa de video
#5. Mostrar el consumo en watts de todas las placas de video
#6. Paneles solares mas recomendados para el consumo en watts de las placas de video
#7. Salir


#Creamos un diccionario vacio para almacenar las placas de video
placas_de_video = {}
#Creamos un diccionario con los modelos y watts de cada panel solar
paneles = {
    "Sharp NU-U250S": 250, 
    "SunPower SPR-325W": 325,
    "SunPower SPR-345W": 345,
    "Futura Solar FS-360W": 360,
    "Meyer Burger MB-380W": 380,
    "LG NeON 2 400W": 400,
    "AUO SunForte 420W": 420,
    "PanaSonic HIT 440W": 440,
    "Jinko Solar JKM-460W": 460,
}

def agregar_placa_de_video(placas_de_video):
    nombre = input("Ingrese el nombre de la placa de video: ")
    print("")
    watts = int(input("Ingrese el consumo en watts de la placa de video: "))
    print("")
    placas_de_video[nombre] = watts
    print("Placa de video agregada")
    print("")
    nueva = input("¿Desea ingresar los datos de otra tarjeta gráfica? (s/n) ")
    if nueva.lower() == "s":
        agregar_placa_de_video(placas_de_video)
    else:
        mostrar_menu()


def eliminar_placa_de_video(placas_de_video):
    nombre = input("Ingrese el nombre de la placa de video: ")
    del placas_de_video[nombre]
    print("Placa de video eliminada")
    print("")
    mostrar_menu()


def mostrar_placas_de_video(placas_de_video):
    for nombre, watts in placas_de_video.items():
        print(f"{nombre}: {watts} watts")
    print("")
    mostrar_menu()


def mostrar_consumo_placas_de_video(placas_de_video):
    for nombre, watts in placas_de_video.items():
        print(f"{nombre}: {watts} watts")
        print("")
    mostrar_menu()


def mostrar_consumo_total_placas_de_video(placas_de_video):
    total = 0
    for nombre, watts in placas_de_video.items():
        total += watts
    print(f"Consumo total en watts: {total} watts")
    print("")
    mostrar_menu()


def panel_mas_adecuado(placas_de_video):
    total = 0
    for nombre, watts in placas_de_video.items():
        total += watts
    for nombre, watts in paneles.items():
        if watts >= total:
            print(f"Panel solar mas adecuado: {nombre}")
            print("")
            mostrar_menu()


def mostrar_menu():
    print(separador)
    print("1. Agregar placa de video")
    print("2. Eliminar placa de video")
    print("3. Mostrar todas las placas de video")
    print("4. Mostrar el consumo en watts de cada placa de video")
    print("5. Mostrar el consumo en watts de todas las placas de video")
    print("6. Paneles solares mas recomendados para el consumo en watts de las placas de video")
    print("7. Salir")
    print(separador)
    print("")


def ejecutar_menu():
    placas_de_video = {}

    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))
        print("")

        if opcion == 1:
            agregar_placa_de_video(placas_de_video)
        elif opcion == 2:
            eliminar_placa_de_video(placas_de_video)
        elif opcion == 3:
            mostrar_placas_de_video(placas_de_video)
        elif opcion == 4:
            mostrar_consumo_placas_de_video(placas_de_video)
        elif opcion == 5:
            mostrar_consumo_total_placas_de_video(placas_de_video)
        elif opcion == 6:
            panel_mas_adecuado(placas_de_video)
        elif opcion == 7:
            break

    # Cerrar la conexión a la base de datos
    basededatos.conn.close()
    print("Programa finalizado.")


# Llamamos a la función para ejecutar el menú
ejecutar_menu()