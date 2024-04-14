import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


# Función para registrar un alumno
def registrar_alumno():
    nombre = entry_nombre.get()
    apellido_paterno = entry_apellido_p.get()
    apellido_materno = entry_apellido_m.get()
    grupo = combo_grupo.get()

    if nombre and apellido_paterno and apellido_materno and grupo:
        # Insertar los datos del alumno en la base de datos
        cursor.execute(
            "INSERT INTO Alumnos (nombre, apellido_paterno, apellido_materno, grupo) VALUES (%s, %s, %s, %s)",
            (nombre, apellido_paterno, apellido_materno, grupo))
        conexion.commit()
        messagebox.showinfo("Éxito", "Alumno registrado correctamente.")
        cargar_alumnos()
        cargar_grupos()  # Actualizar la lista de grupos en el combobox
        limpiar_campos()
    else:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")


# Función para cargar los alumnos en la tabla
def cargar_alumnos():
    # Limpiar la tabla
    for i in tabla_alumnos.get_children():
        tabla_alumnos.delete(i)

    # Obtener los datos de los alumnos desde la base de datos
    cursor.execute("SELECT id,nombre, apellido_paterno, apellido_materno, grupo FROM Alumnos")
    alumnos = cursor.fetchall()

    # Insertar los alumnos en la tabla
    for alumno in alumnos:
        id_alumno, nombre, apellido_paterno, apellido_materno, grupo = alumno
        tabla_alumnos.insert("", tk.END, values=(id_alumno, nombre, apellido_paterno, apellido_materno, grupo))


# Función para registrar un grupo
def registrar_grupo():
    carrera = combo_carrera.get()
    grado = combo_grado.get()
    turno = combo_turno.get()  # Se obtiene el turno seleccionado del combobox
    grupo = carrera[:3].upper() + grado + "-" + turno

    # Insertar el grupo en la base de datos
    cursor.execute("INSERT INTO Grupos (nombre) VALUES (%s)", (grupo,))
    conexion.commit()
    messagebox.showinfo("Éxito", "Grupo registrado correctamente.")
    cargar_grupos()  # Actualizar la lista de grupos en el combobox
    label_grupo_generado.config(text="El grupo es: " + grupo)


# Función para cargar los grupos en el combobox
def cargar_grupos():
    # Obtener los datos de los grupos desde la base de datos
    cursor.execute("SELECT nombre FROM Grupos")
    grupos = cursor.fetchall()
    combo_grupo["values"] = [grupo[0] for grupo in grupos]


# Función para registrar una carrera
def registrar_carrera():
    nombre_carrera = entry_carrera.get()

    if nombre_carrera:
        # Insertar la carrera en la base de datos
        cursor.execute("INSERT INTO Carreras (nombre) VALUES (%s)", (nombre_carrera,))
        conexion.commit()
        messagebox.showinfo("Éxito", "Carrera registrada correctamente.")
        cargar_carreras()  # Actualizar la lista de carreras en el combobox
    else:
        messagebox.showerror("Error", "Por favor, ingrese el nombre de la carrera.")


# Función para cargar las carreras en el combobox
def cargar_carreras():
    # Obtener los datos de las carreras desde la base de datos
    cursor.execute("SELECT nombre FROM Carreras")
    carreras = cursor.fetchall()
    combo_carrera["values"] = [carrera[0] for carrera in carreras]


# Conectar a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
)
cursor = conexion.cursor()

# Crear la base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS alumnos")

# Seleccionar la base de datos recién creada
cursor.execute("USE alumnos")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Carreras (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Grupos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(10)
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Turnos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        turno VARCHAR(1)
    )
""")

# Crear las tablas si no existen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Alumnos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        apellido_paterno VARCHAR(255),
        apellido_materno VARCHAR(255),
        grupo VARCHAR(10)
    )
""")

# Insertar los turnos si no existen
cursor.execute("INSERT IGNORE INTO Turnos (turno) VALUES ('M'), ('V'), ('X')")

# Insertar algunas carreras para probar
cursor.execute("INSERT IGNORE INTO Carreras (nombre) VALUES ('Ingeniería en Sistemas Computacionales'), "
               "('Ingeniería Industrial'), ('Licenciatura en Administración'), ('Licenciatura en Psicología')")


