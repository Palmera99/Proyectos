class gato:
    def sonido(self):
        return 'miau'


class perro:
    def sonido(self):
        return 'guau'


def hacer_sonido(animal):
    print(animal.sonido())


perro1 = perro()
gato1 = gato()

hacer_sonido(gato1)
