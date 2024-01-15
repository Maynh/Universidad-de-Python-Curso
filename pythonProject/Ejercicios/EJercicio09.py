'''
Intrucciones de tareas:
Solicitar al ususario dos valores y determinar cual número es el mayor
Solicitar al usuario dos valores:
numero1 (int)
numero2(int)
Se debe imprimir el mayor de los dos números (la salida debe se identica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El número mayor es: <Némro mayor)
'''
num1 = int(input('Proporciona el número 1: '))
num2 = int(input('Proporciona el número 2: '))


if num1 > num2:
    print(f'El número 1 es mayor')
else:
    print(f'El número 2  es mayor')