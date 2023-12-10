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
    'nombre': 'Fernado Gutierrez',
    'edad': 34,
    'correo': 'fguti@example.com',
    'ciudad': 'Palma'
}

agre_datos_auto_id('profesor', data)


# Ejemplo de uso para agregar datos de la colección alumnos

data = {
    'nombre': 'Francisco López',
    'edad': 36,
    'correo': 'flop@example.com',
    'ciudad': 'Tenerife'
}

agre_datos_auto_id('alumnos', data)
