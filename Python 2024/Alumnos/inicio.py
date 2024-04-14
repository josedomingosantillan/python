class Alumnos(list):
    def __init__(self,Nombre,ApellidoPa,ApellidoMa,FechaNacimiento,Turno,Grupo,Carrera):
        self.Nombre=Nombre
        self.ApellidoPA=ApellidoPa
        self.ApellidoMA =ApellidoMa
        self.FechaNacimiento=FechaNacimiento
        self.Turno=Turno
        self.Grupo=Grupo
        self.Carrera=Carrera

class ListAlumnos(list):
    def addAlumno(self, alumno):
        self.append(alumno)
    def getAlumnos(self):
        if len(self) ==0 :
            print("No existen registros en la lista de alumnos.")
        for alumno in self:
            print(f"Nombre: {alumno.Nombre}, Apellido: {alumno.ApellidoPA} {alumno.ApellidoMA}, Fecha de Nacimiento: {alumno.FechaNacimiento}, Turno: {alumno.Turno}, Grupo: {alumno.Grupo}, Carrera: {alumno.Carrera}")


class Menu():
    alumnos_list = ListAlumnos()
    while True:
        print("1. Registrar Alumno")
        print("2. Consultar Alumnos")
        print("3. Salir")
        opcion=int(input("Selecciona una opcion: "))

        if opcion==3:
            exit()
        if opcion==1:
            nombre= input("Nombre: ")
            apellidopa= input("Apellido Paterno: ")
            apellidoma= input("Apellido Materno: ")
            fecha_nac= input("Fecha de Nacimiento mm/dd/yyyy: ")
            Turno= input("Turno: ")
            Grupo= input("Grupo: ")
            Carrera= input("Carrera: ")
            Alumno = Alumnos(nombre,apellidopa,apellidoma,fecha_nac,Turno,Grupo,Carrera)
            alumnos_list.addAlumno(Alumno)
        if opcion==2:
            alumnos_list.getAlumnos()