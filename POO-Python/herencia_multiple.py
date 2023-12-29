class Animal:
    def comer(self):
        print('esta comiendo')


class Mamifero(Animal):
    def amamantar(self):
        print('esta amamantando')


class Ave(Animal):
    def volar(self):
        print('esta volando')


class Murcielago(Mamifero, Ave):
    pass


murci = Murcielago()

murci.comer()
murci.amamantar()
murci.volar()
