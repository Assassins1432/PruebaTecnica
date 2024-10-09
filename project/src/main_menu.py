import os
from Ejercicios import fibonacci, gcd, palindrome, sort_numbers, to_uppercase


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
        print("1. Calcular Fibonacci")
        print("2. Convertir cadena a mayúsculas")
        print("3. Ordenar lista de números")
        print("4. Verificar si una cadena es un palíndromo")
        print("5. Calcular el MCD de dos números")
        print("6. Salir")

        try:
            choice = int(input("Ingrese su elección (1-6): "))
            if choice == 1:
                fibonacci.main()
            elif choice == 2:
                to_uppercase.main()
            elif choice == 3:
                sort_numbers.main()
            elif choice == 4:
                palindrome.main()
            elif choice == 5:
                gcd.main()
            elif choice == 6:
                print("Saliendo...")
                break
            else:
                clear_terminal()
                print("Opción no válida. Por favor, ingrese un número entre 1 y 6.")
        except ValueError as e:
            clear_terminal()
            print(f"Error: {e}. Por favor, ingrese un número entero válido.")


if __name__ == "__main__":
    main_menu()
