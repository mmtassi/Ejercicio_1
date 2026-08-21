from solucion.prestamo import Prestamo


def test_prestamo_en_termino():
    prestamo = Prestamo("El Quijote", "Juan Perez", 3)

    assert prestamo.esta_vencido() is False
    assert prestamo.dias_de_retraso() == 0
    assert prestamo.resumen() == "El Quijote - Juan Perez - en término"


def test_prestamo_vencido():
    prestamo = Prestamo("1984", "Maria Garcia", 10)

    assert prestamo.esta_vencido() is True
    assert prestamo.dias_de_retraso() == 3
    assert prestamo.resumen() == "1984 - Maria Garcia - vencido (3 días)"


def test_prestamo_limite_siete_dias():
    prestamo = Prestamo("Cien años de soledad", "Pedro Martinez", 7)

    assert prestamo.esta_vencido() is False
    assert prestamo.dias_de_retraso() == 0
    assert prestamo.resumen() == "Cien años de soledad - Pedro Martinez - en término"


def test_dias_invalidos_lanzan_value_error():
    try:
        Prestamo("Dorian Gray", "Ana Lopez", "4")
        assert False
    except ValueError:
        assert True