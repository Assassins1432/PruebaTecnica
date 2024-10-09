from project.src.Ejercicios.palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("level") == True
    assert is_palindrome("world") == False
