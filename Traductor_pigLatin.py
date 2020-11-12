"""
El Pig Latin es una lengua lúdica que consiste en modificar las palabras con base en las siguientes condiciones:

Si una palabra comienza con sonido de consonante, se pasan todas las consonantes antes de la primer vocal y se agrega la sílaba “ay” al final (comida = omidacay).

Si la palabra inicia con vocal, entonces agrega la sílaba “way” al final (onomatopeya = onomatopeyaway).
Tu objetivo es crear un programa que reciba un texto y lo traduzca a esta lengua ¿qué resultados obtuviste?

forma ineficiente:
 if palabra[0] == 'a':
        nuevaPalabra = 'away' + palabra[:]
        print(nuevaPalabra)
    elif palabra[0] == 'e':
        nuevaPalabra = 'away' + palabra[:]
        print(nuevaPalabra)
    elif palabra[0] == 'i':
        nuevaPalabra = 'away' + palabra[:]
        print(nuevaPalabra)
    elif palabra[0] == 'o':
        nuevaPalabra = 'away' + palabra[:]
        print(nuevaPalabra)
    else:
        print('no empieza en vocal')"""
"""
"""


def run():
    vocal = ('a', 'e', 'i', 'o', 'u')
    cadena = str(input('escriba el texto a traducir '))

    for palabra in cadena:
        if cadena[0] in vocal:
            nuevaPalabra = cadena + 'away'
            print(f'{nuevaPalabra}')
            break
        else:
            nuevaPalabra = cadena[1:] + cadena[0] + 'ay'
            print(f'{nuevaPalabra}')
            break


if __name__ == "__main__":
    run()
