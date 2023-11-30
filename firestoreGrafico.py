from tkinter import messagebox
from firebase_admin import credentials, firestore
import firebase_admin
import tkinter as tk

# Configuración inicial de Firebase
cred = credentials.Certificate(r'C:/Users/pepe/Downloads/alpine-charge-403816-508bb90d3f34.json')
firebase_admin.initialize_app(cred)

# Inicializar la instancia de Firestore
db = firestore.client()

# Funciones de Firebase
def add_data(collection_id, document_id, data):
    db.collection(collection_id).document(document_id).set(data)

def get_all_data(collection_id):
    documents = db.collection(collection_id).stream()
    data = []
    for doc in documents:
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id
        data.append(doc_data)
    return data

def delete_data(collection_id, document_id):
    db.collection(collection_id).document(document_id).delete()

# Funciones de la interfaz Tkinter
def actualizar_datos():
    # Limpia la lista actual
    lista_alumnos.delete(0, tk.END)

    # Obtiene y muestra los datos actualizados
    todos_los_alumnos = get_all_data('alumnos')
    for alumno in todos_los_alumnos:
        # Asegúrate de que cada alumno tenga un ID y un nombre
        # Utiliza .get() para manejar casos donde 'nombre' podría no estar presente
        id_alumno = alumno.get('id', 'ID Desconocido')
        nombre_alumno = alumno.get('nombre', 'Nombre Desconocido')

        # Inserta la información del alumno en la lista
        lista_alumnos.insert(tk.END, f"{id_alumno}: {nombre_alumno}")

# No me gusta esto, hay que hacerlo con id automática
def agregar_alumno():
    nuevo_id = entrada_id.get()
    nuevo_nombre = entrada_nombre.get()
    add_data('alumnos', nuevo_id, {'nombre': nuevo_nombre})
    actualizar_datos()

def eliminar_alumno():
    seleccion = lista_alumnos.curselection()
    if seleccion:
        id_seleccionado = lista_alumnos.get(seleccion[0]).split(':')[0]
        delete_data('alumnos', id_seleccionado)
        actualizar_datos()

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("Gestión de Alumnos")

# Crear widgets
etiqueta_id = tk.Label(raiz, text="ID del Alumno:")
etiqueta_id.pack()

entrada_id = tk.Entry(raiz)
entrada_id.pack()

etiqueta_nombre = tk.Label(raiz, text="Nombre del Alumno:")
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(raiz)
entrada_nombre.pack()

boton_agregar = tk.Button(raiz, text="Agregar Alumno", command=agregar_alumno)
boton_agregar.pack()

boton_eliminar = tk.Button(raiz, text="Eliminar Alumno Seleccionado", command=eliminar_alumno)
boton_eliminar.pack()

lista_alumnos = tk.Listbox(raiz)
lista_alumnos.pack()

# Inicializar la lista con los datos actuales
actualizar_datos()

# Ejecutar el bucle principal
raiz.mainloop()

