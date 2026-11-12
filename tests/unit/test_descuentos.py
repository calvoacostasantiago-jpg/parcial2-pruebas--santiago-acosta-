"""Pruebas de descuentos construidas con ciclos rojo, verde y refactor."""

from parqueadero.descuentos import aplicar_descuento


def test_cliente_frecuente_recibe_diez_por_ciento_de_descuento():
    assert aplicar_descuento(3000, "frecuente") == 2700
