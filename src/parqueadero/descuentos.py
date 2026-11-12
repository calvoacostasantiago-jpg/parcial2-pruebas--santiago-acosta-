"""Descuentos para clientes del parqueadero."""


def aplicar_descuento(valor: int, tipo_cliente: str) -> int:
    if tipo_cliente not in ("ninguno", "frecuente", "convenio"):
        raise ValueError("Tipo de cliente no válido")
    if valor < 0:
        raise ValueError("El valor no puede ser negativo")
    if valor == 0:
        return 0
    if tipo_cliente == "ninguno":
        return valor
    if tipo_cliente == "convenio":
        return valor * 80 // 100
    return valor * 90 // 100
