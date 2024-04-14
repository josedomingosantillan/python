class Trabajador:
    def __init__(self, ID, nombre, puesto, dias_trabajados, sueldo_diario, area):
        self.ID = ID
        self.nombre = nombre
        self.puesto = puesto
        self.dias_trabajados = dias_trabajados
        self.sueldo_diario = sueldo_diario
        self.area = area

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_puesto(self):
        return self.puesto

    def set_puesto(self, puesto):
        self.puesto = puesto

    def get_dias_trabajados(self):
        return self.dias_trabajados

    def set_dias_trabajados(self, dias_trabajados):
        self.dias_trabajados = dias_trabajados

    def get_sueldo_diario(self):
        return self.sueldo_diario

    def set_sueldo_diario(self, sueldo_diario):
        self.sueldo_diario = sueldo_diario

    def get_area(self):
        return self.area

    def set_area(self, area):
        self.area = area

    def calcular_sueldo_semanal(self):
        return self.dias_trabajados * self.sueldo_diario


class Supervisor(Trabajador):
    def __init__(self, ID, nombre, puesto, dias_trabajados, sueldo_diario, area, personas_a_cargo):
        super().__init__(ID, nombre, puesto, dias_trabajados, sueldo_diario, area)
        self.personas_a_cargo = personas_a_cargo

    def get_personas_a_cargo(self):
        return self.personas_a_cargo

    def set_personas_a_cargo(self, personas_a_cargo):
        self.personas_a_cargo = personas_a_cargo

    def calcular_sueldo_semanal(self):
        if self.personas_a_cargo <= 10:
            return super().calcular_sueldo_semanal() * 1.05
        else:
            return super().calcular_sueldo_semanal() * 1.1

nombre = input("Ingrese el nombre del Trabajador: ")
puesto = input("Ingrese el puesto del Trabajador: ")
dias_trabajados = int(input("Ingrese los días trabajados en número entero: "))
sueldo_diario = float(input("Ingrese el sueldo diario puede incluir decimales: "))
area = input("Ingrese el área del Trabajador: ")


trabajador1 = Trabajador(1, nombre, puesto, dias_trabajados, sueldo_diario, area)

personas_a_cargo = int(input("Ingrese el número de personas a cargo del Supervisor: "))

supervisor1 = Supervisor(1, nombre, puesto, dias_trabajados, sueldo_diario, area, personas_a_cargo)

print("Sueldo semanal del trabajador: ", trabajador1.calcular_sueldo_semanal())


print("Sueldo semanal del supervisor: ", supervisor1.calcular_sueldo_semanal())
