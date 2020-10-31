"""
1* Comenzar a hacer comparaciones de elementos adyacentes
2* Repetir hasta tener una pasada completa sin ningun  swap o cambio

"""


def bubbleSort(array):
    n = len(array)
    cierre = 1
    for i in range(n):  # vector inicial
        print(array)
        changes = False
        for j in range(0, n-i-1):  # Este es el recorrido para cada una de las posiciones del
            # vector j es el auxiliar, n-i-1 (i-1 para quedar en la posicion previa o anterior del ciclo inicial)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                changes = True
        if not changes:
            break


array = [190, 1200, 1, 2, 3, 55, 1000, 6, 800]
bubbleSort(array)

print(" el arreglo ordenado de forma Ascendende es:  ")

for i in range(len(array)):
    print("%d" % array[i])
