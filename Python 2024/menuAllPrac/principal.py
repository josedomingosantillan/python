# -*- coding: utf-8 -*-
active = True


def menu():
    try:
        print("1.- Variables")
        print("2.- If")
        print("3.- While")
        print("4.- For")
        print("4.- For")
        print("5.- Tablas de Multiplicar")
        print("6.- Ecuaciones de 2do grado")
        print("7.- Fibonacci")
        print("8.- Piramide For")
        print("9.- Piramide While")
        print("10.- Rombo For")
        print("11.- Rombo While")
        print("12.- Binario a Decimal")
        print("13.- Decimal a Binario")
        print("14.- Potencias")
        print("15.- Salir")
        opcion = int(input("Selecciona una opción:"))
        return opcion
    except ValueError as err:
        print("Ocurrio un error")
        print(err)
        call()


def ejeVariables():
    variable = "Mensaje"
    print("tu mensaje es: ", variable)


def ejeIf():
    nombre = input("Ingresa un nombre: ")
    edad = int(input("Ingresa una edad: "))

    if 0 < edad < 120:
        if edad <= 12:
            print("{} tienes {} años y eres niño.".format(nombre, edad))
        elif 12 < edad <= 17:
            print("{} tienes {} años y eres adolescente".format(nombre, edad))
        elif 17 < edad <= 60:
            print("{} tienes {} años y eres adulto.".format(nombre, edad))
        else:
            print("{} tienes {} años y eres anciano.".format(nombre, edad))
    else:
        print("error en la edad")


def ejeWhile():
    numero = int(input('Ingresa un numero: '))

    iterador = 1
    while iterador <= numero:
        print(f"{iterador}")
        iterador += 1


def ejeFor():
    numero = int(input('Ingresa un numero: '))

    for iterador in range(1, numero + 1):
        print(f"{iterador}")


def ejeTablas():
    print("1- Incremento.")
    print("2- Decremento.")

    opc = int(input("Selecciona una opcion"))

    if opc == 1:
        tabla = int(input("Ingresa un numero"))
        for i in range(1, 11):
            print(f"{tabla} x  {i} = {tabla * i}")
    elif opc == 2:
        tabla = int(input("Ingresa un numero"))
        iterador = 10
        while (iterador >= 1):
            print(f"{tabla} x  {iterador} = {tabla * iterador}")
            iterador -= 1
    else:
        print("Ocurrió un error")


def ejeEcuaciones():
    import cmath

    def chicharronera(a, b, c):
        try:
            sqrt_part = cmath.sqrt(b ** 2 - 4 * a * c)
            x1 = (-b + sqrt_part) / (2 * a)
            x2 = (-b - sqrt_part) / (2 * a)

            if x1.imag == 0:
                x1 = x1.real
            if x2.imag == 0:
                x2 = x2.real

            return x1, x2

        except ZeroDivisionError:
            return "Error: El coeficiente 'a' no puede ser cero."
        except ValueError:
            return "Error: La ecuación no tiene soluciones reales."

    try:
        a = float(input("Ingrese el coeficiente 'a': "))
        b = float(input("Ingrese el coeficiente 'b': "))
        c = float(input("Ingrese el coeficiente 'c': "))

        soluciones = chicharronera(a, b, c)

        if isinstance(soluciones, tuple):
            print(f"Soluciones: {soluciones[0]}, {soluciones[1]}")
        else:
            print(soluciones)

    except ValueError:
        print("Error: Ingrese coeficientes válidos (números).")


def ejeFibonacci():
    n = int(input('Ingresa un numero \n'))
    if n < 0:
        n = n * -1

    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(f"Serie de Fibonacci hasta {n} es: {fibonacci}")


def ejePiramideFor():
    num = int(input("Ingresa un numero: "))

    if num > 0:
        for y in range(1, num + 1, 1):
            z = num
            for _ in range(z, y, -1):
                print(" ", end="")
            for x in range(1, y + 1, 1):
                print("* ", end="")
            print()
    else:
        num = num * -1
        for y in range(1, num + 1, 1):
            for x in range(1, y + 1, 1):
                print(" ", end="")
            z = num
            for _ in range(z, y - 1, -1):
                print("* ", end="")
            print()


def ejePiramideWhile():
    num = int(input("Ingresa un numero"))

    if num > 0:
        y = 1
        while y <= num:
            z = num
            while z >= y:
                print(" ", end="")
                z -= 1
            x = 1
            while x <= y:
                print("* ", end="")
                x += 1
            print()
            y += 1
    else:
        num = num * -1
        y = 1
        while y <= num:
            x = 1
            while x <= y:
                print(" ", end="")
                x += 1
            z = num
            while z >= y:
                print("*", end=" ")
                z -= 1
            print()
            y += 1


def ejeRomboFor():
    num = int(input("Ingresa un numero: "))

    if num < 0:
        num = num * -1
    for y in range(1, num + 1, 1):
        z = num
        for _ in range(z, y, -1):
            print(" ", end="")
        for x in range(1, y + 1, 1):
            print("* ", end="")
        print()
    for y in range(1, num, 1):
        for x in range(1, y + 1, 1):
            print(" ", end="")
        z = num
        for _ in range(z, y, -1):
            print("* ", end="")
        print()


def ejeRombowhile():
    num = int(input("Ingresa un numero"))

    if num < 0:
        num = num * -1
    y = 1
    while y <= num:
        z = num
        while z >= y:
            print(" ", end="")
            z -= 1
        x = 1
        while x <= y:
            print("* ", end="")
            x += 1
        print()
        y += 1
    y = 2
    while y <= num:
        x = 1
        while x <= y:
            print(" ", end="")
            x += 1
        z = num
        while z >= y:
            print("*", end=" ")
            z -= 1
        print()
        y += 1


def ejeBinarioToDecimal():
    numero_binario = input("Ingresa un numero")

    if numero_binario == "0":
        print("El numero es 0")
        return
    numero_decimal = int(numero_binario, 2)
    print(f"El numero {numero_binario} en decimal es {numero_decimal}")


def ejeDecimalToBinario():
    numero_decimal = int(input("Ingresa un numero"))
    numero_binario = bin(numero_decimal)[2:]
    print(f"El numero {numero_decimal} en binario es {numero_binario}")

def ejePotencias():
    try:
        base = float(input("Ingrese un número: "))
        exponente = int(input("Ingrese la potencia a la cual desea elevar el número: "))
        resultado = base ** exponente
        print(f"{base} elevado a la potencia {exponente} es igual a: {resultado}")

    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def call():
    try:
        opcion = menu()
        if opcion == 15:
            print("Saliendo....")
            exit()
        if opcion == 1:
            ejeVariables()
        if opcion == 2:
            ejeIf()
        if opcion == 3:
            ejeWhile()
        if opcion == 4:
            ejeFor()
        if opcion == 5:
            ejeTablas()
        if opcion == 6:
            ejeEcuaciones()
        if opcion == 7:
            ejeFibonacci()
        if opcion == 8:
            ejePiramideFor()
        if opcion == 9:
            ejePiramideWhile()
        if opcion == 10:
            ejeRomboFor()
        if opcion == 11:
            ejeRombowhile()
        if opcion == 12:
            ejeBinarioToDecimal()
        if opcion == 13:
            ejeDecimalToBinario()
        if opcion== 14:
            ejePotencias()

        if opcion > 15 or opcion < 1:
            print("Opcion Invalida.")
    except ValueError as err:
        print(f"Ocurrio un error {err}")



print("Menu de jose domingo Santillan Rodriguez")
while active:
    call()
