def sumar(num1, num2, num3):
    suma = num1 + num2 + num3

    if suma < 10:
        return min(num1, num2, num3)
    elif suma > 15:
        return max(num1, num2, num3)
    else:
        numero_intermedio = suma - \
            (max(num1, num2, num3) + min(num1, num2, num3))
        return numero_intermedio


def ordenar_palabras(palabra):
    letras_ordenadas = sorted(palabra)
    letra_ordenada = ''.join(letras_ordenadas)
    return letra_ordenada


def listar_numeros(*args):
    suma = 0
    for i in args:
        if i == 0:
            suma += 1
    if suma >= 2:
        return True

    else:
        return False


def contar_primos(num1):
    return
