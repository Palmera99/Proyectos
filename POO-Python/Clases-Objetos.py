class Estudiante():
    def __init__(self, Nombre, Edad, Grado):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Grado = Grado

    def Estudiar(self):
        print(f'El estudiante {self.Nombre} esta estudiando')


Nombre = input('Ingrese el Nombre del estudiante: ')
Edad = int(input('Ingrese edad del estudiante: '))
Grado = input('Ingrese grado del estudiante: ')


estudiante1 = Estudiante(Nombre, Edad, Grado)

print(f"""
Nombre {estudiante1.Nombre}\n
edad {estudiante1.Edad}\n
Grado {estudiante1.Grado}\n
""")

while True:
    Estudiar = input('El estudiante esta estudiando? Y/N: ').lower()
    if Estudiar == 'y':
        estudiante1.Estudiar()
