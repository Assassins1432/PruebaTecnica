import os


def clear_terminal():
    """
    Limpia la terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


def draw_square(side_length):
    """
    Dibuja un cuadrado utilizando la letra 'O', con el centro vacío.

    Args:
        side_length (int): La longitud del lado del cuadrado.
    """
    if side_length <= 0:
        raise ValueError("La longitud del lado debe ser un número positivo.")

    # Dibuja el cuadrado con centro vacío
    for row in range(side_length):
        if row == 0 or row == side_length - 1:  # Primera y última fila completas de 'O'
            print("O" * side_length)
        else:
            print(
                "O" + " " * (side_length - 2) + "O"
            )  # Filas intermedias con bordes de 'O' y centro vacío


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        try:
            user_input = input(
                "Ingrese la longitud del lado del cuadrado (o 'salir' para terminar): "
            )
            if user_input.lower() == "salir":
                print("Saliendo...")
                break
            side_length = int(user_input)
            clear_terminal()
            draw_square(side_length)
        except ValueError as e:
            clear_terminal()
            print(f"Error: {e}. Por favor, ingrese un número entero positivo.")
        except Exception as e:
            clear_terminal()
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
