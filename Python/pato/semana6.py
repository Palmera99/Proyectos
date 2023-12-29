try:
    dolares = int(input('Ingresa una cantidad de dolares: '))
    clp = 840
    print(
        f'La cantidad de {dolares} dolar/es a pesos chilenos es: {dolares*clp}')
except ValueError:
    print('Error de valor')
