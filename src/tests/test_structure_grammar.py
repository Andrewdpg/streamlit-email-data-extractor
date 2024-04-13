import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from model.grammar_module.structure_grammar import *

SAMPLE_EMAIL_1 = """
From: sender@example.com
To: recipient@example.com
Subject: Correo de Prueba
Date: Mon, 12 Apr 2024 10:00:00 +0000
Message-ID: <12345@example.com>

--boundary
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

Este es el cuerpo en texto plano.

--boundary
Content-Type: text/html; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

<html><body>Este es el cuerpo en HTML.</body></html>
--boundary--
"""

SAMPLE_EMAIL_2 = """
From: sender@example.com
To: recipient@example.com
Subject: Correo de Prueba 2
Date: Tue, 13 Apr 2024 10:00:00 +0000
Message-ID: <67890@example.com>

--boundary
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: quoted-printable

Este es otro cuerpo en texto plano.

--boundary--
"""

@pytest.mark.parametrize("email, expected", [
    (SAMPLE_EMAIL_1, True),
    ("Invalid email content", False)
])
def test_validate_structure(email, expected):
    assert (validate_structure(email) is not None) == expected

@pytest.mark.parametrize("email, body_type, expected", [
    (SAMPLE_EMAIL_1, "text", "Este es el cuerpo en texto plano."),
    (SAMPLE_EMAIL_1, "html", "<html><body>Este es el cuerpo en HTML.</body></html>"),
    (SAMPLE_EMAIL_1, "invalid", ValueError),
])
def test_get_body(email, body_type, expected):
    if body_type == "invalid":
        with pytest.raises(expected):
            get_body(email, body_type)
    else:
        assert expected in get_body(email, body_type)

@pytest.mark.parametrize("camps, expected", [
    (["From: sender@example.com", "To: recipient@example.com", "Subject: Correo de Prueba", "Date: Mon, 12 Apr 2024 10:00:00 +0000", "Message-ID: <12345@example.com>"], 
    {"FROM": "sender@example.com", "TO": "recipient@example.com", "SUBJECT": "Correo de Prueba", "DATE": "Mon, 12 Apr 2024 10:00:00 +0000", "ID": "<12345@example.com>"})
])
def test_get_email_metadata(camps, expected):
    assert get_email_metadata(camps) == expected

@pytest.mark.parametrize("email, expected", [
    (SAMPLE_EMAIL_1, True),
    ("Invalid email content", False)
])
def test_parse_email(email, expected):
    assert (parse_email(email) is not None) == expected

@pytest.mark.parametrize("emails, expected", [
    ([SAMPLE_EMAIL_1, SAMPLE_EMAIL_2], 2),
    ([""], 0)
])
def parse_emails(emails: list):
    parsed_emails = {}
    for email in emails:
        parsed_email = parse_email(email)
        if parsed_email is not None and "META" in parsed_email and "ID" in parsed_email["META"]:
            parsed_emails[parsed_email["META"]["ID"]] = parsed_email
    return parsed_emails

def test_parse_emails_empty_email():
    emails = [""]
    parsed_emails = parse_emails(emails)
    assert parsed_emails == {}