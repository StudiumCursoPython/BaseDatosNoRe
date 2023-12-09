from firebase_admin import credentials, firestore, initialize_app

# Inicializar la aplicación Firebase con las credenciales
cred = credentials.Certificate('alpine-charge-403816-508bb90d3f34.json')
initialize_app(cred)

# Obtener una referencia a la base de datos Firestore
db = firestore.client()

# Ejemplo de datos para actualizar
id_alumno_a_actualizar = 'id_del_alumno'
datos_actualizados_alumno = {
    "edad": 21,
    "curso": "Física"
}

id_profesor_a_actualizar = 'id_del_profesor'
datos_actualizados_profesor = {
    "departamento": "Historia"
}

# Actualizar datos en la colección 'alumnos'
db.collection('alumnos').document(id_alumno_a_actualizar).update(datos_actualizados_alumno)

# Actualizar datos en la colección 'profesores'
db.collection('profesores').document(id_profesor_a_actualizar).update(datos_actualizados_profesor)

print("Datos actualizados con éxito")