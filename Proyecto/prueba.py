# Establecemos una conexion con la base de datos PostreSQL
import psycopg2

# Importamos la funcion conbinations del modulo itertools para generar todas las combinaciones posibels
from itertools import combinations

#Creamos la variable separador para imprimir una linea separadora en el programa
separador = "-" * 40

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

# Crear una conexión a la base de datos con la biblioteca psycop2 proporcionando los datos necesarios
try:
    conn = psycopg2.connect(
        host="localhost",
        database="prueba",
        user="postgres",
        password="admin"
    )
    print("Conexion exitosa")
    print(separador)
except Exception as ex:
    print(ex)

# Crear una tabla "usuarios" para almacenar los nombres de los usuarios y contraseñas
conn.cursor().execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre TEXT,
        contraseña TEXT
    )
    """
)
conn.commit()

# Con esta funcion solicitamos al usuario que ingrese nombre y contraseña
def registrar_usuario():
    nombre = input("Digite su nombre: ")
    contraseña = input("Digite su contraseña: ")

    # Insertar los datos del usuario en la base de datos
    conn.cursor().execute(
        "INSERT INTO usuarios VALUES (%s, %s)",
        (nombre, contraseña)
    )
    conn.commit()
    print("Usuario registrado exitosamente.")
    print(separador)

# Con esta funcion solicitamos al usuario que ingrese el nombre y contraseña previos
def inicio_usuario():
    while True:
        nombre = input("Digite su nombre: ")
        contraseña = input("Digite su contraseña: ")
        
        # Se verifica que los datos ingresados coincidan con los registros almacenados en la tabla "usuarios"
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s",
            (nombre, contraseña)
        )
        result = cursor.fetchone()

        if result is not None:
            print("Inicio de sesión exitoso")
            print("")
            return True  # Retorna True si el inicio de sesión es exitoso

        print("Nombre de usuario y/o contraseña incorrectos. Por favor, inténtelo nuevamente.")
        print(separador)
      

# Esta funcion solicita al usuario que ingrese el nombre y el consumo de la placa de video, y se agrega al diccionario "placas_de_video"
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

# Esta funcion solicita al usuario que ingrese el nombre de una placa de video que desea eliminar del diccionario
def eliminar_placa_de_video(placas_de_video):
    nombre = input("Ingrese el nombre de la placa de video: ")
    del placas_de_video[nombre]
    print("Placa de video eliminada")
    print("")
   
# Esta funcion muestra los nombres de todas las placas de video almacenadas en el diccionario
def mostrar_placas_de_video(placas_de_video):
    for nombre, watts in placas_de_video.items():
        print(separador)
        print(f"Has elegido {nombre} como placa de video")
    print("")
    
# Esta funcion muestra el consumo de cada placa de video almacenada en el diccionario
def mostrar_consumo_placas_de_video(placas_de_video):
    for nombre, watts in placas_de_video.items():
        print(separador)
        print(f"El consumo de {nombre} es de {watts} watts")
        print("")
    
# Esta funcion muestra el consumo total de todas las placas de video
def mostrar_consumo_total_placas_de_video(placas_de_video):
    total = 0
    for nombre, watts in placas_de_video.items():
        total += watts
    print(separador)
    print(f"Consumo total: {total} watts")
    print("")
    
# Esta funcion genera todas las combinaciones posibles de valores dentro de una lista y retorna una lista con las que cumplan el requisito minimo    
def generar_combinaciones(valores, objetivo):
    combinaciones = []
    for r in range(1, len(valores) + 1):
        for comb in combinations(valores, r):
            if sum(comb) >= objetivo:
                combinaciones.append(comb)
    return combinaciones

# Encuentra la combinacion mas adecuada de paneles solares para cubrir el consumo total de las placas de video
def panel_mas_adecuado(placas_de_video):
    total = sum(placas_de_video.values())  # Consumo total en watts de las placas de video
    combinaciones = generar_combinaciones(paneles.values(), total)

    if not combinaciones:
        print("No se encontraron paneles solares que cubran el consumo solicitado.")
        return

    tolerancia = 200  # Tolerancia en watts

    min_paneles = float('inf')
    mejor_combinacion = None

    for combinacion in combinaciones:
        suma_combinacion = sum(combinacion)
        if suma_combinacion >= total and suma_combinacion <= total + tolerancia:
            if len(combinacion) < min_paneles:
                min_paneles = len(combinacion)
                mejor_combinacion = combinacion

    if mejor_combinacion is None:
        print("No se encontró una combinación de paneles solares dentro de la tolerancia establecida.")
        return

    print(f"Necesitarás al menos {min_paneles} paneles solares para el consumo total de las placas de video.")
    print("El panel recomendado es:")

    paneles_recomendados = [nombre for nombre, watts in paneles.items() if watts in mejor_combinacion]
    print(f"{', '.join(paneles_recomendados)}. Estos {len(mejor_combinacion)} paneles te cubrirán {sum(mejor_combinacion)} watts.")

# Muestra diferentes opciones del menu
def mostrar_menu():
    print(separador)
    print("1. Agregar placa de video")
    print("2. Eliminar placa de video")
    print("3. Mostrar las placas de video")
    print("4. Mostrar el consumo de cada placa de video")
    print("5. Mostrar el consumo total")
    print("6. Paneles solares mas adecuados para las placas de video")
    print("7. Salir")
    print(separador)
    print("")

# Se encarga de ejecutar el menu principal del programa, podemos seleccionar diferentes opciones
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

    # Cerrar la conexión a la base de datos antes de finalizar el programa
    conn.close()
    print(separador)
    print("Programa finalizado.")
    print(separador)


# Llamamos a la función para ejecutar el menú
registrar_usuario()
inicio_usuario()
ejecutar_menu()
