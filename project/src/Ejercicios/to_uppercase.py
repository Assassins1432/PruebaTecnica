def to_uppercase(string):
    """
    Convierte una cadena a mayúsculas.

    Args:
        string (str): La cadena a convertir.

    Returns:
        str: La cadena en mayúsculas.
    """
    if not isinstance(string, str):
        raise ValueError("La entrada debe ser una cadena.")
    return string.upper()


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        user_input = input(
            "Ingrese una cadena para convertir a mayúsculas (o 'salir' para terminar): "
        )
        if user_input.lower() == "salir":
            print("Saliendo...")
            break
        try:
            if not user_input.strip():
                raise ValueError("La entrada no puede estar vacía.")
            result = to_uppercase(user_input)
            print(f"La cadena en mayúsculas es: {result}")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese una cadena válida.")


if __name__ == "__main__":
    main()
