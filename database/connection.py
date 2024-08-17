import mysql.connector
from mysql.connector import Error

from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def create_connection():
    """Establecer la conexión con la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),          # Ejemplo: 'localhost'
            user=os.getenv("DB_USER"),       # Tu usuario de MySQL
            password=os.getenv("DB_PASSWORD"),# Tu contraseña de MySQL
            database=os.getenv("DB_NAME"), # El nombre de tu base de datos
            port=os.getenv("DB_PORT")
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def execute_query(query, params=None):
    """Ejecutar un procedimiento almacenado y devolver los resultados en formato de diccionario."""
    connection = create_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)
        try:
            if params is None:
                cursor.callproc(query)
            else:
                # breakpoint()
                cursor.callproc(query, params)
            
            # Confirmar la transacción
            connection.commit()
            
            results = []
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            return results
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            print(f"Consulta: {query}")
            print(f"Parámetros: {params}")
            connection.rollback()  # Revertir cambios en caso de error
        finally:
            cursor.close()
            connection.close()