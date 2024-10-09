def sort_numbers(numbers):
    """
    Ordena una lista de números en orden ascendente.

    Args:
        numbers (list): La lista de números a ordenar.

    Returns:
        list: La lista de números ordenada.
    """
    return sorted(numbers)


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        user_input = input(
            "Ingrese una lista de números separados por comas (o 'salir' para terminar): "
        )
        if user_input.lower() == "salir":
            print("Saliendo...")
            break
        try:
            if not user_input.strip():
                raise ValueError("La entrada no puede estar vacía.")
            number_list = [int(num.strip()) for num in user_input.split(",")]
            result = sort_numbers(number_list)
            print(f"La lista de números ordenada es: {result}")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese una lista de números válida.")


if __name__ == "__main__":
    main()
