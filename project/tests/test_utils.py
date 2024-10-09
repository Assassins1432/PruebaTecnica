# test_utils.py
"""
Este módulo contiene pruebas para el módulo utils.
"""

from src.utils import add


def test_add():
    """
    Prueba la función add.
    """
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
