from database import Database


class Menu:
    db = Database()
    db.connect()
    while True:
        print("1. Registrar")
        print("2. Consultar")
        print("3. Modificar")
        print("4. Vender")
        print("5. Salir")
        opcion = int(input("Selecciona una opcion: "))

        if opcion == 5:
            db.close_connection()
            exit()
        if opcion == 1:
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            idEditorial = db.getEditorial(db)
            optionEditorial = int(input("Ingresa el id de la editorial: "))
            ExistEditorial = True
            if optionEditorial not in idEditorial:
                print("No existe la editorial")
                ExistEditorial = False

            if ExistEditorial == True:
                idGenero = db.getGeneros(db)
                optionGenero = int(input("Ingresa el id del Genero: "))
                ExistGenero = True
                if optionGenero not in idGenero:
                    print("No existe el Genero.")
                    ExistGenero = False

            if ExistGenero == True:
                idIdioma = db.getIdiomas(db)
                optionIdioma = int(input("Ingresa el id del Idioma: "))
                ExistIdioma = True
                if optionIdioma not in idIdioma:
                    print("No existe el Idioma.")
                    ExistIdioma = False

            if ExistIdioma == True:
                db.insert_libro(nombre, optionIdioma, optionGenero, optionEditorial, precio, cantidad)

        if opcion == 2:
            db.get_libros(db)

        if opcion == 3:
            ids = db.get_libros(db)
            idLibro = int(input("Ingrese el id del libro: "))

            if (idLibro in ids):
                precio = float(input("Ingresa el nuevo precio: "))
                if precio >= 0:
                    cantidad = int(input("Ingresa la cantidad nueva de libros"))
                    if cantidad >= 0:
                        db.updateLibro(idLibro, precio, cantidad)
                    else:
                        print("La cantidad es incorrecta.")
                else:
                    print("El precio es incorrecto.")
            else:
                print("No existe el libro")

        if opcion == 4:
            ids = db.get_libros(db)
            idLibro = int(input("Ingrese el id del libro: "))
            if (idLibro in ids):
                cantidad = int(input("Ingresa la cantidad de libros a vender: "))
                precio, cantidadb = db.get_libro(idLibro)
                if cantidad >= 0 and cantidad <= cantidadb:
                    db.VenderLibro(idLibro, cantidad)
                    total_venta = precio * cantidad
                    print("Venta realizada correctamente. El total de la venta es de: $" + str(total_venta))
                else:
                    print("La cantidad es incorrecta.")
            else:
                print("No existe el libro")
