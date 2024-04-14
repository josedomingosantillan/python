import tkinter as tk
from tkinter import messagebox
import pyodbc

# Conexión a la base de datos Oracle
conn = pyodbc.connect('User Id=SYSTEM;Password=chivasDE1;Data Source=localhost:1521/FREE;')

cursor = conn.cursor()

# Función para autenticar usuarios
def autenticar_usuario():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    query = "SELECT COUNT(*) FROM usuarios WHERE usuario = ? AND contrasena = ?"
    cursor.execute(query, (usuario, contrasena))
    resultado = cursor.fetchone()[0]

    if resultado == 1:
        abrir_gui_recepcion_paquetes()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para abrir la GUI de recepción de paquetes
def abrir_gui_recepcion_paquetes():
    ventana_principal.destroy()

    # Crear nueva ventana para la recepción de paquetes
    ventana_recepcion_paquetes = tk.Tk()
    ventana_recepcion_paquetes.title("Recepción de Paquetes")

    # Función para insertar un nuevo paquete en la base de datos
    def insertar_paquete():
        folio = folio_entry.get()
        fecha = fecha_entry.get()
        remitente = remitente_entry.get()
        tel_remitente = tel_remitente_entry.get()
        destinatario = destinatario_entry.get()
        direccion_destinatario = direccion_destinatario_entry.get()
        tel_destinatario = tel_destinatario_entry.get()
        peso_paquete = peso_paquete_entry.get()
        observaciones_paquete = observaciones_paquete_entry.get()
        costo_envio = costo_envio_entry.get()

        query = "INSERT INTO paquetes VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (folio, fecha, remitente, tel_remitente, destinatario,
                               direccion_destinatario, tel_destinatario, peso_paquete,
                               observaciones_paquete, costo_envio))
        conn.commit()
        messagebox.showinfo("Éxito", "Paquete insertado correctamente")

    # Crear etiquetas y campos de entrada para los datos del paquete
    tk.Label(ventana_recepcion_paquetes, text="Folio:").grid(row=0, column=0)
    folio_entry = tk.Entry(ventana_recepcion_paquetes)
    folio_entry.grid(row=0, column=1)

    tk.Label(ventana_recepcion_paquetes, text="Fecha:").grid(row=1, column=0)
    fecha_entry = tk.Entry(ventana_recepcion_paquetes)
    fecha_entry.grid(row=1, column=1)

    # Repite lo anterior para el resto de los campos...

    # Botón para insertar un nuevo paquete
    insertar_button = tk.Button(ventana_recepcion_paquetes, text="Insertar Paquete", command=insertar_paquete)
    insertar_button.grid(row=10, columnspan=2)

    ventana_recepcion_paquetes.mainloop()

# Crear la ventana principal de la aplicación con la GUI de seguridad
ventana_principal = tk.Tk()
ventana_principal.title("Inicio de Sesión")

# Crear etiquetas y campos de entrada para usuario y contraseña
tk.Label(ventana_principal, text="Usuario:").grid(row=0, column=0)
usuario_entry = tk.Entry(ventana_principal)
usuario_entry.grid(row=0, column=1)

tk.Label(ventana_principal, text="Contraseña:").grid(row=1, column=0)
contrasena_entry = tk.Entry(ventana_principal, show="*")
contrasena_entry.grid(row=1, column=1)

# Botón para autenticar al usuario
autenticar_button = tk.Button(ventana_principal, text="Iniciar Sesión", command=autenticar_usuario)
autenticar_button.grid(row=2, columnspan=2)

ventana_principal.mainloop()
