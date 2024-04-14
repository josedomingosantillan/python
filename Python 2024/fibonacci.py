n=int(input('Ingresa un numero \n'))
fibonacci = [0, 1]
while fibonacci[-1] + fibonacci[-2] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(f"Serie de Fibonacci hasta {n} es: {fibonacci}")