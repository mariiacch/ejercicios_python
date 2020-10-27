""" El reto es escribir
un programa que tome como parametros las hrs
y los minutos

y que calcule los segundos


"""
Segundo_por_hr = 3540
Segundo_por_min = 60


def Reloj(hora, minutos):
    calculo_hr = hora * Segundo_por_hr
    calculo_min = minutos * Segundo_por_min
    print(f'{hora} hora(s) tiene {calculo_hr} segundos')
    print(f' y {minutos} minuto(s) tiene {calculo_min} segundos ')


Reloj(5, 5)
