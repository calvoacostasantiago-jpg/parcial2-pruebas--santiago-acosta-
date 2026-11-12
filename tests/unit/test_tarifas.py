
"""Pruebas unitarias iniciales de calcular_tarifa. Están incompletas a propósito."""

import pytest

from parqueadero.tarifas import calcular_tarifa


def test_carro_con_una_hora_y_un_minuto_paga_dos_horas():
    assert calcular_tarifa(61, "carro") == 6000


def test_moto_con_media_hora_paga_una_hora():
    assert calcular_tarifa(30, "moto") == 1500


def test_rechaza_un_tipo_de_vehiculo_desconocido():
    with pytest.raises(ValueError, match="Tipo de vehículo no válido"):
        calcular_tarifa(30, "bicicleta")