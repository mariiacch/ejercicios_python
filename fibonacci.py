"""
Realiza una secuencia fibonacci
¿Que es?

Es la suma de los dos numeros anteriores
a esta

fibonacci(n)=fibonacci(n-1) + fibonacci(n-2)

0 y 1 son los caso base
pero no es practico aplicar recursividad por lo que se recomienda usar un algoritmo iterativo
"""


def fibonacci():
    n = int(input('ingresa un numero de secuencia: '))

    num1, num2 = 0, 1  # caso base
    print(f'{num1}')
    print(f'{num2}')
    for i in range(n-1):
        num3 = num1+num2
        print(f'{num3}')
        num1 = num2  # 1
        # print(num1)
        num2 = num3  # num1+num2 1
       # print(num2)


fibonacci()
