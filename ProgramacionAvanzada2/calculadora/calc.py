
def calcularnotaunica():
    while True:
        numero = float(input('ingresa la nota '))
        resultado = numero * 7 / 9
        print(resultado)
        if numero == 0:
            break


def calcularnotafinal():
    while True:
        notafinal = float(input('ingresa la nota final '))
        notadeseada = float(input('ingresa la nota deseada '))
        resultado = notafinal * 7 / notadeseada
        print(resultado)


while True:
    print("""Opciones:
          1. Nota Individual
          2. Nota Final
          """)
    seleccion = int(input('Ingresa una opcion (1 o 2): '))
    if seleccion == 1:
        calcularnotaunica()
    elif seleccion == 2:
        calcularnotafinal()
    else:
        print('Fin del programa')
        break
