try:
    numero = 0
    cantnum = int(input('ingresar numeros a promediar: '))
    for cantidad in range(cantnum):
        var1 = int(input('ingresa la nota a promediar: '))
        numero += var1
    print(
        f'El promedio de las {cantnum} notas a  promediar es {numero/cantnum}')
except:
    print('hubo un error')
