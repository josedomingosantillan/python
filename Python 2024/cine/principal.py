import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Datos de películas y precios
peliculas = {
    "Spiderman": {"precio": 10, "imagen": "Spider-Man.jpg"},
    "Avengers": {"precio": 12, "imagen": "avengers.jpg"},
    "Toy Story": {"precio": 8, "imagen": "toystory.jpg"}
}

# Variables globales para almacenar valores
cantidad_entradas_global = None
monto_pago_global = None

class SistemaVentas:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Ventas de Entradas")
        self.master.geometry("400x400")

        self.mostrar_formulario_peliculas()

    def mostrar_formulario_peliculas(self):
        self.frame_peliculas = tk.Frame(self.master)
        self.frame_peliculas.pack()

        self.label_pelicula = tk.Label(self.frame_peliculas, text="Seleccione una película:")
        self.label_pelicula.pack()

        # Mostrar botones e imágenes para las películas
        for pelicula, datos in peliculas.items():
            imagen = Image.open(datos["imagen"])
            imagen.thumbnail((100, 150))
            foto = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(self.frame_peliculas, image=foto)
            label_imagen.image = foto
            label_imagen.pack()
            boton_pelicula = tk.Button(self.frame_peliculas, text=pelicula,command=lambda p=pelicula: self.seleccionar_pelicula(p))
            boton_pelicula.pack()

    def seleccionar_pelicula(self, pelicula):
        global cantidad_entradas_global
        global monto_pago_global

        self.pelicula_seleccionada = pelicula
        self.frame_peliculas.destroy()

        self.frame_entradas = tk.Frame(self.master)
        self.frame_entradas.pack()

        self.label_entradas = tk.Label(self.frame_entradas, text="Cantidad de entradas:")
        self.label_entradas.pack()

        self.entry_entradas = tk.Entry(self.frame_entradas)
        self.entry_entradas.pack()

        self.boton_calcular = tk.Button(self.frame_entradas, text="Calcular Total", command=self.calcular_total)
        self.boton_calcular.pack()

    def calcular_total(self):
        global cantidad_entradas_global

        cantidad_entradas_global = int(self.entry_entradas.get())
        precio_entrada = peliculas[self.pelicula_seleccionada]["precio"]
        total_pagar = cantidad_entradas_global * precio_entrada

        messagebox.showinfo("Total a pagar", f"Total a pagar: ${total_pagar}")

        self.frame_entradas.destroy()

        self.frame_pago = tk.Frame(self.master)
        self.frame_pago.pack()

        self.label_pago = tk.Label(self.frame_pago, text="Monto de pago:")
        self.label_pago.pack()

        self.entry_pago = tk.Entry(self.frame_pago)
        self.entry_pago.pack()

        self.boton_cambio = tk.Button(self.frame_pago, text="Calcular Cambio", command=self.calcular_cambio)
        self.boton_cambio.pack()

    def calcular_cambio(self):
        global monto_pago_global

        monto_pago_global = float(self.entry_pago.get())

        if cantidad_entradas_global is None or monto_pago_global is None:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return

        total_pagar = cantidad_entradas_global * peliculas[self.pelicula_seleccionada]["precio"]
        cambio = monto_pago_global - total_pagar

        if cambio >= 0:
            messagebox.showinfo("Cambio", f"Su cambio es: ${cambio}")
            self.limpiar_y_mostrar_formulario_peliculas()
        else:
            messagebox.showerror("Error", "El monto pagado es insuficiente.")

    def limpiar_y_mostrar_formulario_peliculas(self):
        self.frame_pago.destroy()
        self.mostrar_formulario_peliculas()


def main():
    root = tk.Tk()
    sistema_ventas = SistemaVentas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
