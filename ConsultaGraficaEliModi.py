""" 
Curso Python empresa de 'Lenguaje de Programación Python'

Autor: José Antonio Calvo López

Fecha: Noviembre 2023

"""

from tkinter import messagebox, Entry, Listbox, PhotoImage, Label
from firebase_admin import credentials, firestore, initialize_app
import tkinter as tk, os, sys

# Inicializar la aplicación Firebase con las credenciales
cred = credentials.Certificate('alpine-charge-403816-508bb90d3f34.json')
initialize_app(cred)

# Obtener una referencia a la base de datos Firestore
db = firestore.client()

# Función para obtener y mostrar los identificadores de una colección
def mostrar_identificadores(coleccion):
    lista_identificadores.delete(0, tk.END)  # Limpiar la lista
    documentos = db.collection(coleccion).stream()
    for documento in documentos:
        identificador = documento.id
        lista_identificadores.insert(tk.END, identificador)

# Función para actualizar la colección actual y mostrar identificadores
def actualizar_mostrar_identificadores(coleccion):
    global coleccion_actual
    coleccion_actual = coleccion
    mostrar_identificadores(coleccion)

# Función para cargar los datos de un documento seleccionado en campos de entrada
def cargar_datos_seleccionados():
    seleccionados = lista_identificadores.curselection()
    if not seleccionados:
        return

    identificador = lista_identificadores.get(seleccionados[0])
    documento = db.collection(coleccion_actual).document(identificador).get()
    if documento.exists:
        datos = documento.to_dict()
        for campo, valor in datos.items():
            if campo in campos_entrada:
                campos_entrada[campo].delete(0, tk.END)
                campos_entrada[campo].insert(0, valor)

# Función para actualizar un documento con los datos ingresados
def actualizar_documento():
    seleccionados = lista_identificadores.curselection()
    if not seleccionados:
        messagebox.showwarning("Advertencia", "Selecciona un identificador para actualizar.")
        return

    identificador = lista_identificadores.get(seleccionados[0])
    nuevos_datos = {}
    for campo, entrada in campos_entrada.items():
        nuevos_datos[campo] = entrada.get()

    try:
        db.collection(coleccion_actual).document(identificador).update(nuevos_datos)
        messagebox.showinfo("Éxito", "Documento actualizado con éxito.")
        mostrar_identificadores(coleccion_actual)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

def eliminar_documento():
    seleccionados = lista_identificadores.curselection()
    if not seleccionados:
        messagebox.showwarning("Advertencia", "Selecciona un identificador para eliminar.")
        return

    identificador = lista_identificadores.get(seleccionados[0])
    try:
        db.collection(coleccion_actual).document(identificador).delete()
        messagebox.showinfo("Éxito", "Documento eliminado con éxito.")
        mostrar_identificadores(coleccion_actual)
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error al intentar eliminar el documento: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Modificar-Eliminar Documentos Firestore")
#centrado aproximado de la ventana
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

# Obtener la ruta de acceso a los recursos incluidos en el archivo
ruta_recursos = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Cargar las imágenes
icono = PhotoImage(file=os.path.join(ruta_recursos, "Studium.png"))

# Crear y configurar elementos de la GUI
frame_botones = tk.Frame(root)
frame_botones.pack()

boton_alumnos = tk.Button(frame_botones, text="Mostrar Alumnos", command=lambda: actualizar_mostrar_identificadores('alumnos'))
boton_alumnos.pack(side=tk.LEFT)

boton_profesor = tk.Button(frame_botones, text="Mostrar Profesores", command=lambda: actualizar_mostrar_identificadores('profesor'))
boton_profesor.pack(side=tk.LEFT)

# Lista para mostrar identificadores con modo de selección SINGLE y centrado
lista_identificadores = Listbox(root, selectmode=tk.SINGLE, height=15, width=50, justify=tk.CENTER)
lista_identificadores.pack()
lista_identificadores.bind("<<ListboxSelect>>", cargar_datos_seleccionados)

campos_entrada = {}  # Diccionario para almacenar los campos de entrada

# Campos de entrada para modificar datos
campos_modificar = ["nombre", "edad", "correo"]


# Construye los Labels y las entradas en funcion a campos_modificar
for campo in campos_modificar:
    label = tk.Label(root, text=f"{campo.capitalize()}:")
    label.pack()
    entrada = Entry(root)
    entrada.pack()
    campos_entrada[campo] = entrada

label_separador = Label(root, text= "------")
label_separador.pack()

frame_otros_botones = tk.Frame(root)
frame_otros_botones.pack()

boton_actualizar = tk.Button(frame_otros_botones, text="Actualizar", command=actualizar_documento)
boton_actualizar.pack(side=tk.LEFT)

boton_actualizar = tk.Button(frame_otros_botones, text="Eliminar", command=eliminar_documento)
boton_actualizar.pack(side=tk.LEFT)

# Ejecutar la aplicación
root.geometry("400x450")
root.iconphoto(True, icono)
root.mainloop()


