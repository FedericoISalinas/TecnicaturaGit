import psycopg2
import itertools
separar = ("-" * 30)
# Crear una conexión a la base de datos
try:
    conn = psycopg2.connect(
        host="localhost",
        database="proyecto_tercer_semestre",
        user="postgres",
        password="admin"
    )
    print("Conexion exitosa")

except Exception as ex:
    print(ex)

# Crear una tabla para almacenar los usuarios
conn.cursor().execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre TEXT,
        contraseña TEXT
    )
    """
)
conn.commit()

# Crear una tabla para almacener los datos de las placas de video
conn.cursor().execute(
    """
    CREATE TABLE IF NOT EXISTS placas (
        nombre TEXT,
        watts INT
    )
    """
)
conn.commit()


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
    print(separar)
    
def iniciar_sesion():
    while True:
        nombre = input("Digite su nombre: ")
        contraseña = input("Digite su contraseña: ")

        # Verificar si el usuario y la contraseña coinciden en la base de datos
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s",
            (nombre, contraseña)
        )
        result = cursor.fetchone()

        if result is not None:
            print("Inicio de sesión exitoso")
            print(separar)
            ejecutar_menu()
            break
        else:
            print("Nombre de usuario y/o contraseña incorrectos. Por favor, inténtelo nuevamente.")

## PARTE 2
# Creamos un diccionario vacio para almacenar las placas de video
placas_de_video = {}

# Creamos un diccionario con los modelos y watts de cada panel solar
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

# Creamos una funcion para agregar una placa de video
def agregar_placa_de_video(placas_de_video):
    nombre = input("Ingrese el nombre de la placa de video: ")
    watts = int(input("Ingrese el consumo en watts de la placa de video: "))
    placas_de_video[nombre] = watts
    print("Placa de video agregada")
    print(separar)
    nueva = input("¿Desea ingresar los datos de otra tarjeta gráfica? (s/n) ")
    conn.cursor().execute(
        "INSERT INTO placas VALUES (%s, %s)",
        (nombre, watts)
    )
    conn.commit()
    
    if nueva.lower() == "s":
        agregar_placa_de_video(placas_de_video)
    return placas_de_video
## PARTE 3
# Creamos una funcion para eliminar una placa de video
def eliminar_placa_de_video(placas_de_video):
    nombre = input("Ingrese el nombre de la placa de video: ")
    del placas_de_video[nombre]
    print("Placa de video eliminada")
    print(separar)
    return placas_de_video

# Creamos una funcion para mostrar todas las placas de video
def mostrar_placas_de_video(placas_de_video):
    for nombre, watts in placas_de_video.items():
        print(f"{nombre}s")
    return placas_de_video

# Creamos una funcion para mostrar el consumo en watts de cada placa de video
def mostrar_consumo_placas_de_video(placas_de_video):
    for nombre, watts in placas_de_video.items():
        print(f"{nombre}: {watts} watts")
    return placas_de_video

# Creamos una funcion para mostrar el consumo en watts de todas las placas de video
def mostrar_consumo_total_placas_de_video(placas_de_video):
    total = 0
    for nombre, watts in placas_de_video.items():
        total += watts
    print(f"Consumo total en watts: {total} watts")
    return placas_de_video
    

## PARTE 4

def panel_mas_adecuado(placas_de_video):
    total = 0
    for nombre, watts in placas_de_video.items():
        total += watts

    mejores_paneles = []
    mejor_diferencia = float('inf')

    for r in range(1, len(paneles) + 1):
        combinations = itertools.combinations(paneles.items(), r)
        for combo in combinations:
            combo_watts = sum(watts for _, watts in combo)
            diferencia = abs(total - combo_watts)
            if diferencia <= 200 and diferencia < mejor_diferencia:
                mejores_paneles = combo
                mejor_diferencia = diferencia

    if len(mejores_paneles) > 0:
        print("Mejor combinación de paneles solares para el consumo en watts de las placas de video:")
        panel_nombres = [nombre for nombre, _ in mejores_paneles]
        panel_watts = sum(watts for _, watts in mejores_paneles)
        print(f"Paneles: {panel_nombres}, Total de watts: {panel_watts}")
    else:
        print("No hay combinaciones de paneles solares disponibles dentro del margen de consumo para cubrir el consumo total de las placas de video.")


## PARTE 5
# Creamos una funcion para mostrar el menu
def mostrar_menu():
    print("1. Agregar placa de video")
    print("2. Eliminar placa de video")
    print("3. Mostrar todas las placas de video")
    print("4. Mostrar el consumo en watts de cada placa de video")
    print("5. Mostrar el consumo en watts de todas las placas de video")
    print("6. Paneles solares más recomendados para el consumo en watts de las placas de video")
    print("7. Salir")
    
# Creamos una funcion para ejecutar el menu
def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))
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

# Ejemplo de uso:

registrar_usuario()
iniciar_sesion()

# Cerrar la conexión a la base de datos
conn.close()
 
## PARTE 6