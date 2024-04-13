import os
import re
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

import pytest

from model.regex_module.data_parser import (parse_email_address,
                                            parse_email_address_list)
from model.regex_module.info_extractor import *


# Test cases for the extract_tasks function
@pytest.mark.parametrize("email, expected_tasks", [
    ("Tareas pendientes:\n1. Finalizar el informe trimestral antes del 30/06/2023.\n2. Preparar la presentación para el evento de lanzamiento (https://ejemplo.com/presentacion).\n3. Coordinar con el equipo de marketing la campaña publicitaria (https://marketing.ejemplo.com).\n\n",["Finalizar el informe trimestral antes del 30/06/2023.","Preparar la presentación para el evento de lanzamiento (https://ejemplo.com/presentacion).","Coordinar con el equipo de marketing la campaña publicitaria (https://marketing.ejemplo.com).",],),
    ("Necesito que hagas la presentación para mañana.",["la presentación para mañana"],),
    ("1. Terminar el proyecto\n2. Revisar la presentación",None,),
    ("Tareas:\n1. Revisar informe\n2. Enviar correo a cliente\n\n",["Revisar informe", "Enviar correo a cliente"],),
])
def test_extract_tasks(email, expected_tasks):
    assert expected_tasks == extract_tasks(email)

# Test cases for the extract_links function
@pytest.mark.parametrize("email, expected_links", [
    ("Aquí tienes el enlace: https://www.example.com", ["https://www.example.com"]),
    ("No hay enlaces en este correo.", None),
    ("Puedes descargar el archivo desde aquí: ftp://ftp.download.com, si tienes alguna duda, contactanos mediante nuestro canal de atención en canal-atencion.com", ["ftp://ftp.download.com", "canal-atencion.com"]),
])
def test_extract_links(email, expected_links):
    assert extract_links(email) == expected_links

# Test cases for the extract_events function
@pytest.mark.parametrize("email, expected_events", [
    ("Tendremos una reunión el 10/02/2024 a las 15:00 en la sala de conferencias. No faltar.", ["Reunión el 10/02/2024 a las 15:00 en la sala de conferencias."]),
    ("Evento el 15/03/2024 a las 9:30", ["Evento el 15/03/2024 a las 9:30"]),
    ("Quisiera que tuvieramos una cita el 20-04-2024 a las 14:00 en el café. luego del evento en el salón 404E", ["Cita el 20-04-2024 a las 14:00 en el café.", "Evento en el salón 404e"]),
    ("Evento en la sede central", ["Evento en la sede central"])
])
def test_extract_events(email, expected_events):
    assert extract_events(email) == expected_events

# Test cases for the extract_dates function
@pytest.mark.parametrize("email, expected_dates", [
    ("La fecha límite es el 25/04/2024.", [datetime(2024, 4, 25).date()]),
    ("Recordatorio: la reunión es el 10-05-2024.", [datetime(2024, 5, 10).date()]),
    ("El evento será el 15 de Marzo 2024.", ["15 de Marzo 2024"]),
    ("No hay fechas en este correo.", None)
])
def test_extract_dates(email, expected_dates):
    assert extract_dates(email) == expected_dates

# Test cases for the extract_physical_addresses function
@pytest.mark.parametrize("email, expected_addresses", [
    ("La dirección es Calle 123, piso 5.", ["Calle 123, piso 5"]),
    ("No se proporcionó ninguna dirección.", None),
    ("La oficina está en la Carrera 4b 75-19.", ["Carrera 4b 75-19"])
])
def test_extract_physical_addresses(email, expected_addresses):
    assert extract_physical_addresses(email) == expected_addresses

# Test cases for the extract_info function
@pytest.mark.parametrize("email, expected_info", [
    ("Hola Andrés, aquí tienes tus tareas pendientes:\n1. Completar informe de ventas\n2. Preparar presentación para reunión.\n\nLa fecha límite es el 25/04/2024. Aquí tienes el enlace para que subas los documentos necesarios: https://www.example.com", {"tasks": ["Completar informe de ventas", "Preparar presentación para reunión."], "links": ["https://www.example.com"], "events": ["Reunión"], "verification_code": None, "greetings": ["Hola"], "dates": [datetime(2024, 4, 25).date()], "physical_addresses": None}),
])
def test_extract_info(email, expected_info):
    assert extract_info(email) == expected_info

# Test cases for parse_email_address function
@pytest.mark.parametrize("address, expected_result", [
    ("=?UTF-8?Q?John_Doe?= <john@example.com>", ("John_Doe", "john@example.com")),
    ("john@example.com", (None, "john@example.com")),
    ("=?UTF-8?Q?Jane_Doe?= <jane@example.com>", ("Jane_Doe", "jane@example.com")),
    ("=?UTF-8?Q?Juan_P=C3=A9rez?= <juan@example.com>", ("Juan_Pérez", "juan@example.com")),
])
def test_parse_email_address(address, expected_result):
    assert parse_email_address(address) == expected_result

# Test cases for parse_email_address_list function
@pytest.mark.parametrize("email_list, expected_result", [
    ("=?UTF-8?Q?John_Doe?= <john@example.com>, =?UTF-8?Q?Jane_Doe?= <jane@example.com>", [("John_Doe", "john@example.com"), ("Jane_Doe", "jane@example.com")]),
    ("john@example.com, jane@example.com", [(None, "john@example.com"), (None, "jane@example.com")]),
    ("=?UTF-8?Q?John_Doe?= <john@example.com>, =?UTF-8?Q?Juan_P=C3=A9rez?= <juan@example.com>", [("John_Doe", "john@example.com"), ("Juan_Pérez", "juan@example.com")]),
])
def test_parse_email_address_list(email_list, expected_result):
    assert parse_email_address_list(email_list) == expected_result
