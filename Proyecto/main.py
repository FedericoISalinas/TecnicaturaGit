import proyecto
import basededatos
import psycopg2

# Ejecutamos el inicio de sesion

basededatos.registrar_usuario()
basededatos.inicio_usuario()
proyecto.ejecutar_menu()
