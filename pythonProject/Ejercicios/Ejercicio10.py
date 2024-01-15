print('Proporciones los siguientes datos del libro: ')
nom = input('Proporciona el nombre del libro:')
id = int(input('Proporciona el ID del libro: '))
precio = float(input('proporciona el valor del libro: '))
envioGratis = bool(input('Indica si es envio gratuito (True/False): ')) # SI se saca bool se puede hacer la setencia de if/ else como esta abajo

'''if envioGratis == 'True':
    envioGratis = True
elif envioGratis == 'False':
    envioGratis = False
else:
    envioGratis= 'Valor incorrecto, debe escribir True/False' '''
print(f'''
    Nombre: {nom}
    ID: {id}
    Precio: {precio}
    ENvio: {envioGratis}
''')