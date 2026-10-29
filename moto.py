from vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, placa, color, dueno, cilindrada):
        super().__init__(placa, color, dueno)
        self.cilindrada = cilindrada

    def calcular_tarifa(self, horas):
        return horas * 5

    def describir(self):
        return f"Moto | {super().describir()} | {self.cilindrada} cc"
