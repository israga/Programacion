#Fecha: 2025/07/26
#Estudiante: Ismael Racines
#Tema: Formulario de compra

import tkinter as tk 
from tkinter import messagebox

#Función para calcular total
def calcular_total():
    producto = entry_producto.get().strip()
    try:
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        if precio <= 0 or cantidad <= 0:
            raise ValueError

        subtotal = precio * cantidad
        iva = subtotal * 0.15
        total = subtotal + iva

        label_subtotal.config(text=f"Subtotal: ${subtotal:.2f}")
        label_iva.config(text=f"IVA (15%): ${iva:.2f}")
        label_total.config(text=f"Total a pagar: ${total:.2f}")

    except ValueError:
        messagebox.showerror("Entrada inválida", "El precio y cantidad deben ser números positivos.")

# Función para limpiar formulario
def nueva_compra():
    entry_producto.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    label_subtotal.config(text="Subtotal:")
    label_iva.config(text="IVA (15%):")
    label_total.config(text="Total a pagar:")

# Función para mostrar cómo funciona
def mostrar_ayuda():
    messagebox.showinfo("Cómo funciona", "Hay que ingresar un producto, con el precio unitario pues del producto que se desee adquirir\nLe damos al boton de calcular y directamente nos da el precio ya con su IVA que es del 15% y con su total a pagar")

# Función para salir
def salir_app():
    ventana.quit()


#diseño de la interfaz de usuario 
ventana = tk.Tk()
ventana.title("Calculadora de compras")
ventana.geometry("600x400")


# Etiquetas y entradas
tk.Label(ventana, text="Producto:").pack(pady=5)
entry_producto = tk.Entry(ventana, width=40)
entry_producto.pack()

tk.Label(ventana, text="Precio unitario:").pack(pady=5)
entry_precio = tk.Entry(ventana, width=40)
entry_precio.pack()

tk.Label(ventana, text="Cantidad:").pack(pady=5)
entry_cantidad = tk.Entry(ventana, width=40)
entry_cantidad.pack()

# Botón Calcular
tk.Button(ventana, text="Calcular total", command=calcular_total, bg="#28a745", fg="white", width=20).pack(pady=15)

 # Resultados
label_subtotal = tk.Label(ventana, text="Subtotal:")
label_subtotal.pack()

label_iva = tk.Label(ventana, text="IVA (15%):")
label_iva.pack()

label_total = tk.Label(ventana, text="Total a pagar:")
label_total.pack()

# Menú
barra_menu = tk.Menu(ventana)

# Menú Archivo
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nueva compra", command=nueva_compra)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_app)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Ayuda
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Cómo funciona", command=mostrar_ayuda)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

ventana.config(menu=barra_menu)

ventana.mainloop()
