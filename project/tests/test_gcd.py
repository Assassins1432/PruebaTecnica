from project.src.Ejercicios.gcd import gcd


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(101, 103) == 1
    assert gcd(0, 5) == 5
