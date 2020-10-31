# Realizar un juego de piedra papel o tijera en python
# debe ser humano vs computer

import random


def run():
    computer_opcion = random.randint(1, 3)
    all_opt = 1, 2, 3
    user = int(input("""
    Hey este es un mini juego de piedra papel o tijera

    USER VS COMPUTER

    Estas son tus opciones:
    
    Ingresa 1 si tu opcion es piedra
    Ingresa 2 si tu opcion es tijera
    Ingresa 3 si tu opcion es papel
    :
    
    """))
    if user and computer_opcion == all_opt:
        print('empate intenta de nuevo')
    elif user == 3 and computer_opcion == 2:
        print(f'compu winn con la opcion {computer_opcion}')
    elif computer_opcion == 3 and user == 2:
        print(f'tu ganaste y la compu perdio con la opcion {computer_opcion}')
    elif user == 1 and computer_opcion == 2:
        print(f'compu winn con la opcion {computer_opcion}')
    elif user == 2 and computer_opcion == 1:
        print(f'tu ganaste y la compu perdio con la opcion {computer_opcion}')
    elif user == 3 and computer_opcion == 1:
        print(f'tu ganaste y la compu perdio con la opcion {computer_opcion}')
    elif user == 1 and computer_opcion == 3:
        print(f'compu winn con la opcion {computer_opcion}')
    else:
        print("""
        Ingresa una opcion valida!!
        1 = Para piedra
        2= Para tijera
        3= para papel""")


if __name__ == "__main__":

    run()
