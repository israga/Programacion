#fecha: 2025/07/15
#autor: Ismael Racines
#Tema: Ecuacion Cuadratica 

import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Dos Parábolas - (9, 5)")
ventana.geometry("320x290")  # Tamaño fijo

# Crear canvas para dibujar
canvas = tk.Canvas(ventana, width=300, height=250, bg="white")
canvas.place(x=10, y=10)  # Posicionamos usando .place()

# Dibujar ejes X e Y
canvas.create_line(0, 125, 300, 125, fill="gray")   # Eje X
canvas.create_line(150, 0, 150, 250, fill="gray")   # Eje Y

# Escalado: 1 unidad = 10 píxeles
def escalar_x(x):
    return x * 10

def escalar_y(y):
    return 125 - y * 5  # Invertimos y escalamos eje Y

# Función cuadrática positiva: y = x² - 10x + 14
def parabola_positiva(x):
    return x**2 - 10*x + 14

# Función cuadrática negativa: y = -x² + 10x - 14
def parabola_negativa(x):
    return -x**2 + 10*x - 14

# Dibujar parábola positiva (azul)
for x_pixel in range(0, 300):
    x = x_pixel / 10
    y = parabola_positiva(x)
    y_pixel = escalar_y(y)
    if 0 <= y_pixel <= 250:
        canvas.create_oval(x_pixel, y_pixel, x_pixel + 1, y_pixel + 1, fill="blue")

# Dibujar parábola negativa (verde)
for x_pixel in range(0, 300):
    x = x_pixel / 10
    y = parabola_negativa(x)
    y_pixel = escalar_y(y)
    if 0 <= y_pixel <= 250:
        canvas.create_oval(x_pixel, y_pixel, x_pixel + 1, y_pixel + 1, fill="green")

# Dibujar el punto (9, 5)
x_p = escalar_x(9)
y_p = escalar_y(5)
canvas.create_oval(x_p - 3, y_p - 3, x_p + 3, y_p + 3, fill="red")  # Punto en rojo
canvas.create_text(x_p + 40, y_p, text="(9, 5)", fill="black")

# Etiquetas de ecuaciones
etiqueta1 = tk.Label(ventana, text="y = x² - 10x + 14 (azul)", font=("Arial", 9))
etiqueta1.place(x=70, y=262)

etiqueta2 = tk.Label(ventana, text="y = -x² + 10x - 14 (verde)", font=("Arial", 9))
etiqueta2.place(x=70, y=275)

# Mostrar ventana
ventana.mainloop()
