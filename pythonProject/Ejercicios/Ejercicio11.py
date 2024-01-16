'''
    Solicitar al usuario que ingrese un mes, determinar que estacion de año corresponde al que ingreso el usuario
'''


mes = int(input('Proporciona mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Verano'
elif mes == 3 or mes == 4 or mes ==5:
    estacion = 'Otoño'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Primavera'
else:
    estacion = 'Mes incorrecto'

print(f'Para el mes {mes} la estación es: {estacion}')