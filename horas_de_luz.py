import datetime
import math

fecha = input("Ingresa la fecha en formato dd/mm: ")
dia, mes = map(int, fecha.split('/'))

fecha_completa = datetime.datetime(datetime.datetime.now().year, mes, dia)
dia_del_anio = fecha_completa.timetuple().tm_yday

print(f"El número de día correspondiente a la fecha {fecha} es: {dia_del_anio}")

def calcular_horas_de_luz(dia_del_anio):
    horas_de_luz = 12 + 0.5561 * math.sin((0.9863 * (dia_del_anio - 173) * math.pi / 180))
    return horas_de_luz

dia = int(input("Ingresa el día del año (1-365): "))
horas_de_luz = calcular_horas_de_luz(dia)
print(f"La cantidad aproximada de horas de luz para el día {dia} es: {horas_de_luz:.2f}")
