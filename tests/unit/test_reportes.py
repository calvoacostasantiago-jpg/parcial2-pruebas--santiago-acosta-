"""Pruebas que protegen el comportamiento de resumen durante el refactor."""

from parqueadero.reportes import resumen


def test_resume_los_registros_del_dia():
    registros = [("carro", 10), ("carro", 61), ("moto", 600), ("carro", 1440)]

    resultado = resumen(registros)

    # 0 (gracia) + 6000 (2 horas) + 12000 (tope moto) + 25000 (tope carro)
    assert resultado == {"carro": 3, "moto": 1, "total_recaudado": 43000}


def test_sin_registros_todo_es_cero():
    assert resumen([]) == {"carro": 0, "moto": 0, "total_recaudado": 0}
