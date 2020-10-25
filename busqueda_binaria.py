objetivo = int(input('escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
# la funcion max regresa el valor mas alto entre 2 valores
"""entonces ahi dice que regreese 1.0 o el objetivo si el objetivo es menor a 1.0 vamos a empezar directo
de 1.0 """
respuesta = (alto + bajo)/2
# siempre se divide entre 2

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo={bajo} alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    respuesta = (alto + bajo) / 2

""" ¿Porque la respuesta de alto y bajo se divide entre 2? para hacerla mas pequeña en cada iteracion 

Recuerda que en el espacio de busqueda se esta dividiendo entre 2"""
print(f'La raiz cuadrada de {objetivo} es {respuesta}')
