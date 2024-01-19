import psycopg2
import logging

def db():
    conn = psycopg2.connect(
        host="db-postgres",
        database="postgres",
        port="5432",
        user="postgres",
        password="123456789Zz.")

    cursor = conn.cursor()

    return cursor, conn


def make_safety_query(query):
    conn = None
    try:
        # Establecer conexión
        cursor, conn = db()

        try:
            # Iniciar la transacción
            cursor.execute("BEGIN")

            # Ejecutar la consulta
            cursor.execute(query)

            # Confirmar la transacción si todo fue exitoso
            cursor.execute("COMMIT")

        except Exception as e:
            # Si hay un error, realizar un rollback
            cursor.execute("ROLLBACK")
            logging.info(f"Error en la transacción: {e}")

        finally:
            # Cerrar el cursor
            cursor.close()

    except Exception as e:
        # Manejar el error de conexión
        logging.info(f"Error al conectar a la base de datos: {e}")

    finally:
        # Cerrar la conexión, independientemente de si hubo un error o no
        if conn is not None:
            cursor.close()
            conn.close()
