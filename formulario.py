import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Diccionarios para las conversiones básicas
UNIDADES = (
    '', 'uno', 'dos', 'tres', 'cuatro', 'cinco',
    'seis', 'siete', 'ocho', 'nueve'
)

DECENAS = (
    '', 'diez', 'veinte', 'treinta', 'cuarenta',
    'cincuenta', 'sesenta', 'setenta', 'ochenta', 'noventa'
)

ESPECIALES = {
    11: 'once', 12: 'doce', 13: 'trece', 14: 'catorce', 15: 'quince',
    16: 'dieciséis', 17: 'diecisiete', 18: 'dieciocho', 19: 'diecinueve',
    21: 'veintiuno', 22: 'veintidós', 23: 'veintitrés', 24: 'veinticuatro',
    25: 'veinticinco', 26: 'veintiséis', 27: 'veintisiete', 28: 'veintiocho',
    29: 'veintinueve'
}

CENTENAS = (
    '', 'ciento', 'doscientos', 'trescientos', 'cuatrocientos',
    'quinientos', 'seiscientos', 'setecientos', 'ochocientos', 'novecientos'
)

def numero_a_letras(n):
    if n == 0:
        return 'cero'
    if n == 100:
        return 'cien'

    letras = ''

    miles = n // 1000
    cientos = (n % 1000) // 100
    decenas = (n % 100) // 10
    unidades = n % 10

    # MILES
    if miles > 0:
        if miles == 1:
            letras += 'mil '
        else:
            letras += numero_a_letras(miles) + ' mil '

    # CENTENAS
    if cientos > 0:
        letras += CENTENAS[cientos] + ' '

    # DECENAS Y UNIDADES
    dos_digitos = n % 100

    if 10 < dos_digitos < 30:
        letras += ESPECIALES.get(dos_digitos, '')
    else:
        if decenas > 0:
            letras += DECENAS[decenas]
            if unidades > 0:
                letras += ' y '
        if unidades > 0:
            letras += UNIDADES[unidades]

    return letras.strip()

def convertir_a_letras():
    nombre = entry_nombre.get().strip()
    cantidad_texto = entry_cantidad.get().strip()

    if not nombre or not cantidad_texto:
        messagebox.showwarning("Faltan datos", "Por favor completa todos los campos.")
        return

    try:
        cantidad = int(cantidad_texto)
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")
        return

    if cantidad < 0 or cantidad > 9999:
        messagebox.showerror("Error", "La cantidad debe estar entre 0 y 9,999.")
        return

    cantidad_letras = numero_a_letras(cantidad).capitalize()

    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    resultado_texto = (
        f"Fecha actual: {fecha_actual}\n"
        f"Nombre: {nombre}\n"
        f"Cantidad: ${cantidad}\n"
        f"En letras: {cantidad_letras} dolares"
    )
    etiqueta_resultado.config(text=resultado_texto)

# Interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Formulario de Pago")
ventana.geometry("490x360")

tk.Label(ventana, text="Nombre del usuario:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

tk.Label(ventana, text="Cantidad a pagar (máx 9,999):").pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack(pady=5)

boton_convertir = tk.Button(ventana, text="Mostrar Recibo", command=convertir_a_letras)
boton_convertir.pack(pady=15)

etiqueta_resultado = tk.Label(ventana, text="", justify="left")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()
