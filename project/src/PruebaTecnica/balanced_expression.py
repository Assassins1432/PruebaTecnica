import os


def clear_terminal():
    """
    Limpia la terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


def is_balanced(expression):
    """
    Verifica si una expresión con paréntesis, llaves y corchetes está equilibrada.

    Args:
        expression (str): La expresión a verificar.

    Returns:
        bool: True si la expresión está equilibrada, False en caso contrario.
    """
    stack = []
    matching_brackets = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if stack == [] or matching_brackets[char] != stack.pop():
                return False

    return stack == []


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        try:
            user_input = input(
                "Ingrese una expresión para verificar si está equilibrada (o 'salir' para terminar): "
            )
            if user_input.lower() == "salir":
                print("Saliendo...")
                break
            clear_terminal()
            if is_balanced(user_input):
                print("La expresión está equilibrada.")
            else:
                print("La expresión no está equilibrada.")
        except Exception as e:
            clear_terminal()
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
