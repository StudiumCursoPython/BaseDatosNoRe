import firebase_admin
import tkinter as tk
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import messagebox


# Asegúrate de que la inicialización de Firebase y las funciones estén definidas aquí

# Configuración inicial de Firebase
cred = credentials.Certificate(r'alpine-charge-403816-508bb90d3f34.json')
firebase_admin.initialize_app(cred)

# Inicializar la instancia de Firestore
db = firestore.client()

#Función para agregar un documento con ID (document_id) generado automáticamente
def add_data_auto_id(collection_id, data):
    doc_ref = db.collection(collection_id).add(data)
    return doc_ref

# Función para agregar un alumno desde la interfaz de Tkinter
def agregar_alumno():
    # Recoger datos de los campos de entrada
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()

    # Validar datos antes de enviar
    if nombre and edad.isdigit() and correo:
        # Crear diccionario con los datos
        alumno_data = {
            'nombre': nombre,
            'edad': int(edad),
            'correo': correo
        }

        # Llamar a la función para agregar a Firestore
        doc_ref = add_data_auto_id('alumnos', alumno_data)

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", f"Alumno agregado")  # falla al coger la id  -- con ID: {doc_ref.id}")

        # Limpiar campos de entrada
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
    else:
        # Mostrar mensaje de error si los datos no son válidos
        messagebox.showerror("Error", "Por favor, ingrese datos válidos.")

# Configuración de la ventana principal de Tkinter
root = tk.Tk()
root.title("Agregar Alumno")

# Crear campos de entrada y etiquetas
label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_edad = tk.Label(root, text="Edad:")
label_edad.pack()
entry_edad = tk.Entry(root)
entry_edad.pack()

label_correo = tk.Label(root, text="Correo:")
label_correo.pack()
entry_correo = tk.Entry(root)
entry_correo.pack()

# Botón para agregar alumno
boton_agregar = tk.Button(root, text="Agregar Alumno", command=agregar_alumno)
boton_agregar.pack()

# Ejecutar la aplicación
root.mainloop()
