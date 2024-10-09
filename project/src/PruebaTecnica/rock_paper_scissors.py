import os
import json


def clear_terminal():
    """
    Limpia la terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


def determine_winner(game_data):
    """
    Determina el ganador de un juego de Piedra, Papel o Tijera en una serie de mejor de 5.

    Args:
        game_data (dict): Un diccionario con las jugadas de ambos jugadores. Las jugadas deben ser
                          'R' (Roca), 'P' (Papel) o 'S' (Tijera).

    Returns:
        str: El resultado del juego, indicando el ganador o si hubo empate.
    """
    rules = {"R": "S", "P": "R", "S": "P"}
    player1_wins = 0
    player2_wins = 0

    # Se recorre cada jugada de ambos jugadores
    for player1_move, player2_move in zip(game_data["jugador1"], game_data["jugador2"]):
        if player1_move == player2_move:
            continue  # Empate en esta jugada, no se suma ningún punto.
        elif rules[player1_move] == player2_move:
            player1_wins += 1
        else:
            player2_wins += 1

        # Verificar si alguno de los jugadores ya ganó 3 rondas
        if player1_wins == 3:
            return "Victoria Jugador 1"
        elif player2_wins == 3:
            return "Victoria Jugador 2"

    # Si no hay un ganador tras 5 jugadas, el juego termina en empate o con ventaja mínima
    if player1_wins > player2_wins:
        return "Victoria Jugador 1"
    elif player2_wins > player1_wins:
        return "Victoria Jugador 2"
    else:
        return "Empate"


def main():
    """
    Función principal para interactuar con el usuario.
    Permite introducir las jugadas en formato JSON y determina el ganador.
    """
    while True:
        try:
            user_input = input(
                "Ingrese las jugadas de ambos jugadores en formato JSON (o 'salir' para terminar): "
            )
            if user_input.lower() == "salir":
                print("Saliendo...")
                break

            # Parsear el JSON ingresado por el usuario
            game_data = json.loads(user_input)

            if len(game_data["jugador1"]) != 5 or len(game_data["jugador2"]) != 5:
                raise ValueError("Ambos jugadores deben tener exactamente 5 jugadas.")

            clear_terminal()

            result = determine_winner(game_data)
            print(result)

        except json.JSONDecodeError:
            clear_terminal()
            print(
                "Error: Formato JSON inválido. Asegúrese de ingresar un JSON correctamente formado."
            )
        except KeyError:
            clear_terminal()
            print(
                "Error: El JSON debe contener las claves 'jugador1' y 'jugador2' con 5 jugadas cada uno."
            )
        except ValueError as e:
            clear_terminal()
            print(f"Error: {e}.")
        except Exception as e:
            clear_terminal()
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
