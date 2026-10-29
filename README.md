# Parqueo El Obelisco

**Nombre:** Erick Fernando España Ruiz  
**Carné:** 202201376  
**Curso:** Fundamentos de Programación 2 · IS24 · Segundo semestre 2026

## Ejecución

Requiere Python 3.9 o superior. No utiliza dependencias externas.
Desde la carpeta que contiene los siete archivos Python:

```bash
python3 main.py
```

En Windows también se puede usar `python main.py` o `py main.py`.

## Archivos y diseño

- `cliente.py`: Cliente con nombre, teléfono y descripción.
- `vehiculo.py`: Vehiculo abstracto con ABC y calcular_tarifa abstracto.
- `moto.py`: Moto, con cilindrada.
- `carro.py`: Carro, con puertas.
- `pickup.py`: Pickup, con carga_ton.
- `parqueo.py`: Parqueo, con entradas, salidas, búsqueda y recaudación.
- `main.py`: menú por terminal y validación de entradas numéricas.

Moto, Carro y Pickup heredan de Vehiculo y reutilizan sus métodos mediante
super(). La asociación se representa guardando en dueno el Cliente recibido.
La agregación se representa agregando a estacionados el vehículo recibido:
Parqueo no crea esos objetos.

## Reglamento

Capacidad de seis vehículos, horas enteras entre 6 y 22 y placas únicas
normalizadas a mayúsculas. Los rechazos no modifican los vehículos
estacionados ni la recaudación. Una salida anterior a la entrada se rechaza;
si las horas son iguales, se cobra una hora.

- Moto: Q5 por hora, sin tope.
- Carro: Q10 por hora, máximo Q60 por visita.
- Pickup: Q15 por hora más Q10 de manejo por visita.

Los datos se conservan únicamente durante la ejecución.

## Comprobación manual

1. Registrar una moto a las 8, un carro a las 8 y una pickup a las 9.
2. Intentar repetir la placa del carro: debe indicar Art. 3.
3. Intentar otra entrada a las 23: debe indicar Art. 2.
4. Agregar tres vehículos para completar seis; el séptimo debe indicar Art. 1.
5. Listar y buscar una placa en minúsculas; buscar también una inexistente.
6. Intentar sacar la moto a las 7: debe indicar Art. 4.
7. Sacar la moto a las 10 (Q10), el carro a las 16 (Q60) y la pickup a las 9 (Q25).
8. Consultar el resumen: tres espacios libres y Q95 recaudados.
9. Probar una opción inexistente, un tipo inválido y abc como hora.
10. Terminar con la opción 6.
