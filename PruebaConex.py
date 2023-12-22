""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from firebase_admin import credentials, firestore
import firebase_admin

def verificar_conexion(db):
    try:
        # Obtener un documento o una colección como prueba
        # Se usa como límite 1 por ahorrar datos de recogida innecesarios 
        documentos = db.collection('profesor').limit(1).get()

        # Si la consulta se realiza sin errores, la conexión es buena
        if documentos:
            print("Conexión con Firestore correcta.")
        else:
            print("Conexión con Firestore correcta, pero no se encuentran los documentos.")

    except Exception as e:
        # En caso de una excepción, la conexión falló
        print(f"Error al verificar la conexión: {e}")

try:
    # Autenticación con el archivo json
    credencial = credentials.Certificate(r'alpine-charge-403816-508bb90d3f34.json')
    firebase_admin.initialize_app(credencial)

    # Inicializa la instancia de Firestore
    db = firestore.client()

    # Ejecutar la función de verificación
    verificar_conexion(db)

except FileNotFoundError as f:
    print(f"Archivo JSON erróneo o no encontrado: {f}")
except Exception as e:
    # Manejo de otras excepciones generales
    print(f"Error al inicializar Firebase: {e}")

