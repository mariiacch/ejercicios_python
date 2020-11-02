# buscar el numero menor en  mi array
# crear dos  subarray para llevar el control de mi algoritmo
# Imprimir el resultado del ordenamiento

array = [20, 34, 68, 799, 100, 21, 23, ]


def selectionSort(array):
    # recorrer todo nuestro array
    for i in range(len(array)):
        print(f""" 
        Array principal{array} """)
        # encontrar el valor minimo restante dentro del array desordenado
        idxdes = i  # auxiliar para decir el indice del array desordenado
        for j in range(i+1, len(array)):
            if array[idxdes] > array[j]:
                idxdes = j
                print(f"""
                Array secundario{array} """)
        # ya que encontramos el minimo lo vamos a cambiar por el primer valor de neustro array desordenado
        array[i], array[idxdes] = array[idxdes], array[i]


# ejecutar la funcion
selectionSort(array)
print("""

Array ordernado:""")
for i in range(len(array)):
    print(array[i])
