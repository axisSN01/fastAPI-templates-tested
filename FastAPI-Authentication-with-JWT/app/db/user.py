from app.db.db import db
from passlib.hash import sha256_crypt
import logging

def createUser(user_full_name, user_email, user_password):
    conn = None
    cursor = None
    try:
        cursor, conn = db()
        
        try:
            user_password = sha256_crypt.encrypt(user_password)
            # Iniciar la transacción
            cursor.execute("BEGIN")

            cursor.execute("INSERT INTO TBL_Users(UserFullName, UserEmail, UserPassword) Values(%s, %s, %s);", (user_full_name, user_email, user_password,))

            # Confirmar la transacción si todo fue exitoso
            cursor.execute("COMMIT")


        except Exception as e:
            # Si hay un error, realizar un rollback
            cursor.execute("ROLLBACK")
            logging.info(f"Error en la transacción: {e}")

            return 0

    except Exception as e:
        # Manejar el error de conexión
        logging.info(f"Error al conectar a la base de datos: {e}")
        return 0

    finally:
        # Cerrar la conexión, independientemente de si hubo un error o no
        if conn is not None:
            cursor.close()
            conn.close()            
        return 1

def checkUser(login_email, login_password):
    conn = None
    cursor = None
    try:
        cursor, conn = db()  
        try:
            cursor.execute(
                        'SELECT UserPassword FROM TBL_Users WHERE UserEmail=%s', (login_email,))
            user = cursor.fetchone()

        except Exception as e:
            logging.info(f"Error en la transacción: {e}")
            return 0

    except Exception as e:
        # Manejar el error de conexión
        logging.info(f"Error al conectar a la base de datos: {e}")
        return 0

    finally:

        if conn is not None:
            cursor.close()
            conn.close()

        if sha256_crypt.verify(login_password, user[0]) != True:
            return 0
        else:
            return 1