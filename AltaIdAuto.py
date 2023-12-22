""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from firebase_admin import credentials, firestore
import firebase_admin

# Usar el archivo json descargado
cred = credentials.Certificate(r'alpine-charge-403816-508bb90d3f34.json')
firebase_admin.initialize_app(cred)

# Inicializa la instancia de Firestore
db = firestore.client()

''' # Función para agregar datos en el caso que no se quiera generar la id automáticamente, no recomendable, no mantiene las buenas practicas de las BBDD relacionales
def agre_datos(collection_id, document_id, data):
    db.collection(collection_id).document(document_id).set(data)
'''
#Función para agregar un documento con ID (document_id) generado automáticamente, mejores prácticas
def agre_datos_auto_id(collection_id, data):
    doc_ref = db.collection(collection_id).add(data)
    return doc_ref

# Ejemplo de uso para agregar datos para la colección profesor

data = {
    'nombre': 'Nando Guti',
    'edad': 94,
    'correo': 'mguti@example.com',
    'ciudad': 'La Palma'
}

agre_datos_auto_id('profesor', data)


# Ejemplo de uso para agregar datos de la colección alumnos

data = {
    'nombre': 'Francisco Pi',
    'edad': 56,
    'correo': 'flopi@example.com',
    'ciudad': 'Sevilla'
}

agre_datos_auto_id('alumnos', data)
