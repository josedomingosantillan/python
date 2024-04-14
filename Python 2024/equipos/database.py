


class Database:
    def __init__(self):
        self.localhost = '127.0.0.1'
        self.user = "root"
        self.password = "12345"
        self.database = "ISC401V"
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.localhost,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as error:
            print("Ocurrió un error al conectar: \n")
            print(error)

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            return results
        except mysql.connector.Error as error:
            print("Ocurrió un error al ejecutar la consulta: ")
            print(error)

    def insert_equipo(self, nombre, marca, modelo, precio):
        try:
            query = "INSERT INTO equipos (EquipoId,EquipoNombre, EquipoMarca, EquipoModelo, EquipoPrecio) VALUES (%s,%s, %s, %s, %s)"
            values = (None,nombre, marca, modelo, precio)

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Registro insertado correctamente.")
        except mysql.connector.Error as error:
            print("Ocurrió un error al insertar el registro: ")
            print(error)

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()


class Menu:
    db = Database()
    db.connect()
    while True:
        print("1. Registrar Equipos")
        print("2. Consultar Equipos")
        print("3. Salir")
        opcion = int(input("Selecciona una opcion: "))

        if opcion == 3:
            db.close_connection()
            exit()
        if opcion == 1:
            nombre = input("Nombre: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            precio = float(input("Precio: "))
            db.insert_equipo(nombre, marca, modelo, precio)
        if opcion == 2:
            query = "SELECT * FROM equipos"
            results = db.execute_query(query)

            fields = [desc[0] for desc in db.cursor.description]

            print(", ".join(fields))

            for row in results:
                print(", ".join(map(str, row)))