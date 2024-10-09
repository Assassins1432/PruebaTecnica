import os

from PruebaTecnica import balanced_expression, chess, draw_square, rock_paper_scissors


def clear_terminal():
    """
    Limpia la terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


def main_menu():
    """
    Muestra el menú principal y permite al usuario seleccionar una opción.
    """
    while True:
        print("\nSeleccione una opción:")
        print("1. Calcular movimiento de peón en ajedrez")
        print("2. Dibujar un cuadrado con 'O'")
        print("3. Verificar si una expresión está equilibrada")
        print("4. Determinar el ganador de Piedra, Papel o Tijera")
        print("5. Salir")

        try:
            choice = int(input("Ingrese su elección (1-5): "))
            if choice == 1:
                chess.main()
            elif choice == 2:
                draw_square.main()
            elif choice == 3:
                balanced_expression.main()
            elif choice == 4:
                rock_paper_scissors.main()
            elif choice == 5:
                print("Saliendo...")
                break
            else:
                raise ValueError(
                    "Opción no válida. Por favor, ingrese un número entre 1 y 5."
                )
        except ValueError as e:
            clear_terminal()
            print(f"Error: {e}. Por favor, ingrese un número entero válido.")
        except Exception as e:
            clear_terminal()
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main_menu()
