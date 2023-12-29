class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def caminar(self):
        pass

    def hablar(self):
        pass

    def describeme(self):
        print('Soy un ', type(self).__name__)


class Perro(Animal):
    pass


class Gato(Animal):
    pass


mi_perro = Perro('salchicha', 10)
mi_perro.describeme()
mi_gato = Gato('Siames', 15)
mi_gato.describeme()
