import mysql.connector


class Database:
    def __init__(self):
        self.localhost = '127.0.0.1'
        self.user = "root"
        self.password = "12345"
        self.database = "libreria"
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

    def insert_libro(self, nombre, optionIdioma, optionGenero, optionEditorial, precio, cantidad):
        try:
            query = "INSERT INTO libro (id,nombre, id_idioma, id_genero, id_editorial,precio,existencia) VALUES (%s,%s, %s, %s, %s,%s,%s)"
            values = (None, nombre, optionIdioma, optionGenero, optionEditorial, precio, cantidad)

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Registro insertado correctamente.")
        except mysql.connector.Error as error:
            print("Ocurrió un error al insertar el registro: ")
            print(error)

    def get_libros(self, db):
        query = "SELECT lb.id as Id, lb.nombre as Nombre, id.nombre as Idioma, gn.nombre as Genero, ed.nombre as Editorial, lb.precio Precio, lb.existencia Existencia FROM libro as lb inner join cat_idioma as id on lb.id_idioma = id.id inner join cat_genero as gn on lb.id_genero = gn.id inner join cat_editorial as ed on lb.id_editorial = ed.id order by id asc;"
        results = db.execute_query(query)
        fields = [desc[0] for desc in db.cursor.description]
        print(", ".join(fields))
        idLibros = []
        for row in results:
            print(", ".join(map(str, row)))
            idLibros.append(row[0])

        return idLibros

    def get_libro(self, idLibro):
        try:
            query = "SELECT lb.id as Id, lb.nombre as Nombre, id.nombre as Idioma, gn.nombre as Genero, ed.nombre as Editorial, lb.precio Precio, lb.existencia Existencia FROM libro as lb inner join cat_idioma as id on lb.id_idioma = id.id inner join cat_genero as gn on lb.id_genero = gn.id inner join cat_editorial as ed on lb.id_editorial = ed.id where lb.id=%s"
            data = (idLibro,)
            self.cursor.execute(query, data)
            result = self.cursor.fetchone()
            if result:
                precio = result[5]
                cantidad = result[6]
                return precio, cantidad
            else:
                print(f"No se encontró ningún libro con el ID {idLibro}")
                return None, None

        except mysql.connector.Error as err:
            print(f"Error al obtener el libro: {err}")

    def getIdiomas(self, db):
        queryIdioma = "Select id,nombre from cat_idioma order by id asc;";
        resultsIdioma = db.execute_query(queryIdioma)
        fieldsIdioma = [desc[0] for desc in db.cursor.description]
        idIdioma = []
        print("Idiomas: \n")
        print(", ".join(fieldsIdioma))
        for row in resultsIdioma:
            print(", ".join(map(str, row)))
            idIdioma.append(row[0])
        return idIdioma

    def getGeneros(self, db):
        queryGenero = "Select id,nombre from cat_genero order by id asc;";
        resultsGenero = db.execute_query(queryGenero)
        fieldsGenero = [desc[0] for desc in db.cursor.description]
        idGenero = []
        print("Generos: \n")
        print(", ".join(fieldsGenero))
        for row in resultsGenero:
            print(", ".join(map(str, row)))
            idGenero.append(row[0])
        return idGenero

    def getEditorial(self, db):
        queryEditorial = "Select id,nombre from cat_editorial order by id asc;";
        resultsEditorial = db.execute_query(queryEditorial)
        fieldsEditorial = [desc[0] for desc in db.cursor.description]
        print("Editoriales: \n")
        print(", ".join(fieldsEditorial))
        idEditorial = []
        for row in resultsEditorial:
            print(", ".join(map(str, row)))
            idEditorial.append(row[0])
        return idEditorial

    def updateLibro(self, idLibro, precio, cantidad):
        try:
            queryUpdateLibro = "Update libro set precio = %s,existencia=%s where id = %s;"
            data = (precio, cantidad, idLibro)
            self.cursor.execute(queryUpdateLibro, data)
            self.connection.commit()
            print("Libro actualizado correctamente.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def VenderLibro(self, idLibro, cantidad):
        try:
            queryUpdateLibro = "Update libro set existencia= existencia - %s where id = %s;"
            data = (cantidad, idLibro)
            self.cursor.execute(queryUpdateLibro, data)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def close_connection(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
