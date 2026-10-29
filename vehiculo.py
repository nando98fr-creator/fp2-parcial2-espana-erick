from abc import ABC, abstractmethod
from cliente import Cliente


class Vehiculo(ABC):
    def __init__(self, placa, color, dueno: Cliente):
        self.placa = placa.strip().upper()
        self.color = color
        self.dueno = dueno
        self.hora_entrada = None

    @abstractmethod
    def calcular_tarifa(self, horas):
        pass

    def describir(self):
        return (f"{self.placa}, color {self.color}, "
                f"dueño: {self.dueno.describir()}")
