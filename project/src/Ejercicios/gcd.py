def gcd(number1, number2):
    """
    Encuentra el máximo común divisor (MCD) de dos números.

    Args:
        number1 (int): El primer número.
        number2 (int): El segundo número.

    Returns:
        int: El MCD de los dos números.
    """
    while number2:
        number1, number2 = number2, number1 % number2
    return number1


def main():
    """
    Función principal para interactuar con el usuario.
    """
    while True:
        user_input1 = input("Ingrese el primer número (o 'salir' para terminar): ")
        if user_input1.lower() == "salir":
            print("Saliendo...")
            break
        user_input2 = input("Ingrese el segundo número (o 'salir' para terminar): ")
        if user_input2.lower() == "salir":
            print("Saliendo...")
            break
        try:
            if not user_input1.strip() or not user_input2.strip():
                raise ValueError("Las entradas no pueden estar vacías.")
            number1 = int(user_input1)
            number2 = int(user_input2)
            result = gcd(number1, number2)
            print(f"El MCD de {number1} y {number2} es {result}.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese números enteros válidos.")


if __name__ == "__main__":
    main()
