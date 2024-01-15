'''operandoA = 3
operandoB = 2
suma = operandoA + operandoB
#print('EL resultado es: ', suma)
print(f'Resultado suma: {suma}') #sintaxis diferente f' '

resta = operandoA - operandoB
print(f'Resultado rest: {resta}')

multiplicacion = operandoA * operandoB
print(f'Resultado rest: {multiplicacion}')

division = operandoA / operandoB # poner "//" para resultado entero
print(f'Resultado rest: {division}')

modulo = operandoA % operandoB
print(f'Resultado rest: {modulo}')

exponente = operandoA ** operandoB
print(f'Resultado rest: {exponente}')

#Operador de asiganacion
miVariable = 10
print(miVariable)

#Incremento con reasignacion reasignación
miVariable = miVariable + 1
print(miVariable)

miVariable += 1 # otra sintaxis
print(miVariable)

#OPeradores de comparación

a = 4
b = 2
resultado = (a == b)
print(f' Resultado == : {resultado}')

resultado = (a != b)
print(f' Resultado != : {resultado}')


#Operadores Lógicos

a = True
b = True
resultado = a and b # Cuando ambas son verdaderos, sale verdadero
print(resultado)

a = True
b = False
resultado = a or b # Cuando hay un verdadero, sale verdadero
print(resultado)

a = True
b = False
resultado =  not b # Se invierte valor
print(resultado)

'''

# SIntaxis simplificada de operador And



edad  = int(input('Ingrese su edad: '))
#veintes = edad >= 20 and edad < 30
#print(veintes)
#treintas = edad >= 30 and edad < 40
#print(treintas)


if ( 20 >= edad < 30) or (30 >= edad <40):
    print('Dentro de rango (20\'s) o (30\'s)')
#    if veintes: #If añidado
#        print('Dentro de los 20\'s')
#    elif treintas:
#        print('Dentro de los 30\'s')
#    else:
#        print('Fuera de los rangos')
else:
    print("No esta dentro de los 20's ni 30's")


