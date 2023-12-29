# Definiciones
def Leerarchivo():
    with open('archivo.txt', 'r') as f:
        contenido = f.read()
        print(contenido)


def Escribirarchivo():
    with open('archivo.txt', 'w') as f:
        contenido = input('ingresa cosas para el archivo: ')
        f.write(contenido)
