from app.db.db import db
import logging

def addPost(user_id, post_tittle, post_create_date, post_content):
    conn = None
    cursor = None
    try:
        cursor, conn = db()

        try:
            cursor.execute("INSERT INTO TBL_Posts(UserID, PostTitle, PostCreateDate, PostContent) Values(%s, %s, %s, %s);", (user_id, post_tittle, post_create_date, post_content,))
            conn.commit()

        except Exception as e:
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
 

def getAllPost():
    conn = None
    cursor = None
    try:
        cursor, conn = db()

        try:
            cursor.execute(
                        'SELECT * FROM TBL_Posts')
            posts = cursor.fetchall()

        except Exception as e:
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

        logging.info("Success")

        return posts


def getIdPost(id):
    conn = None
    cursor = None
    try:
        cursor, conn = db()

        try:
            cursor.execute(
                        'SELECT * FROM TBL_Posts where PostID=%s',(id,))
            post = cursor.fetchone()

        except Exception as e:
            logging.info(f"Error en la transacción: {e}")
            return -99

    except Exception as e:
        # Manejar el error de conexión
        logging.info(f"Error al conectar a la base de datos: {e}")
        return -99   
    
    finally:
        # Cerrar la conexión, independientemente de si hubo un error o no
        if conn is not None:
            cursor.close()
            conn.close()            

        return post
    
def deleteIdPost(id):
    conn = None
    cursor = None
    try:
        cursor, conn = db()

        try:
            cursor.execute("DELETE FROM TBL_Posts WHERE PostID=%s", (id,))
            conn.commit()

        except Exception as e:
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

def updatePost(user_id, post_id, post_tittle, post_content):
    conn = None
    cursor = None
    try:
        cursor, conn = db()

        try:
            cursor.execute("UPDATE TBL_Posts SET PostTitle=%s, PostContent=%s WHERE PostID=%s AND UserID=%s", (post_tittle, post_content, post_id, user_id,))
            conn.commit()

        except Exception as e:
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