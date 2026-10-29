from vehiculo import Vehiculo


class Parqueo:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.estacionados: list[Vehiculo] = []
        self.total_recaudado = 0

    def espacios_libres(self):
        return self.capacidad - len(self.estacionados)

    def buscar(self, placa):
        placa = placa.strip().upper()
        for vehiculo in self.estacionados:
            if vehiculo.placa == placa:
                return vehiculo
        return None

    def registrar_entrada(self, vehiculo, hora):
        # Todas las reglas se revisan antes de modificar el estado.
        if self.espacios_libres() <= 0:
            print("Art. 1: el parqueo está lleno.")
            return False
        if type(hora) is not int or not 6 <= hora <= 22:
            print("Art. 2: la hora debe ser un entero entre 6 y 22.")
            return False
        if self.buscar(vehiculo.placa) is not None:
            print("Art. 3: la placa ya está dentro del parqueo.")
            return False
        vehiculo.hora_entrada = hora
        self.estacionados.append(vehiculo)
        print(f"Entrada registrada: {vehiculo.placa}, hora {hora}.")
        return True

    def registrar_salida(self, placa, hora):
        vehiculo = self.buscar(placa)
        if vehiculo is None:
            print("No se encontró esa placa en el parqueo.")
            return 0
        if type(hora) is not int or not 6 <= hora <= 22:
            print("Art. 2: la hora debe ser un entero entre 6 y 22.")
            return 0
        if hora < vehiculo.hora_entrada:
            print("Art. 4: no puede salir antes de la hora de entrada.")
            return 0
        horas = max(1, hora - vehiculo.hora_entrada)
        monto = vehiculo.calcular_tarifa(horas)
        self.total_recaudado += monto
        self.estacionados.remove(vehiculo)
        print(f"Salida: {vehiculo.placa} | Horas cobradas: {horas} | Cobrar: Q{monto}")
        return monto

    def listar(self):
        if not self.estacionados:
            print("No hay vehículos estacionados.")
            return
        for vehiculo in self.estacionados:
            print(f"{vehiculo.describir()} | Hora de entrada: {vehiculo.hora_entrada}")
