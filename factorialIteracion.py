# Realizar la funcion factorial de un numero
# (n*factorial(n-1))

# n = 3!= 1*2*3
# n!=n*(n-1)

n = int(input('ingresa el valor para calcular su factorial: '))

factorial = 1


if n == 0 or n == 1:
    factorial = 1
else:
    for i in range(1, n + 1):
        factorial *= i
        print(i-1)
    print(f'{n}!= {factorial}')
