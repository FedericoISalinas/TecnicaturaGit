import psycopg2
separador = "-" * 40
# Crear una conexión a la base de datos
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
   
def inicio_usuario():
    while True:
        nombre = input("Digite su nombre: ")
        contraseña = input("Digite su contraseña: ")

        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s",
            (nombre, contraseña)
        )
        result = cursor.fetchone()

        if result is not None:
            print("Inicio de sesión exitoso")
            print("")
            break  # Finaliza el ciclo while si el inicio de sesión es exitoso

        print("Nombre de usuario y/o contraseña incorrectos. Por favor, inténtelo nuevamente.")
        print(separador)


# Ejemplo de uso:

registrar_usuario()
    
inicio_usuario()

# Cerrar la conexión a la base de datos
conn.close()
