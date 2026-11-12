"""Descuentos para clientes del parqueadero."""


def aplicar_descuento(valor: int, tipo_cliente: str) -> int:
    if tipo_cliente == "ninguno":
        return valor
    return 2700
