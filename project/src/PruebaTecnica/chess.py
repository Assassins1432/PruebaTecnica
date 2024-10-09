import os


def clear_terminal():
    """
    Limpia la terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


def is_valid_move(board, start_position, end_position):
    """
    Verifica si el movimiento de un peón es válido.

    Args:
        board (list): El tablero de ajedrez.
        start_position (tuple): La posición inicial del peón.
        end_position (tuple): La posición final del peón.

    Returns:
        tuple: (bool, str) Indica si el movimiento es válido y un mensaje.
    """
    start_row, start_col = start_position
    end_row, end_col = end_position
    piece = board[start_row][start_col]

    # Verificar que el peón sea válido (B para blanco y N para negro)
    if piece not in ["B", "N"]:
        return False, "No hay un peón en la posición inicial."

    # Direcciones: los peones blancos se mueven hacia arriba (B), los negros hacia abajo (N)
    direction = -1 if piece == "B" else 1
    start_row_valid = 6 if piece == "B" else 1

    # Movimiento hacia adelante
    if start_col == end_col:
        # Primer movimiento (puede moverse dos casillas hacia adelante)
        if (
            start_row == start_row_valid
            and end_row == start_row + 2 * direction
            and board[end_row][end_col] == ""
            and board[start_row + direction][end_col] == ""
        ):
            return True, "Movimiento válido de dos casillas."
        # Movimiento normal de una casilla hacia adelante
        elif end_row == start_row + direction and board[end_row][end_col] == "":
            return True, "Movimiento válido de una casilla."
    # Captura en diagonal
    elif (
        abs(start_col - end_col) == 1
        and end_row == start_row + direction
        and board[end_row][end_col] != ""
        and board[end_row][end_col].lower() != piece.lower()
    ):
        return True, "Peón captura a otro peón."

    return False, "Movimiento no válido."


def move_pawn(board, start_position, end_position):
    """
    Mueve un peón en el tablero de ajedrez.

    Args:
        board (list): El tablero de ajedrez.
        start_position (tuple): La posición inicial del peón.
        end_position (tuple): La posición final del peón.

    Returns:
        tuple: (list, str) El tablero actualizado y un mensaje.
    """
    is_valid, message = is_valid_move(board, start_position, end_position)
    if is_valid:
        start_row, start_col = start_position
        end_row, end_col = end_position
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = ""
    return board, message


def print_board(board):
    """
    Imprime el tablero de ajedrez.

    Args:
        board (list): El tablero de ajedrez.
    """
    for row in board:
        print(" ".join(row if row else "." for row in row))


def main():
    """
    Función principal para interactuar con el usuario.
    """
    board = [
        ["N", "N", "N", "N", "N", "N", "N", "N"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["B", "B", "B", "B", "B", "B", "B", "B"],
        ["", "", "", "", "", "", "", ""],
    ]

    while True:
        try:
            user_input = input(
                "Ingrese la posición inicial y final del peón (ej. '6,0 4,0'), 'ejemplo' para usar un ejemplo predefinido, o 'salir' para terminar: "
            )
            if user_input.lower() == "salir":
                print("Saliendo...")
                break
            elif user_input.lower() == "ejemplo":
                start_position = (6, 0)
                end_position = (4, 0)
            else:
                start_position, end_position = user_input.split()
                start_position = tuple(map(int, start_position.split(",")))
                end_position = tuple(map(int, end_position.split(",")))

            board, message = move_pawn(board, start_position, end_position)
            clear_terminal()
            print(message)
            print_board(board)
        except ValueError as e:
            clear_terminal()
            print(f"Error: {e}. Por favor, ingrese posiciones válidas.")
        except Exception as e:
            clear_terminal()
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
