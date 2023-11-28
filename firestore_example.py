import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Usar el archivo json descargado
cred = credentials.Certificate(r'alpine-charge-403816-508bb90d3f34.json')
firebase_admin.initialize_app(cred)

# Inicializa la instancia de Firestore
db = firestore.client()

# Función para agregar datos en el caso que no se quiera generar la id automáticamente, no recomendable
def add_data(collection_id, document_id, data):
    db.collection(collection_id).document(document_id).set(data)

#Función para agregar un documento con ID (document_id) generado automáticamente, mejores prácticas
def add_data_auto_id(collection_id, data):
    doc_ref = db.collection(collection_id).add(data)
    return doc_ref

#Funcion para obtener todos los datos de una colección
def get_all_data(collection_id):
    documents = db.collection(collection_id).stream()
    data = []
    for doc in documents:
        doc_data = doc.to_dict()
        # Opcional, si quieres incluir el ID del documento
        doc_data['id'] = doc.id  
        data.append(doc_data)
    return data

# Función para obtener datos concretos
def get_data(collection_id, document_id):
    doc_ref = db.collection(collection_id).document(document_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

# Ejemplo de uso para agregar datos
'''
data = {
    'nombre': 'Fernado Gutierrez',
    'edad': 34,
    'correo': 'fguti@example.com',
    'ciudad': 'Palma'
}

add_data_auto_id('profesor', data)
'''



# Obtener datos

# Todos los alumnos
todos_alumnos = get_all_data('alumnos')
#Todos los users
todos_users = get_all_data('users')

for alumno in todos_alumnos:
    print(alumno)

for user in todos_users:
    print(user)

#especificos

user_data = get_data('users', 'user_2')
alumnos_data = get_data('alumnos','1UcwfQA0QPZhbsPnRnNA')
profesores_data = get_data('profesor','6AfENRpVmw3INEANdMvf')

print(user_data, alumnos_data, profesores_data)
