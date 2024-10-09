from project.src.Ejercicios.sort_numbers import sort_numbers


def test_sort_numbers():
    assert sort_numbers([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
    assert sort_numbers([5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8]
    assert sort_numbers([]) == []
    assert sort_numbers([1]) == [1]
