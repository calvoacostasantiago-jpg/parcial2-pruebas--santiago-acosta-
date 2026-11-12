"""Pruebas de descuentos construidas con ciclos rojo, verde y refactor."""

import pytest

from parqueadero.descuentos import aplicar_descuento


def test_cliente_frecuente_recibe_diez_por_ciento_de_descuento():
    assert aplicar_descuento(3000, "frecuente") == 2700


def test_cliente_sin_beneficio_paga_el_valor_completo():
    assert aplicar_descuento(3000, "ninguno") == 3000


def test_cliente_con_convenio_recibe_veinte_por_ciento_de_descuento():
    assert aplicar_descuento(25000, "convenio") == 20000


@pytest.mark.parametrize("tipo_cliente", ["ninguno", "frecuente", "convenio"])
def test_valor_cero_se_mantiene_en_cero(tipo_cliente):
    assert aplicar_descuento(0, tipo_cliente) == 0


@pytest.mark.parametrize(
    ("valor", "tipo_cliente", "valor_esperado"),
    [
        (1999, "frecuente", 1799),
        (1999, "convenio", 1599),
        (2999, "frecuente", 2699),
        (2999, "convenio", 2399),
        (1, "frecuente", 0),
        (1, "convenio", 0),
        (1, "ninguno", 1),
        (10_000_000_000_000_010, "frecuente", 9_000_000_000_000_009),
        (10_000_000_000_000_010, "convenio", 8_000_000_000_000_008),
    ],
)
def test_resultado_se_redondea_hacia_abajo_al_peso_entero(valor, tipo_cliente, valor_esperado):
    assert aplicar_descuento(valor, tipo_cliente) == valor_esperado


@pytest.mark.parametrize("tipo_cliente", ["ninguno", "frecuente", "convenio"])
@pytest.mark.parametrize("valor", [-1, -3000])
def test_rechaza_un_valor_negativo(valor, tipo_cliente):
    with pytest.raises(ValueError, match="^El valor no puede ser negativo$"):
        aplicar_descuento(valor, tipo_cliente)
