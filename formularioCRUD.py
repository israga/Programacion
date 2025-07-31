#Tema: Formulario CRUD con Tkinter y mongodb
#Etudiante: Ismael Racines
#fecha: 

import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from bson.objectid import ObjectId

# Diseño de funciones CRUD (create, read, update, delete)
def crearEstudiante():
   datos = {
       "nombres": entry_nombres.get(),
       "apellidos": entry_apellidos.get(),
       "edad": entry_edad.get(),
       "correo": entry_correo.get()
   }
   # Valida si hay datos vacíos
   if "" in datos.values():
       messagebox.showwarning("Error", "Todos los campos son obligatorios")
       return # Abandonar la función
   
   # Guardamos el registro en la BDD
   coleccion.insert_one(datos)
   messagebox.showinfo("Éxito", "Estudiante creado con éxito")
   limpiarCampos()
   cargarEstudiantes() # Carga los registros de los estudiantes

# Limpiar los cuadros de texto
def limpiarCampos():
   entry_id.delete(0, tk.END)
   entry_apellidos.delete(0, tk.END)
   entry_nombres.delete(0, tk.END)
   entry_edad.delete(0, tk.END)
   entry_correo.delete(0, tk.END)

# Función que muestra todos los estudiantes ingresados
def cargarEstudiantes():
   lista.delete(0, tk.END)
   for estudiante in coleccion.find():
       texto = f"{estudiante['_id']} | {estudiante['apellidos']} | {estudiante['nombres']} | {estudiante['edad']} | {estudiante['correo']}"
       lista.insert(tk.END, texto)

# Función para cargar la información de un estudiante y los muestre en los cuadros de texto
def cargaUnEstudiante(event):
   selEstudiante = lista.get(lista.curselection()) # Captura la fila actual seleccionada
   id = selEstudiante.split(' | ')[0]
   estudiante = coleccion.find_one({"_id": ObjectId(id)})

   # Cargamos los cuadros de texto
   limpiarCampos()
   entry_id.insert(0, str(estudiante["_id"]))
   entry_apellidos.insert(0, (estudiante["apellidos"]))
   entry_nombres.insert(0, (estudiante["nombres"]))
   entry_edad.insert(0, (estudiante["edad"]))
   entry_correo.insert(0, str(estudiante["correo"]))

# Función para actualizar los datos del estudiante
def actualizarEstudiante():
   id = entry_id.get()
   if id == "":
       messagebox.showwarning("Error", "Selecciona un estudiante para actualizar")
       return
   nuevosDatos = {
       "nombres": entry_nombres.get(),
       "apellidos": entry_apellidos.get(),
       "edad": entry_edad.get(),
       "correo": entry_correo.get()
   }
   # Validamos que no falte ningún dato
   if "" in nuevosDatos.values():
       messagebox.showwarning("Error", "Todos los campos son obligatorios")
       return
   
   # Actualizamos el estudiante en la base de datos
   coleccion.update_one(
       {"_id": ObjectId(id)},
       {"$set": nuevosDatos}
   )
   messagebox.showinfo("Éxito", "Estudiante actualizado correctamente")
   limpiarCampos()
   cargarEstudiantes()

# Función para eliminar un estudiante de la base de datos
def eliminarEstudiante():
   id = entry_id.get()
   if id == "":
       messagebox.showwarning("Error", "Selecciona un estudiante para eliminar")
       return
   
   # Confirmación antes de eliminar
   confirmacion = messagebox.askyesno("Confirmar", "¿Estás segura que deseas eliminar este estudiante?")
   if confirmacion:
       coleccion.delete_one({"_id": ObjectId(id)})
       messagebox.showinfo("Éxito", "Estudiante eliminado correctamente")
       limpiarCampos()
       cargarEstudiantes()

# Diseño del formulario
ventana = tk.Tk()
ventana.title("Formulario de clientes")
ventana.geometry("700x400")

# Campos de formulario
tk.Label(ventana, text="ID").grid(row=0, column=0)
entry_id = tk.Entry(ventana, stat="normal")
entry_id.grid(row=0, column=1)

# Conexión a MongoDB
cliente = MongoClient("mongodb://localhost:27017")
db = cliente["Academico"]
coleccion = db["estudiantes"]
tk.Label(ventana, text="Nombres").grid(row=1, column=0)
entry_nombres = tk.Entry(ventana)
entry_nombres.grid(row=1, column=1)
tk.Label(ventana, text="Apellidos").grid(row=2, column=0)
entry_apellidos = tk.Entry(ventana)
entry_apellidos.grid(row=2, column=1)
tk.Label(ventana, text="Edad").grid(row=3, column=0)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=3, column=1)
tk.Label(ventana, text="Correo").grid(row=4, column=0)
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=4, column=1)

# Botones de acción
tk.Button(ventana, text="Crear", command=crearEstudiante).grid(row=5, column=0, pady=10)
tk.Button(ventana, text="Actualizar", command=actualizarEstudiante).grid(row=5, column=1, pady=10)
tk.Button(ventana, text="Eliminar", command=eliminarEstudiante).grid(row=5, column=2, pady=10)
tk.Button(ventana, text="Limpiar", command=limpiarCampos).grid(row=5, column=3, pady=10)

# Control para mostrar los registros ingresados
lista = tk.Listbox(ventana, width=90)
lista.grid(row=6, column=0, columnspan=4, padx=10, pady=10)
lista.bind("<<ListboxSelect>>", cargaUnEstudiante)

# Mostrar datos al momento de cargar el formulario
cargarEstudiantes()
ventana.mainloop()