"""Cálculo de la tarifa de un parqueadero."""

import math

MINUTOS_DE_GRACIA = 15
MINUTOS_MAXIMOS = 1440
TARIFA_POR_HORA = {"carro": 3000, "moto": 1500}
TOPE_DIARIO = {"carro": 25000, "moto": 12000}


def calcular_tarifa(minutos: int, tipo_vehiculo: str) -> int:
    """Calcula el valor a pagar, en pesos, por una estadía en el parqueadero.

    Los primeros 15 minutos son gratis. Después se cobra cada hora o fracción
    de hora según el tipo de vehículo, sin superar el tope diario.
    """
    if tipo_vehiculo not in TARIFA_POR_HORA:
        raise ValueError("Tipo de vehículo no válido")
    if not 0 <= minutos <= MINUTOS_MAXIMOS:
        raise ValueError("Los minutos deben estar entre 0 y 1440")

    if minutos <= MINUTOS_DE_GRACIA:
        return 0

    horas_cobradas = math.ceil(minutos / 60)
    valor = horas_cobradas * TARIFA_POR_HORA[tipo_vehiculo]
    return min(valor, TOPE_DIARIO[tipo_vehiculo])