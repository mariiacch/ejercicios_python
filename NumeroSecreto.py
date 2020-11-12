"""
Este es un juego sencillo que trata de adivinar un número aleatorio, 
el truco está en que no sabes cuál es ese número pero en cada ingresarás un número y sabrás si este es mayor o menor al número secreto. Así que toma en cuenta estas restricciones para intentar adivinar el número y no olvides contar el número de intentos para mostrarlo una vez aciertes.

Reglas del reto
"""
import random


def run():
    contador = 0
    numero_aleatorio = random.randint(1, 100)
    numero = int(input('Ingresa un numero entre el 1 y 100 : '))
    while numero_aleatorio != numero:
        if numero > numero_aleatorio:
            print(f'{numero} es mayor  ')
            numero = int(input('Ingresa otro numero : '))
            contador += 1
        else:
            print(f'{numero} es muy pequeño')
            numero = int(input('Ingresa otro numero : '))
            contador += 1

    print('hey adivinaste!')
    print(f'Numero de intentos: {contador} ')


if __name__ == "__main__":
    run()
