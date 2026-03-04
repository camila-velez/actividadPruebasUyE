
# TODO: Escribe pruebas unitarias para es_palindromo y suma.
# Sugerencias:
# - "radar" -> True, "anita lava la tina" -> True, "python" -> False, "" -> True, "Radar" -> True
# - suma(2,3) -> 5; suma(0,5) -> 5; suma(-2,3) -> 1

from python_app.palindromo import es_palindromo


def test_palindromo_basico():
    assert es_palindromo("radar") is True


def test_palindromo_mayusculas():
    assert es_palindromo("Radar") is True


def test_palindromo_frase():
    assert es_palindromo("anita lava la tina") is True


def test_no_palindromo():
    assert es_palindromo("python") is False


def test_palindromo_vacio():
    assert es_palindromo("") is True
