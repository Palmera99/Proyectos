import random
import string


def generarpassword(longitud, agregarmayus=True, agregarminus=True, agregarnum=True, agregarsimbo=True):
    caracteres = ''
    if agregarmayus:
        caracteres += string.ascii_uppercase
    if agregarminus:
        caracteres += string.ascii_lowercase
    if agregarnum:
        caracteres += string.digits
    if agregarsimbo:
        caracteres += string.punctuation
    if not caracteres:
        print("Error: Debe seleccionar al menos un tipo de caracteres.")
        return None
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password


def main():
    print('================================')
    print('Generador de Contraseñas')

    longitud = int(input('Ingrese la Longitud de la contraseña: '))
    agregarmayus = input('¿Quiere agregar mayusculas? (Y/N)').lower() == 'y'
    agregarminus = input('¿Quiere agregar minusculas? (Y/N)').lower() == 'y'
    agregarnum = input('¿Quiere agregar numeros? (Y/N)').lower() == 'y'
    agregarsimbo = input('¿Quiere agregar simbolos? (Y/N)').lower() == 'y'

    password = generarpassword(
        longitud, agregarmayus, agregarminus, agregarnum, agregarsimbo)
    print(password)


main()
