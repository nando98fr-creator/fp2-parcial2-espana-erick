from cliente import Cliente
from moto import Moto
from carro import Carro
from pickup import Pickup
from parqueo import Parqueo


def leer_entero(mensaje):
    texto = input(mensaje).strip()
    # isascii evita caracteres como ², que isdigit acepta pero int no.
    if not texto.isascii() or not texto.isdigit() or len(texto) > 9:
        print("Dato inválido: escribe un número entero de hasta 9 dígitos.")
        return None
    return int(texto)


def main():
    parqueo = Parqueo("El Obelisco", 6)
    while True:
        print("\n=== Parqueo El Obelisco ===")
        print("1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Ver vehículos estacionados")
        print("4. Buscar vehículo por placa")
        print("5. Ver resumen del día")
        print("6. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            tipo = input("Tipo (M, C o P): ").strip().upper()
            if tipo not in ("M", "C", "P"):
                print("Tipo inválido: elige M, C o P.")
                continue
            placa = input("Placa: ").strip()
            color = input("Color: ").strip()
            mensajes = {"M": "Cilindrada: ", "C": "Puertas: ", "P": "Carga en toneladas: "}
            dato = leer_entero(mensajes[tipo])
            if dato is None:
                continue
            nombre = input("Nombre del dueño: ").strip()
            telefono = input("Teléfono: ").strip()
            hora = leer_entero("Hora de entrada: ")
            if hora is None:
                continue
            dueno = Cliente(nombre, telefono)
            if tipo == "M":
                vehiculo = Moto(placa, color, dueno, dato)
            elif tipo == "C":
                vehiculo = Carro(placa, color, dueno, dato)
            else:
                vehiculo = Pickup(placa, color, dueno, dato)
            parqueo.registrar_entrada(vehiculo, hora)
        elif opcion == "2":
            placa = input("Placa: ")
            hora = leer_entero("Hora de salida: ")
            if hora is not None:
                parqueo.registrar_salida(placa, hora)
        elif opcion == "3":
            parqueo.listar()
        elif opcion == "4":
            vehiculo = parqueo.buscar(input("Placa: "))
            if vehiculo is None:
                print("No se encontró esa placa en el parqueo.")
            else:
                print(vehiculo.describir())
        elif opcion == "5":
            print(f"Espacios libres: {parqueo.espacios_libres()}")
            print(f"Total recaudado: Q{parqueo.total_recaudado}")
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida: elige del 1 al 6.")


if __name__ == "__main__":
    main()
