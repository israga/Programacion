#Fecha: 2025/07/22
#Estudiante: Ismael Racines
#Tema: Cuadros de dialogo

import tkinter as tk 
from tkinter import filedialog, messagebox

#funcion para abrir el archivo 
def abrirArchivo():
    ruta = filedialog.askopenfilename(title="Abrir archivo", filetypes=[("Texto", "*.txt")])
    if ruta:
        with open(ruta, "r") as f:
            contenido = f.read()
        texto.delete("1.0", tk.END) 
        texto.insert(tk.END, contenido) 


#funcion para guardar el archivo
def guardarArchivo():
    ruta = filedialog.asksaveasfilename(defaultextension=".txt")
    if ruta:
        try:
            with open(ruta, "w") as f:
                f.write(texto.get("1.0", tk.END))
                messagebox.showinfo("Confirmacion", "Archivo guardado con exito")
        except:
            messagebox.showerror("Error", "Ocurrio un error al guardar el archivo")


#funcion para salir de la aplicacion 
def salirAplicacion():
    if messagebox.askyesno("Confirme","Deseas salir de la aplicacion ?"):
        ventana.quit()


#funcion acerca de
def acercaDe():
    messagebox.showinfo("Acerca de", "Editor de texto\nDesarrollado por Ismael Racines\nTodos los derechos reservados")  

#funcion manual de usuario
def manualUsuario():
    messagebox.showinfo("Mensaje", "En proceso de construccion") 

#diseño de la interfaz de usuario 
ventana = tk.Tk()
ventana.title("Sistema Academico - Menu Principal")
ventana.geometry("600x400")


#Area de texto principal 
texto = tk.Text(ventana, wrap="word", font=("Arial",12))
texto.pack(expand=True, fill="both", padx=5, pady=5)

#barra de menu
barraMenu = tk.Menu(ventana)

#Menu archivo
menuArchivo = tk.Menu(barraMenu, tearoff=0)
menuArchivo.add_command(label="Abrir", command=abrirArchivo)
menuArchivo.add_command(label="Guardar", command=guardarArchivo)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=salirAplicacion)
barraMenu.add_cascade(label="Archivo", menu=menuArchivo)

#actividad para el estudiante: agregue el menu de ayuda con las siguientes
#opciones: Acerca de  - Manual de usuario
#asignar la barra de menu en la ventana 
menudeAyuda = tk.Menu(barraMenu, tearoff=0)
menudeAyuda.add_command(label="Acerca de", command=acercaDe)
menudeAyuda.add_command(label="Manual de usuario", command=manualUsuario)
barraMenu.add_cascade(label="Ayuda", menu=menudeAyuda)

#asignar la barra de menu en la ventana 
ventana.config(menu=barraMenu)



#agregue un tercer menu "operaciones" que tiene las siguientes las siguientes opciones:
#Mis pasatiempos - Mis tareas pendientes - Carta a mi madre 
#Mis pasatiempos: se debe mostrar en el cuadro de texto una lista de 
#todo aquello que le gusta hacer 
#Mis tareas: lista de actividades que debe realizar diariamente 
#Carta a mi madre: carta con al menos 5 lineas 


#funcion mis pasatiempos
def mostrarPasatiempos():
     texto.delete(1.0, tk.END)
     texto.insert(tk.END, "Pasatiempos:\n")
     texto.insert(tk.END, "Hacer ejercicios de fuerza\n")
     texto.insert(tk.END, "Trotar en las mañanas\n")
     texto.insert(tk.END, "Practicar Karate algo que me gustaria\n")

#funcion mis tareas
def misTareas():
     texto.delete(1.0, tk.END)
     texto.insert(tk.END, "Despierto en las mañanas y ayudo en los caseres del hogar\n")
     texto.insert(tk.END, "Me pongo a practicar las materias de la Universidad\n")
     texto.insert(tk.END, "Hago las tareas pendientes de las diversas materias que hay")

#funcion poema para mis padres
def poemaPadres():
     texto.delete(1.0, tk.END)
     texto.insert(tk.END, "Mi padre duerme. Su semblante augusto figura un apacible corazón; está ahora tan dulce... si hay algo en él de amargo, seré yo. Hay soledad en el hogar; se reza; y no hay noticias de los hijos hoy. Mi padre se despierta, ausculta la huida a Egipto, el restañante adiós. Está ahora tan cerca; si hay algo en él de lejos, seré yo. Y mi madre pasea allá en los huertos, saboreando un sabor ya sin sabor. Está ahora tan suave, tan ala, tan salida, tan amor. Hay soledad en el hogar sin bulla, sin noticias, sin verde, sin niñez. Y si hay algo quebrado en esta tarde, y que baja y que cruje, son dos viejos caminos blancos, curvos. Por ellos va mi corazón a pie")

#Menu de operaciones
menuOperaciones = tk.Menu(barraMenu, tearoff=0)
menuOperaciones.add_command(label="Mis pasatiempos", command=mostrarPasatiempos)
menuOperaciones.add_command(label="Mis tareas", command=misTareas)
menuOperaciones.add_command(label="Poema a mis padres", command=poemaPadres)
barraMenu.add_cascade(label="Operaciones", menu=menuOperaciones)


#Muestra el formulario 
ventana.mainloop()