"""
El área de un triángulo se describe de la siguiente manera: A = (b * h) / 2 .

El reto del día de hoy es:
 
 Escribir un programa que tome la base y la altura como parámetros y calcule el área del triángulo.

 Bonus: El programa debe determinar si el triángulo es isósceles, equilátero o escaleno.

 """
def calcular_triangulo(lado,lado2,lado3):
     
     if lado and lado2 != lado3:
         print(" el triangulo es isoceles")
     elif lado and lado2 == lado3:
        print('triangulo equilatero')
     else:
        print('todos los lados son distintos por lo tanto es escaleno')

def run():
      lado=int(input('ingrese primer lado del triangulo: '))
      lado2=int(input('ingresa segundo lado del triangulo: '))
      lado3=int(input('ingresa tercer lado del triangulo: '))
      calcular_triangulo(lado,lado2,lado3) 
      
      base=int(input('Ingrese base del triangulo: '))
      altura=int(input('Ingrese altura del triangulo: '))
      area=(base*altura) /2 
      print('el area del triangulo es ' + str(area))

if __name__ == "__main__":
    run()

