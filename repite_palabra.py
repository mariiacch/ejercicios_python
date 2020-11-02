"""
El reto del día de hoy es crear un programa
que recibe como parámetro un string
y la cantidad de veces que queremos
repetir ese string y devuelve una cadena
con las repeteciones. ¿El twist?
Sólo puedes usar una función
 recursiva (pro tip: no olvides tu caso base).

 """
#palabra = input(' Escribe palabra a repetir:  ')
#n = int(input(' Escribe numero de repeticion: '))


def cadena(palabra, n):
    """ 
    """

    if n == 1:  # caso base para poner punto de finalizacion
        return palabra

    # caso recursivo como hay que repetir se le resta una vez la repeticion para cumplir el objetivo
    return palabra + cadena(palabra, n - 1)


print(cadena('maria', 2))
