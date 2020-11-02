# Realiza una calculadora en python

def calculator():
    if operador == '+':
        suma = valor1 + valor2
        print(suma)
    elif operador == '-':
        resta = valor1 - valor2
        print(resta)
    elif operador == '*':
        multiplicacion = valor1 * valor2
        print(multiplicacion)
    elif operador == '/':
        division = valor1 / valor2
        print(division)
    else:
        print('ingresa un operador valido')


if __name__ == "__main__":
    valor1 = int(input('Ingresa valor 1:  '))
    operador = input('Ingresa operador:  ')
    valor2 = int(input('Ingresa valor 2:  '))
    

    calculator()
