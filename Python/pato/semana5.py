try:
    num = list(input('ingresa un numero de 3 o mas digitos: '))
    suma = 0
    for index in list(num):
        suma += int(index)
    print(f'la suma de los numeros es {suma}')

except:
    print('Hubo un error')
