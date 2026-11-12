"""Resumen de vehículos y recaudo diario del parqueadero."""

from parqueadero.tarifas import calcular_tarifa


def resumen(registros: list[tuple[str, int]]) -> dict[str, int]:
    """Cuenta los vehículos y acumula el recaudo usando las tarifas vigentes."""
    resultado = {"carro": 0, "moto": 0, "total_recaudado": 0}
    for tipo_vehiculo, minutos in registros:
        resultado[tipo_vehiculo] += 1
        resultado["total_recaudado"] += calcular_tarifa(minutos, tipo_vehiculo)
    return resultado
