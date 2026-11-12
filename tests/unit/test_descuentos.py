"""Pruebas de descuentos construidas con ciclos rojo, verde y refactor."""

from parqueadero.descuentos import aplicar_descuento


def test_cliente_frecuente_recibe_diez_por_ciento_de_descuento():
    assert aplicar_descuento(3000, "frecuente") == 2700


def test_cliente_sin_beneficio_paga_el_valor_completo():
    assert aplicar_descuento(3000, "ninguno") == 3000


def test_cliente_con_convenio_recibe_veinte_por_ciento_de_descuento():
    assert aplicar_descuento(25000, "convenio") == 20000