def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_apellido_p.delete(0, tk.END)
    entry_apellido_m.delete(0, tk.END)
    combo_grupo.set('')


# Crear la ventana principal
ventana_menu = tk.Tk()
ventana_menu.title("Menú")

label_titulo_menu = ttk.Label(ventana_menu, text="Menú", font=("Arial", 16))
label_titulo_menu.pack()


def mostrar_ventana_alumnos():
    ventana_alumnos.deiconify()
    ventana_menu.iconify()


def mostrar_ventana_grupos():
    ventana_grupos.deiconify()
    ventana_menu.iconify()


boton_registrar_alumno_menu = ttk.Button(ventana_menu, text="Registrar Alumno", command=mostrar_ventana_alumnos)
boton_registrar_alumno_menu.pack()

boton_registrar_grupo_menu = ttk.Button(ventana_menu, text="Registrar Grupo", command=mostrar_ventana_grupos)
boton_registrar_grupo_menu.pack()

ventana_alumnos = tk.Toplevel(ventana_menu)
ventana_alumnos.title("Registro de Alumnos")
ventana_alumnos.geometry("400x350")
ventana_alumnos.withdraw()

frame_alumnos = ttk.Frame(ventana_alumnos)
frame_alumnos.pack(pady=10)

label_titulo_alumnos = ttk.Label(frame_alumnos, text="Registro de Alumnos", font=("Arial", 16))
label_titulo_alumnos.grid(row=0, column=0, columnspan=2)

label_nombre = ttk.Label(frame_alumnos, text="Nombre:")
label_nombre.grid(row=2, column=0, sticky="e")
entry_nombre = ttk.Entry(frame_alumnos)
entry_nombre.grid(row=2, column=1)

label_apellido_p = ttk.Label(frame_alumnos, text="Apellido Paterno:")
label_apellido_p.grid(row=3, column=0, sticky="e")
entry_apellido_p = ttk.Entry(frame_alumnos)
entry_apellido_p.grid(row=3, column=1)

label_apellido_m = ttk.Label(frame_alumnos, text="Apellido Materno:")
label_apellido_m.grid(row=4, column=0, sticky="e")
entry_apellido_m = ttk.Entry(frame_alumnos)
entry_apellido_m.grid(row=4, column=1)

label_grupo = ttk.Label(frame_alumnos, text="Grupo:")
label_grupo.grid(row=5, column=0, sticky="e")
combo_grupo = ttk.Combobox(frame_alumnos)
combo_grupo.grid(row=5, column=1)

boton_registrar_alumno = ttk.Button(frame_alumnos, text="Registrar Usuario", command=registrar_alumno)
boton_registrar_alumno.grid(row=7, column=0, columnspan=2)

frame_tabla_alumnos = ttk.Frame(ventana_alumnos)
frame_tabla_alumnos.pack(pady=10)

tabla_alumnos = ttk.Treeview(frame_tabla_alumnos,
                             columns=("Id", "Nombre", "Apellido Paterno", "Apellido Materno", "Grupo"),
                             show="headings")
tabla_alumnos.heading("Id", text="Matricula")
tabla_alumnos.heading("Nombre", text="Nombre")
tabla_alumnos.heading("Apellido Paterno", text="Apellido Paterno")
tabla_alumnos.heading("Apellido Materno", text="Apellido Materno")
tabla_alumnos.heading("Grupo", text="Grupo")
tabla_alumnos.pack()

cargar_alumnos()

ventana_grupos = tk.Toplevel(ventana_menu)
ventana_grupos.title("Registro de Grupos")
ventana_grupos.geometry("400x300")
ventana_grupos.withdraw()

frame_grupos = ttk.Frame(ventana_grupos)
frame_grupos.pack(pady=10)

label_titulo_grupos = ttk.Label(frame_grupos, text="Registro de Grupo", font=("Arial", 16))
label_titulo_grupos.grid(row=0, column=0, columnspan=2)

label_carrera = ttk.Label(frame_grupos, text="Carrera:")
label_carrera.grid(row=1, column=0, sticky="e")
combo_carrera = ttk.Combobox(frame_grupos)
combo_carrera.grid(row=1, column=1)

