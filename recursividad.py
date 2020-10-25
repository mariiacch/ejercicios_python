def factorial(n):
    """ Calcula el factorial de n.
    n int >0
    returns n!
    """
    print(n)
    if n == 1:#caso base para poner punto de finalizacion
        return 1

    return n * factorial(n-1)#caso recursivo


n = int(input('Escribe un entero: '))

print(factorial(n))
