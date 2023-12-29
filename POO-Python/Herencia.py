class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def imprimir(self):
        print(f"""

Nombre = {self.nombre}
Edad = {self.edad}
Grado  = {self.grado}

""")


estudiante1 = Estudiante('Hector', 24, 3)
estudiante1.imprimir()
