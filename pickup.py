from vehiculo import Vehiculo


class Pickup(Vehiculo):
    def __init__(self, placa, color, dueno, carga_ton):
        super().__init__(placa, color, dueno)
        self.carga_ton = carga_ton

    def calcular_tarifa(self, horas):
        return horas * 15 + 10

    def describir(self):
        return f"Pickup | {super().describir()} | {self.carga_ton} toneladas"
