import math

def calcular():
    a = int(input("Ingresa el valor de a\n"))
    b = int(input("Ingresa el valor de b\n"))
    c = int(input("Ingresa el valor de c\n"))

    coef = b**2 - 4*a*c

    if coef > 0:
        x1 = (-b + math.sqrt(coef)) / (2*a)
        x2 = (-b - math.sqrt(coef)) / (2*a)
        print(f"Las soluciones son x1 = {x1} y x2 = {x2}\n")
    elif coef == 0:
        x1 = -b / (2*a)
        print(f"La solución doble es x = {x1}\n")
    else:
        print("No hay soluciones reales\n")

calcular()