"""
enumeracion exhaustiva
tambien llamado adivina y verifica
las computadoras actuales son muy rapidas

es uno de los primeros algoritmos
que se debe tratar


problema: raices cuadradas
determinar si un numero tiene una raiz cuadrada exacta"""

objetivo = int(input('escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:  # mientras que la respuesta al cuadrado sea menor que el objetivo
    print(respuesta)  # para entender que esta pasando
    respuesta += 1
"""significa que va aprobar 1*1 2*2 3*3 4*4 5*5... 
hasta que encontremos la respuesta
"""
if respuesta**2 == objetivo:
    print(f'la raiz cuadrada de {objetivo} es { respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')
