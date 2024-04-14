num = int(input("Ingresa un numero: "))

if num > 0:
    for y in range(1, num+1, 1):
        z = num
        for _ in range(z, y, -1):
            print(" ", end="")
        for x in range(1, y+1, 1):
            print("* ", end="")
        print()
else:
    num = num*-1
    for y in range(1, num+1, 1):
        for x in range(1, y+1, 1):
            print(" ", end="")
        z = num
        for _ in range(z, y-1, -1):
            print("* ", end="")
        print()
