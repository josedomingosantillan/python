import tkinter as tk

def click_btn(event):
    # Obtener el texto del botón presionado
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Realizar el cálculo y mostrar el resultado
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        # Limpiar la entrada
        entry.delete(0, tk.END)
    else:
        # Agregar el texto del botón presionado a la entrada
        entry.insert(tk.END, text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Obtener las dimensiones de la pantalla y de la ventana
window_width = 300
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular las coordenadas para mostrar la ventana en el centro de la pantalla
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Definir las dimensiones y la posición de la ventana
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Crear la entrada para mostrar los números y resultados
entry = tk.Entry(root, font=('Arial', 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="ew")

# Configurar el peso de la primera columna (columna de la entrada) para que sea mayor
root.grid_columnconfigure(0, weight=1)

# Definir los botones y sus ubicaciones en la cuadrícula
buttons = [
    ('7', 1, 0, 1, 1), ('8', 1, 1, 1, 1), ('9', 1, 2, 1, 1), ('/', 1, 3, 1, 1),
    ('4', 2, 0, 1, 1), ('5', 2, 1, 1, 1), ('6', 2, 2, 1, 1), ('*', 2, 3, 1, 1),
    ('1', 3, 0, 1, 1), ('2', 3, 1, 1, 1), ('3', 3, 2, 1, 1), ('-', 3, 3, 1, 1),
    ('0', 4, 0, 1, 1), ('.', 4, 1, 1, 1), ('C', 4, 2, 1, 1), ('+', 4, 3, 1, 1),
    ('=', 5, 0, 1, 4)
]

# Crear y posicionar los botones
for (text, row, col, rowspan, columnspan) in buttons:
    btn = tk.Button(root, text=text, font=('Arial', 18), padx=10, pady=10)
    btn.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky="nsew")
    btn.bind("<Button-1>", click_btn)

# Configurar el tamaño de las celdas de la cuadrícula
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Ejecutar el bucle principal
root.mainloop()
