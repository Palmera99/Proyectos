
try:
    n = int(input('ingresa un numero natural positivo: '))
    suma = 0

    if n > 0:
        for i in range(2, n+1, 2):
            suma += i
            print(suma)
    else:
        print('no es un numero natural')
except ValueError:
    print('error de valor')
