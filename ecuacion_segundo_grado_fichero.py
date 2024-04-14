import re

with open("ecuacion.txt", "r") as archivo:
    ecuacion_str = archivo.readline()

match = re.match(r'([+-]?\d*)x\^2\s*([+-]?\d*)x\s*([+-]?\d*)\s*=\s*0', ecuacion_str)

if match:
    a = int(match.group(1)) if match.group(1) else 1
    b = int(match.group(2)) if match.group(2) else 0
    c = int(match.group(3)) if match.group(3) else 0
else:
    print("La ecuación no está en el formato correcto.")
    exit()

# Fórmula cuadrática: x = (-b ± sqrt(b^2 - 4ac)) / 2a
discriminante = b**2 - 4*a*c

if discriminante > 0:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"Soluciones de la ecuación: x1 = {x1}, x2 = {x2}")
elif discriminante == 0:
    x = -b / (2*a)
    print(f"La ecuación tiene una solución doble: x = {x}")
else:
    print("La ecuación no tiene soluciones reales.")
