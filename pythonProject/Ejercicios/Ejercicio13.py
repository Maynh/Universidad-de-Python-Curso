'''
    Instrucciones de la tarea:
EL objetivo del ejercicio es crear un sistema de  calificaciones, como sigue:
EL usuario proporciona un valor entre0 y 10.
SI esta entre 9 y 10 : Imprimir una A
SI esta entre 8 y menor a 9 : Imprimir una B
SI esta entre 7 y menor a 8 : Imprimir una C
SI esta entre 6 y menor a 7 : Imprimir una D
SI esta entre 0 y menor a 6 : Imprimir una F

Cualquier otro valor debe imprimir: Valor incorrecto

'''

nota =  int(input('Ingresa la nota entre 0 al 10: '))
notafinal = None

if 9 <= nota <= 10:
    notafinal = 'A'
elif 8 <= nota < 9:
    notafinal = 'B'
elif 7 <= nota < 8:
    notafinal = 'C'
elif 6 <= nota < 7:
    notafinal = 'D'
elif 0 <= nota < 6:
    notafinal = 'F'
else:
    notafinal = 'Valor Incorrecto'
print(f'La nota es: {notafinal}')