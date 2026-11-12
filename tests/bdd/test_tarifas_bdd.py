"""Pasos de negocio para ejecutar los escenarios de tarifas y descuentos."""

from pytest_bdd import given, parsers, scenarios, then, when

from parqueadero.descuentos import aplicar_descuento
from parqueadero.tarifas import calcular_tarifa

scenarios("features/tarifas.feature")


@given(
    parsers.parse('que un vehículo de tipo "{tipo_vehiculo}" permaneció {minutos:d} minutos'),
    target_fixture="estadia",
)
def registrar_estadia(tipo_vehiculo, minutos):
    return tipo_vehiculo, minutos


@given(parsers.parse('que el cliente es "{tipo_cliente}"'), target_fixture="tipo_cliente")
def identificar_cliente(tipo_cliente):
    return tipo_cliente


@given(
    parsers.parse("que el cobro antes del descuento es {valor:d} pesos"),
    target_fixture="cobro",
)
def registrar_cobro_antes_del_descuento(valor):
    return {"valor": valor}


@when("se calcula el cobro de su estadía", target_fixture="cobro")
def calcular_cobro_de_estadia(estadia):
    tipo_vehiculo, minutos = estadia
    return {"valor": calcular_tarifa(minutos, tipo_vehiculo)}


@when("se aplica el descuento del cliente")
def aplicar_beneficio_del_cliente(cobro, tipo_cliente):
    cobro["valor"] = aplicar_descuento(cobro["valor"], tipo_cliente)


@then(parsers.parse("debe pagar {valor_esperado:d} pesos"))
def comprobar_valor_a_pagar(cobro, valor_esperado):
    assert cobro["valor"] == valor_esperado
