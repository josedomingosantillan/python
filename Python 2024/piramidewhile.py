num= int(input("Ingresa un numero"))

if num>0:
    y=1
    while y<=num:
        z=num
        while z>=y:
            print(" ",end="")
            z-=1
        x=1
        while x<=y:
            print("* ",end="")
            x+=1
        print()
        y+=1
else:
    num= num*-1
    y=1
    while y<=num:
        x=1
        while x<=y:
            print(" ",end="")
            x+=1
        z=num
        while z>=y:
            print("*",end=" ")
            z-=1
        print()
        y+=1


