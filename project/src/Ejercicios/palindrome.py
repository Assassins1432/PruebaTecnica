def is_palindrome(string):
    """
    Verifica si una cadena es un palíndromo.

    Args:
        string (str): La cadena a verificar.

    Returns:
        bool: True si la cadena es un palíndromo, False en caso contrario.
    """
    if not isinstance(string, str):
        raise ValueError("La entrada debe ser una cadena.")
    return string == string[::-1]


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        user_input = input(
            "Ingrese una cadena para verificar si es un palíndromo (o 'salir' para terminar): "
        )
        if user_input.lower() == "salir":
            print("Saliendo...")
            break
        try:
            if not user_input.strip():
                raise ValueError("La entrada no puede estar vacía.")
            result = is_palindrome(user_input)
            if result:
                print(f"La cadena '{user_input}' es un palíndromo.")
            else:
                print(f"La cadena '{user_input}' no es un palíndromo.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese una cadena válida.")


if __name__ == "__main__":
    main()
