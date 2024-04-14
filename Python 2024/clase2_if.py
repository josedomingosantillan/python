# -*- coding: utf-8 -*-

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
