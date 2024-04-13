import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from model.automata_module.ndfa_classification import *

object = Classification()

# Test cases for spam classification
@pytest.mark.parametrize("text, rank", [
    ("oferta", 1),
    ("OFerTa", 1),
    ("Suscripción", 1),
    ("susCRIpción", 1),
])
def test(text, rank):
    df = object.execute((text)).loc[0, "SPAM"]
    assert df ==  rank

# Test cases for work classification
@pytest.mark.parametrize("text, rank", [
    ("reporte de progreso", 1),
    ("reunión de equipo", 1),
    ("asignación de tareas", 1)
])
def test(text, rank):
    df = object.execute((text)).loc[0, "TRABAJO"]
    assert df ==  rank

# Test cases for security classification
@pytest.mark.parametrize("text, rank", [
    ("código de autenticación", 2),
    ("clave de ACCeso", 1),
    ("autenticación", 1),
    ("confirmación de identidad", 1),
])
def test(text, rank):
    df = object.execute((text)).loc[0, "SEGURIDAD"]
    assert df ==  rank

# Test cases for text classification
@pytest.mark.parametrize("text, rank", [
    ("Durante la reunión de equipo, se discutió el progreso del proyecto y se asignaron nuevas tareas. Además, se revisaron los protocolos de autenticación y se enfatizó la importancia de mantener segura la clave de acceso.", [1, 2, 0, 1])
])
def test(text, rank):
    df = object.execute((text)).loc[0, "TRABAJO"]
    assert df ==  rank[0]
    df = object.execute((text)).loc[0, "SEGURIDAD"]
    assert df ==  rank[1]
    df = object.execute((text)).loc[0, "SPAM"]
    assert df ==  rank[2]
    df = object.execute((text)).loc[0, "OTRO"]
    assert df ==  rank[3]