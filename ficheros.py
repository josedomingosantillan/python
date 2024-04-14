import os
def GuardarFichero():
    try:
        text = input("Ingresa un texto \n")
        nombre= input("Ingresa el nombre del archivo\n")
        print("Generando archivo ....\n")
        with open("C:/Users/MSI PRENDAMEX/Documents/Python/ArchivosTXT/"+nombre+'.txt', 'a') as archivo:
            archivo.write(text)
        print("el archivo se guardo con el nombre de: ", nombre+"\n")
    except Exception:
        print("Ocurrio un error", Exception)

def LeerFichero():
    try:
        name=input("ingresa el nombre del archivo \n")
        if os.path.exists("C:/Users/MSI PRENDAMEX/Documents/Python/ArchivosTXT/"+name+'.txt'):
            with open("C:/Users/MSI PRENDAMEX/Documents/Python/ArchivosTXT/"+name+'.txt', 'r') as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    print(linea+"\n", end='')
        else:
            print(f"El archivo '{name}' no existe.")
    except Exception:
        print("Ocurrio un error", Exception)

while True:
    print("1. Crear un archivo")
    print("2. Leer un archivo \n")
    opcion=int(input("\n"))

    if opcion ==1:
        GuardarFichero()
    elif opcion ==2:
        LeerFichero()
    else:
        print("Opcion invalida")
