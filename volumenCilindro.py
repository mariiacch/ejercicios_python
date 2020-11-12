"""
8. Volumen de un cilindro
Las matemáticas son base fundamental de la lógica y programación, por eso es importante practicarlas constantemente. Un cilindro es un cuerpo geométrico que requiere de varias fórmulas, aplícalas en un programa que reciba datos como su altura y radio de las bases para mostrar el resultado acotado a un decimal.

"""
import math


def run():
    radio = int(input('Ingresa el valor del radio: '))
    altura = int(input('Ingresa el valor de la altura: '))
    Volumen = math.pi * (radio**2) * altura

    print(f'Su volumen es:  {Volumen}')


if __name__ == "__main__":
    run()
