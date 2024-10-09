# test_main.py
"""
Este módulo contiene pruebas para el módulo main.
"""

import pytest
from src.main import main

def test_main(capsys):
    """
    Prueba la función principal.
    """
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hola, mundo!\n"