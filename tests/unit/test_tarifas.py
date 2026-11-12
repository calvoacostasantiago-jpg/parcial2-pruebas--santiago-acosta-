"""Particiones de equivalencia y valores límite de las tarifas."""

import pytest

from parqueadero.tarifas import calcular_tarifa


def test_carro_con_una_hora_y_un_minuto_paga_dos_horas():
    assert calcular_tarifa(61, "carro") == 6000


def test_moto_con_media_hora_paga_una_hora():
    assert calcular_tarifa(30, "moto") == 1500


def test_rechaza_un_tipo_de_vehiculo_desconocido():
    with pytest.raises(ValueError, match="Tipo de vehículo no válido"):
        calcular_tarifa(30, "bicicleta")


@pytest.mark.parametrize("tipo_vehiculo", ["carro", "moto"])
@pytest.mark.parametrize("minutos", [0, 1, 14, 15])
def test_estadia_dentro_de_la_gracia_no_paga(minutos, tipo_vehiculo):
    assert calcular_tarifa(minutos, tipo_vehiculo) == 0


@pytest.mark.parametrize(
    ("tipo_vehiculo", "minutos", "valor_esperado"),
    [
        ("carro", 16, 3000),
        ("carro", 59, 3000),
        ("carro", 60, 3000),
        ("carro", 61, 6000),
        ("carro", 119, 6000),
        ("carro", 120, 6000),
        ("carro", 121, 9000),
        ("moto", 16, 1500),
        ("moto", 59, 1500),
        ("moto", 60, 1500),
        ("moto", 61, 3000),
        ("moto", 119, 3000),
        ("moto", 120, 3000),
        ("moto", 121, 4500),
    ],
)
def test_cobra_cada_hora_o_fraccion_despues_de_la_gracia(tipo_vehiculo, minutos, valor_esperado):
    assert calcular_tarifa(minutos, tipo_vehiculo) == valor_esperado


@pytest.mark.parametrize(
    ("tipo_vehiculo", "minutos", "valor_esperado"),
    [
        ("carro", 479, 24000),
        ("carro", 480, 24000),
        ("carro", 481, 25000),
        ("carro", 482, 25000),
        ("carro", 540, 25000),
        ("carro", 541, 25000),
        ("moto", 419, 10500),
        ("moto", 420, 10500),
        ("moto", 421, 12000),
        ("moto", 422, 12000),
        ("moto", 480, 12000),
        ("moto", 481, 12000),
    ],
)
def test_cobro_alcanza_el_tope_diario_y_no_lo_supera(tipo_vehiculo, minutos, valor_esperado):
    assert calcular_tarifa(minutos, tipo_vehiculo) == valor_esperado


@pytest.mark.parametrize(("tipo_vehiculo", "tope"), [("carro", 25000), ("moto", 12000)])
@pytest.mark.parametrize("minutos", [1439, 1440])
def test_acepta_el_limite_de_un_dia_y_cobra_el_tope(minutos, tipo_vehiculo, tope):
    assert calcular_tarifa(minutos, tipo_vehiculo) == tope


@pytest.mark.parametrize("tipo_vehiculo", ["carro", "moto"])
@pytest.mark.parametrize("minutos", [-60, -1, 1441, 1500])
def test_rechaza_minutos_fuera_del_rango_permitido(minutos, tipo_vehiculo):
    with pytest.raises(ValueError, match="^Los minutos deben estar entre 0 y 1440$"):
        calcular_tarifa(minutos, tipo_vehiculo)


@pytest.mark.parametrize("tipo_vehiculo", ["carro", "moto"])
@pytest.mark.parametrize("minutos", [15.5, 60.0, "60", None, True, False])
def test_rechaza_minutos_que_no_son_enteros(minutos, tipo_vehiculo):
    with pytest.raises(ValueError, match="^Los minutos deben estar entre 0 y 1440$"):
        calcular_tarifa(minutos, tipo_vehiculo)


@pytest.mark.parametrize("tipo_vehiculo", ["camion", "bus", "Carro", "MOTO", "", None, 0])
def test_rechaza_tipos_distintos_de_carro_y_moto(tipo_vehiculo):
    with pytest.raises(ValueError, match="^Tipo de vehículo no válido$"):
        calcular_tarifa(30, tipo_vehiculo)
