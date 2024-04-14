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