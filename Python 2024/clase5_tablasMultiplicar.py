print("1- Incremento.")
print("2- Decremento.")

opc= int(input("Selecciona una opcion"))

if opc == 1:
    tabla= int(input("Ingresa un numero"))
    for i in range(1,11):
        print(f"{tabla} x  {i} = {tabla * i}")
elif opc == 2:
    tabla= int(input("Ingresa un numero"))
    iterador=10
    while(iterador>=1):
        print(f"{tabla} x  {iterador} = {tabla * iterador}")
        iterador-=1
else:
    print("Ocurrió un error")