class Ropa:
    def __init__(self, costo, marca, demanda):
        self.costo = costo
        self.marca = marca
        self.demanda = demanda

    def calcular_precio_venta(self):
        # Lógica para calcular el precio de venta en base al costo, marca y demanda
        # Aquí podrías implementar reglas específicas según tus necesidades
        precio_venta = self.costo * (1 + self.calcular_margen())
        return precio_venta

    def ajustar_precio_demanda(self):
        # Lógica para ajustar el precio en función de la demanda
        # Puedes implementar diferentes estrategias según la demanda
        if self.demanda == "alta":
            return self.calcular_precio_venta() * 1.1
        elif self.demanda == "baja":
            return self.calcular_precio_venta() * 0.9
        else:
            return self.calcular_precio_venta()

    def __str__(self):
        return f"Prenda de marca {self.marca}, costo: {self.costo}, demanda: {self.demanda}"

    def calcular_margen(self):
        # Lógica para calcular el margen de beneficio en función de la marca
        # Aquí podrías definir diferentes márgenes para diferentes marcas
        if self.marca == "premium":
            return 0.3
        elif self.marca == "normal":
            return 0.2
        else:
            return 0.1


# Ejemplo de uso
prenda1 = Ropa(20, "premium", "alta")
print(prenda1)
print("Precio de venta:", prenda1.calcular_precio_venta())
print("Precio ajustado:", prenda1.ajustar_precio_demanda())
