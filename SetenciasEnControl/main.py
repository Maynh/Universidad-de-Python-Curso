'''
#Setencia If/ELse
condicion = 768

if condicion == True:
    print('Condicion Verdadera')
elif condicion == False:
    print('Condición Falsa')
else:
    print('Condcicion no reconocida')

#Conversion de número a Texto

num = int(input('Proporcione un valor entre 1 y 3: '))
numTexto = ' '
if num == 1:
    numTexto = 'Número Uno'
elif num == 2:
    numTexto = 'Número Dos'
elif num == 3:
    numTexto = 'Número Tres'
else:
    numTexto = 'Fuera de rango'

print(f'Número proporcionado: {num} , {numTexto}')
'''

#Sintaxis  If Else simplificada (Operador Ternario)
#Se recomienda cuando el código es muy pequeño
condicion = True

print('Condición Verdadera') if condicion else print('Condición Falsa')
