from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin

# Usar el archivo json descargado
cred = credentials.Certificate(r'alpine-charge-403816-508bb90d3f34.json')
firebase_admin.initialize_app(cred)

# Inicializa la instancia de Firestore
db = firestore.client()

#Funcion para obtener todos los datos de una colección
def coger_todos_datos(collection_id):
    documents = db.collection(collection_id).stream()
    data = []
    for doc in documents:
        doc_data = doc.to_dict()
        # Opcional, si quieres incluir el ID del documento
        doc_data['id'] = doc.id  
        data.append(doc_data)
    return data

# Todos los alumnos
todos_alumnos = coger_todos_datos('alumnos')
#Todos los users
datos_profesor = coger_todos_datos('profesor')
print(" ---- Alumnos ---- ")
for alumno in todos_alumnos:
    print(alumno)
print(" ---- Profesores ---- ")
for profesor in datos_profesor:
    print(profesor)

