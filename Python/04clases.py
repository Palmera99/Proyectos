class Perro:
    especie = 'mamifero'

    def __init__(self, nombre, raza):
        print(f'El perro se llama {nombre}, es de raza {raza}')
        self.nombre = nombre
        self.raza = raza

    def Ladra(self):
        print('Guau')


mi_perro = Perro('Maxito', 'Salchicha')
mi_perro.Ladra()
print(mi_perro.nombre)
print(mi_perro.especie)
