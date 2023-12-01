from firebase_admin import credentials, firestore, initialize_app

# Inicializar la aplicación Firebase con las credenciales
cred = credentials.Certificate('alpine-charge-403816-508bb90d3f34.json')
initialize_app(cred)

# Obtener una referencia a la base de datos Firestore
db = firestore.client()

# Función para eliminar un documento de una colección
def eliminar_documento(coleccion, identificador):
    try:
        documento = coleccion.document(identificador).get()
        if documento.exists:
            coleccion.document(identificador).delete()
            print(f'{identificador} eliminado con éxito de la colección {coleccion.id}.')
        else:
            print(f'No se encontró el documento con identificador {identificador} en la colección {coleccion.id}.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Solicitar el identificador por teclado
try:
    identificador = input("Introduce el identificador del documento a eliminar: ")
    # Puedes añadir aquí más validaciones sobre el identificador si es necesario

    # Intentar eliminar el documento en ambas colecciones
    eliminar_documento(db.collection('alumnos'), identificador)
    eliminar_documento(db.collection('profesores'), identificador)

except Exception as e:
    print(f'Ocurrió un error al procesar la entrada: {e}')


