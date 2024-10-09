def fibonacci(position):
    """
    Calcula el n-ésimo número en la serie de Fibonacci.

    La serie de Fibonacci se define como:
        F(0) = 0
        F(1) = 1
        F(n) = F(n-1) + F(n-2) para n >= 2

    Esta función utiliza un enfoque iterativo para calcular el n-ésimo número,
    lo que es eficiente en términos de tiempo y espacio.

    Args:
        position (int): La posición en la serie de Fibonacci.

    Returns:
        int: El n-ésimo número en la serie de Fibonacci.
    """
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        previous, current = 0, 1
        for _ in range(2, position + 1):
            previous, current = current, previous + current
        return current


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        user_input = input(
            "Ingrese la posición en la serie de Fibonacci (o 'salir' para terminar): "
        )
        if user_input.lower() == "salir":
            print("Saliendo...")
            break
        try:
            position = int(user_input)
            if position < 0:
                raise ValueError("La posición no puede ser negativa.")
            result = fibonacci(position)
            print(
                f"El número en la posición {position} de la serie de Fibonacci es {result}."
            )
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número entero válido.")


if __name__ == "__main__":
    main()
