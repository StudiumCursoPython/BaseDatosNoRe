""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from firebase_admin import credentials, firestore, initialize_app

# Inicializar la aplicación Firebase con las credenciales
cred = credentials.Certificate('alpine-charge-403816-508bb90d3f34.json')
initialize_app(cred)

# Obtener una referencia a la base de datos Firestore
db = firestore.client()

# Ejemplo de datos para actualizar
id_alumno_a_actualizar = input ('id_del_alumno: ')

nombre_alumno = input('nombre: ')
edad_alumno = input('edad: ')
correo_alumno = input('email: ')

datos_actualizados_alumno = {
    "nombre": nombre_alumno,
    "edad": edad_alumno,
    "correo": correo_alumno
}

id_profesor_a_actualizar = input ('id_del_profesor: ')

nombre_profe = input('nombre: ')
edad_profe = input('edad: ')
correo_profe = input('email: ')

datos_actualizados_profesor = {
    "nombre": nombre_profe,
    "edad": edad_profe,
    "correo": correo_profe
}

# Actualizar datos en la colección 'alumnos'
db.collection('alumnos').document(id_alumno_a_actualizar).update(datos_actualizados_alumno)

# Actualizar datos en la colección 'profesores'
db.collection('profesor').document(id_profesor_a_actualizar).update(datos_actualizados_profesor)

print("Datos actualizados con éxito")