label_grado = ttk.Label(frame_grupos, text="Grado:")
label_grado.grid(row=2, column=0, sticky="e")
combo_grado = ttk.Combobox(frame_grupos, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
combo_grado.grid(row=2, column=1)

label_turno = ttk.Label(frame_grupos, text="Turno:")
label_turno.grid(row=3, column=0, sticky="e")
combo_turno = ttk.Combobox(frame_grupos, values=["Matutino", "Vespertino", "Mixto"])
combo_turno.grid(row=3, column=1)

boton_generar_grupo = ttk.Button(frame_grupos, text="Generar Grupo", command=registrar_grupo)
boton_generar_grupo.grid(row=4, column=0, columnspan=2)

label_grupo_generado = ttk.Label(frame_grupos, text="")
label_grupo_generado.grid(row=5, column=0, columnspan=2)

cargar_grupos()


def regresar_a_menu_alumnos():
    ventana_menu.deiconify()
    ventana_alumnos.iconify()

def regresar_a_menu_grupos():
    ventana_menu.deiconify()
    ventana_grupos.iconify()

def regresar_a_menu_editar_alumno():
    ventana_menu.deiconify()
    ventana_editar_alumno.withdraw()

# Editar Usuarios
# Crear la ventana de edición de alumno fuera de la función mostrar_ventana_editar_alumno()
ventana_editar_alumno = None


def mostrar_ventana_editar_alumno():
    global ventana_editar_alumno
    seleccion = tabla_alumnos.selection()
    if seleccion:
        # Obtener los datos del alumno seleccionado
        item = tabla_alumnos.item(seleccion)
        id_alumno = item['values'][0]  # Suponiendo que el ID está en la primera columna
        cursor.execute("SELECT * FROM Alumnos WHERE id = %s", (id_alumno,))
        alumno = cursor.fetchone()

        if ventana_editar_alumno is None:
            ventana_editar_alumno = tk.Toplevel()
            ventana_editar_alumno.title("Editar Alumno")
            centrar_ventana(ventana_editar_alumno)
            ajustar_tamano_contenido(ventana_editar_alumno)

            # Crear y configurar los widgets para mostrar los datos del alumno
            ttk.Label(ventana_editar_alumno, text="Nombre:").grid(row=0, column=0)
            entry_nombre_editar = ttk.Entry(ventana_editar_alumno)
            entry_nombre_editar.grid(row=0, column=1)
            ttk.Label(ventana_editar_alumno, text="Apellido Paterno:").grid(row=1, column=0)
            entry_apellido_paterno_editar = ttk.Entry(ventana_editar_alumno)
            entry_apellido_paterno_editar.grid(row=1, column=1)
            ttk.Label(ventana_editar_alumno, text="Apellido Materno:").grid(row=2, column=0)
            entry_apellido_materno_editar = ttk.Entry(ventana_editar_alumno)
            entry_apellido_materno_editar.grid(row=2, column=1)

            # Combobox para seleccionar el nuevo grupo
            ttk.Label(ventana_editar_alumno, text="Grupo:").grid(row=3, column=0)
            combo_grupo_editar = ttk.Combobox(ventana_editar_alumno)
            combo_grupo_editar.grid(row=3, column=1)

            # Botón para guardar los cambios
            ttk.Button(ventana_editar_alumno, text="Guardar Cambios",
                       command=lambda: guardar_cambios_alumno(id_alumno, entry_nombre_editar.get(),
                                                              entry_apellido_paterno_editar.get(),
                                                              entry_apellido_materno_editar.get(),
                                                              combo_grupo_editar.get())).grid(row=4,
                                                                                              column=0,
                                                                                              columnspan=2)

        # Mostrar la ventana de edición
        ventana_editar_alumno.deiconify()

        # Insertar datos del alumno en los campos de edición
        entry_nombre_editar.insert(0, alumno[1])  # Nombre
        entry_apellido_paterno_editar.insert(0, alumno[2])  # Apellido Paterno
        entry_apellido_materno_editar.insert(0, alumno[3])  # Apellido Materno

        # Cargar los grupos disponibles
        cargar_grupos()

        # Obtener todos los grupos disponibles
        cursor.execute("SELECT nombre FROM Grupos")
        grupos = cursor.fetchall()
        lista_grupos = [grupo[0] for grupo in grupos]

        # Establecer la lista de grupos en el combobox y seleccionar automáticamente el grupo actual del alumno
        combo_grupo_editar["values"] = lista_grupos
        combo_grupo_editar.set(alumno[4])  # Grupo actual del alumno
    else:
        messagebox.showerror("Error", "Por favor, seleccione un alumno para editar.")


def guardar_cambios_alumno(id_alumno, nombre, apellido_paterno, apellido_materno, nuevo_grupo):
    cursor.execute(
        "UPDATE Alumnos SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, grupo = %s WHERE id = %s",
        (nombre, apellido_paterno, apellido_materno, nuevo_grupo, id_alumno))
    conexion.commit()
    messagebox.showinfo("Éxito", "Datos del alumno actualizados correctamente.")
    cargar_alumnos()
    ventana_editar_alumno.destroy()


def eliminar_usuario():
    # Obtener la selección actual en la tabla
    seleccion = tabla_alumnos.selection()
    if seleccion:
        # Mostrar mensaje de confirmación
        confirmacion = messagebox.askquestion("Confirmación", "¿Estás seguro de que deseas eliminar este usuario?")
        if confirmacion == 'yes':
            # Obtener el ID del usuario seleccionado
            item = tabla_alumnos.item(seleccion)
            id_usuario = item['values'][0]
            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM Alumnos WHERE id = %s", (id_usuario,))
            conexion.commit()
            # Actualizar la tabla de usuarios
            cargar_alumnos()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
    else:
        messagebox.showerror("Error", "Por favor, seleccione un usuario para eliminar.")


boton_editar_alumno = ttk.Button(ventana_alumnos, text="Editar Alumno", command=mostrar_ventana_editar_alumno)
boton_editar_alumno.pack()

boton_eliminar_usuario = ttk.Button(ventana_alumnos, text="Eliminar Usuario", command=eliminar_usuario)
boton_eliminar_usuario.pack()

boton_regresar_alumnos = ttk.Button(ventana_alumnos, text="Regresar al Menú", command=regresar_a_menu_alumnos)
boton_regresar_alumnos.pack()

boton_regresar_grupos = ttk.Button(ventana_grupos, text="Regresar al Menú", command=regresar_a_menu_grupos)
boton_regresar_grupos.pack()

# Interfaz para registrar carreras
ventana_carreras = tk.Toplevel(ventana_menu)
ventana_carreras.title("Registro de Carreras")
ventana_carreras.geometry("300x150")
ventana_carreras.withdraw()

label_titulo_carreras = ttk.Label(ventana_carreras, text="Registro de Carreras", font=("Arial", 16))
label_titulo_carreras.pack()

label_carrera = ttk.Label(ventana_carreras, text="Nombre de la Carrera:")
label_carrera.pack()
entry_carrera = ttk.Entry(ventana_carreras)
entry_carrera.pack()

boton_registrar_carrera = ttk.Button(ventana_carreras, text="Registrar Carrera", command=registrar_carrera)
boton_registrar_carrera.pack()

# Agregar botón en la ventana principal para abrir la ventana de registro de carreras
boton_registrar_carrera_menu = ttk.Button(ventana_menu, text="Registrar Carrera", command=ventana_carreras.deiconify)
boton_registrar_carrera_menu.pack()


# Función para centrar una ventana en la pantalla
def centrar_ventana(ventana):
    ventana.update_idletasks()
    width = ventana.winfo_width()
    height = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() // 2) - (width // 1)
    y = (ventana.winfo_screenheight() // 2) - (height // 2)
    ventana.geometry('{}x{}+{}+{}'.format(width, height, x, y))


centrar_ventana(ventana_menu)
centrar_ventana(ventana_alumnos)
centrar_ventana(ventana_grupos)
centrar_ventana(ventana_carreras)


def ajustar_tamano_contenido(ventana):
    ventana.update_idletasks()
    ventana.geometry('')


ajustar_tamano_contenido(ventana_menu)
ajustar_tamano_contenido(ventana_alumnos)
ajustar_tamano_contenido(ventana_grupos)
ajustar_tamano_contenido(ventana_carreras)

cargar_carreras()

ventana_menu.mainloop()

# Cerrar la conexión con la base de datos al cerrar la ventana
conexion.close()
