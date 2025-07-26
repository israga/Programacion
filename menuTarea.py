#Fecha: 2025/07/26
#Estudiante: Ismael Racines
#Tema: Registros de Informacion

import tkinter as tk 
from tkinter import messagebox

Trabajadores = []

#Funcion para guardar datos
def guardar_trabajadores():
    nombre = entry_nombre.get().strip()
    cargo = entry_cargo.get().strip()
    departamento = entry_departamento.get().strip()
    if not nombre or not cargo or not departamento:
        messagebox.showwarning("Campos Vacíos", "Ingrese los datos requeridos, Gracias.")
        return

    # Agregar a la lista
    Trabajadores.append((nombre, cargo, departamento))
    mostrar_empleados()
    limpiar()

# Función para limpiar los campos del formulario
def limpiar():
    entry_nombre.delete(0, tk.END)
    entry_cargo.delete(0, tk.END)
    entry_departamento.delete(0, tk.END)

# Función para mostrar los registros en el Text
def mostrar_empleados():
    text_registros.delete('1.0', tk.END)
    for idx, (nombre, cargo, departamento) in enumerate(Trabajadores, start=1):
        registro = f"{idx}. Nombre: {nombre}, Cargo: {cargo}, Departamento: {departamento}\n"
        text_registros.insert(tk.END, registro)

# Función para mostrar ventana "Acerca de"
def acercaDe():
    messagebox.showinfo("Acerca de", "Formulario Registro de Empleados")

# Función para salir de la aplicación
def salir():
    ventana.quit()

#diseño de la interfaz de usuario 
ventana = tk.Tk()
ventana.title("Registro de empleados")
ventana.geometry("600x400")

# Etiquetas y Entradas
tk.Label(ventana, text="Nombre:").pack(pady=3)
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.pack()

tk.Label(ventana, text="Cargo:").pack(pady=3)
entry_cargo = tk.Entry(ventana, width=40)
entry_cargo.pack()

tk.Label(ventana, text="Departamento:").pack(pady=3)
entry_departamento = tk.Entry(ventana, width=40)
entry_departamento.pack()

#Boton de guardar
tk.Button(ventana, text="Guardar", command=guardar_trabajadores, bg="#005ACC", fg="white", width=15).pack(pady=10)

# Área de texto para mostrar los registros
tk.Label(ventana, text="Registros Guardados:").pack()
text_registros = tk.Text(ventana, height=10, width=65)
text_registros.pack(pady=5)

#Barra de menu
barraMenu = tk.Menu(ventana)

#Menu de archivo 
menuArchivo = tk.Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label="Limpiar", command=limpiar)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command= salir)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

#Menu de Ayuda
menuAyuda = tk.Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Acerca de", command=acercaDe)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)

#Asiganar la barra de menu
ventana.config(menu=barraMenu)

#Muestre el formulario
ventana.mainloop()