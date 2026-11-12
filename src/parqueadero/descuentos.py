"""Descuentos para clientes del parqueadero."""

PORCENTAJE_DESCUENTO = {"ninguno": 0, "frecuente": 10, "convenio": 20}


def aplicar_descuento(valor: int, tipo_cliente: str) -> int:
    """Devuelve el valor con descuento, redondeado hacia abajo al peso entero."""
    if tipo_cliente not in PORCENTAJE_DESCUENTO:
        raise ValueError("Tipo de cliente no válido")
    if valor < 0:
        raise ValueError("El valor no puede ser negativo")

    porcentaje_a_pagar = 100 - PORCENTAJE_DESCUENTO[tipo_cliente]
    return valor * porcentaje_a_pagar // 100
