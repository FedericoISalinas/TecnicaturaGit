import psycopg2 # Esto es para poder conectarnos con postgre

conexion = psycopg2.connect(user = 'postgres', password = 'B3shido', host = '127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
            valores = (
                ('Carlos', 'Lara', 'clara@email.com'),
                ('Marcos', 'Canto', 'mcanto@mail.com'),
                ('Marcelo', 'Cuenca', 'cuencam@mail.com')
            ) # es una tupla de tuplas
            cursor.executemany(sentencia, valores) # De esta manera ejecuta la sentencia
            # conexion.commit() esto se utiliza para guardar todos los registros que sean una lista
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()