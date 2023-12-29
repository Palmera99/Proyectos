numero1 = int(input('ingrese el primer numero: '))
numero2 = int(input('ingrese el segundo numero: '))

caracter = input('ingrese el uno de los siguientes caracteres (+,-,*,/): ')

suma = 0

if caracter == '+':
    suma = numero1+numero2
    print(suma)
elif caracter == '-':
    suma = numero1-numero2
    print(suma)
elif caracter == '*':
    suma = numero1*numero2
    print(suma)
elif caracter == '/':
    suma = numero1/numero2
    print(suma)
else:
    print('Ingresaste mal el caracter')
