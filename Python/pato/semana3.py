try:
    num = int(input('ingresa un numero entero: '))
    contador = 1
    while contador < 11:
        print(f'{num} * {contador} = {contador*num}')
        contador += 1
except:
    print('hubo un error')
