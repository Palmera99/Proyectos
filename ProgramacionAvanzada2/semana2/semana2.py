class Farmaceutica:
    def __init__(self, nombre, laboratorio, precio, componente_quimico, __fecha_vencimiento):
        self.__fecha_vencimiento = __fecha_vencimiento
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.precio = precio
        self.componente_quimico = componente_quimico

    def mostrar_farmacos(self):
        print(f'''
                Nombre = {self.nombre}
                Laboratorio = {self.laboratorio}
                Precio = {self.precio}
                Componente Quimico = {self.componente_quimico}
                fecha de vencimiento  = {self.__fecha_vencimiento}
                ''')


farmaco1 = Farmaceutica('Paracetamol', 'bayer', 1500, 'C8H9NO2', '25/04/25')
farmaco2 = Farmaceutica('Ibuprofeno', 'bayer', 1500, 'C13H18O2', '25/04/25')
farmaco3 = Farmaceutica('Atorvastatina', 'bayer', 2500,
                        'C33H35FN2O5', '25/04/25')
farmaco4 = Farmaceutica('Metformina', 'bayer', 2000, 'C4H11N5', '25/04/25')
farmaco5 = Farmaceutica('Enalapril', 'bayer', 700, 'C20H28N2O5', '25/04/25')

farmaco1.mostrar_farmacos()
farmaco2.mostrar_farmacos()
farmaco3.mostrar_farmacos()
farmaco4.mostrar_farmacos()
farmaco5.mostrar_farmacos()
