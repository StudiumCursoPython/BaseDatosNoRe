import firebase_admin
from firebase_admin import credentials, firestore

# Usar el archivo json descargado
cred = credentials.Certificate(r'alpine-charge-403816-508bb90d3f34.json')
firebase_admin.initialize_app(cred)

# Inicializa la instancia de Firestore
db = firestore.client()

''' # Función para agregar datos en el caso que no se quiera generar la id automáticamente, no recomendable
def add_data(collection_id, document_id, data):
    db.collection(collection_id).document(document_id).set(data)
'''
#Función para agregar un documento con ID (document_id) generado automáticamente, mejores prácticas
def add_data_auto_id(collection_id, data):
    doc_ref = db.collection(collection_id).add(data)
    return doc_ref

# Ejemplo de uso para agregar datos para la colección profesor

data = {
    'nombre': 'Fernado Gutierrez',
    'edad': 34,
    'correo': 'fguti@example.com',
    'ciudad': 'Palma'
}

add_data_auto_id('profesor', data)


# Ejemplo de uso para agregar datos de la colección alumnos

data = {
    'nombre': 'Francisco López',
    'edad': 36,
    'correo': 'flop@example.com',
    'ciudad': 'Tenerife'
}

add_data_auto_id('alumnos', data)
