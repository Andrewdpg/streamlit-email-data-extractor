import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from model.transducers_module.transducers import *


# Test cases for text with only one word
@pytest.mark.parametrize("raw_text, normalized_text", [
    ("ejemplo", "ejemplo"),
    ("holA", "holA"),
])
def test(raw_text, normalized_text):
    assert translate(raw_text) ==  normalized_text

# Test cases for text with multiple words
@pytest.mark.parametrize("raw_text, normalized_text", [
    ("""Esto es un texto de ejemplo
    con 
     saltos de linea 
     y todo""", """Esto es un texto de ejemplo
    con 
     saltos de linea 
     y todo"""),
    ("""Hola
    Mundo""", """Hola
    Mundo"""),
])
def test(raw_text, normalized_text):
    assert translate(raw_text) ==  normalized_text

special_characters = {
    "á": "=C3=A1",
    "é": "=C3=A9",
    "í": "=C3=AD",
    "ó": "=C3=B3",
    "ú": "=C3=BA",
    "Á": "=C3=81",
    "É": "=C3=89",
    "Í": "=C3=8D",
    "Ó": "=C3=93",
    "Ú": "=C3=9A",
}

# Test cases for text with special characters
@pytest.mark.parametrize("raw_text, normalized_text", [
    (special_characters["á"], "á"),
    (special_characters["é"], "é"),
    (special_characters["í"], "í"),
    (special_characters["ó"], "ó"),
    (special_characters["ú"], "ú"),
    (special_characters["Á"], "Á"),
    (special_characters["É"], "É"),
    (special_characters["Í"], "Í"),
    (special_characters["Ó"], "Ó"),
    (special_characters["Ú"], "Ú"),
])
def test(raw_text, normalized_text):
    assert translate(raw_text) ==  normalized_text

# Test cases for text with special characters and multiple words
@pytest.mark.parametrize("raw_text, normalized_text", [
    (f"""Esto es un texto de ejemplo con {special_characters["á"]} y todo""", f"""Esto es un texto de ejemplo con á y todo"""),
    (f"""Hola Mundo \n{special_characters["é"]}""", f"""Hola Mundo \né""")
])
def test(raw_text, normalized_text):
    assert translate(raw_text) ==  normalized_text