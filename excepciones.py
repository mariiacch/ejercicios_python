# ejercicio para probar excepciones

"""Generare una funcion que va a dividir
todos los elementos de una lista por un
divisor"""


def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        # print(e) # me muestra el error
        return lista


lista = list(range(10))
divisor = 2  # si pongo de divisor 0 me sale el error de ZeroDivisionError

print(divide_elementos_de_lista(lista, divisor))
