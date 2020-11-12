# cuantos dias faltan para mi cumpleaños
from datetime import date

#fecha_actual = datetime.now()


if __name__ == "__main__":
    micumple = date(2021, 3, 7)# my next birthday
    fechaActual = date(2020, 11, 12)

    diferencia = micumple - fechaActual

    print(f'{diferencia.days} days for your birthday ')
