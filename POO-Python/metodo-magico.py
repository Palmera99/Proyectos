class vector():  # se crea la clase vector
    def __init__(self, a, b):  # se crea los atributos de la clase con el método __init__
        self.a = a
        self.b = b

    def __add__(self, c):  # función que ejecuta la suma de dos objetos
        return vector(self.a + c.a, self.b + c.b)


vector1 = vector(4, 9)  # instanciación de la clase objeto 1
vector2 = vector(7, 2)  # instanciación de la clase objeto 2
resultado = vector1 + vector2
print(resultado.a)
print(resultado.b)
