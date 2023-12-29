class Ropa:
    def __init__(self, costo, marca, demanda):
        self.costo = costo
        self.marca = marca
        self.demanda = demanda

    def ajustar_precio_demanda(self):
        # Lógica para ajustar el precio en función de la demanda
        # Puedes implementar diferentes estrategias según la demanda
        if self.demanda == "alta":
            self.costo *= 1.1
            return self.costo
        elif self.demanda == "baja":
            self.costo *= 0.9
            return self.costo * 0.9
        else:
            return self.costo

    def __str__(self):
        return f"Prenda de marca {self.marca}, costo: {self.costo}, demanda: {self.demanda}"

    # Método mágico diseñado por ti

    def __add__(self, otro):
        # Este método mágico permite sumar el costo de dos prendas de ropa
        return self.costo + otro.costo


# Ejemplo de uso
prenda1 = Ropa(20, "Adidas", "alta")
prenda2 = Ropa(15, "Nike", "baja")

print(prenda1)
print("Precio de venta:", prenda1.costo)
print("Precio ajustado:", prenda1.ajustar_precio_demanda())

print(prenda2)
print("Precio de venta:", prenda2.costo)
print("Precio ajustado:", prenda2.ajustar_precio_demanda())

# Usando el método mágico diseñado por ti para sumar los costos de dos prendas
total_costo = prenda1 + prenda2
print("Total de costo de las dos prendas:", total_costo)
