'''
    Proporciona tu edad:
0-10 La Infancia es Increible
10-20 Muchos cambios y muchos estudios
20-30 Amor y comienza el tarbajo

Cualquier otro valor Etapa de vida no reconocida
'''

edad = int(input('Porporciona tu edad: '))
ciclo = None

if edad >= 0 and edad < 10:
    ciclo = 'La infancia es Increible'
elif edad >=10 and edad < 20:
    ciclo = 'Muchos cambios y muchoes estudios'
elif edad >=20 and edad < 30:
    ciclo = 'Amor y comienzo el Trabajo'
else:
    ciclo = 'Etapa de vida no reconocida'

print(f'Tu edada es: {edad}, {ciclo}')