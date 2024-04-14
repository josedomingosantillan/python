class estudiante:
    nombre = ""
    edad = 0
    grado = 1

    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(nombre, " esta estudiando.")

while (True):
    dato = input("Ingresa una opcion")
    try:
        if dato == "estudiar":
            nombre = input("Ingresa tu nombre: ")
            edad = int(input("Ingresa tu edad: "))
            grado = int(input("Ingresa tu grado del 1 al 11: "))
            estudiante = estudiante(nombre, edad, grado).estudiar()
            dato = ""

    except ValueError as error:
        print("Ocurrio un error \n")
        print(error)
