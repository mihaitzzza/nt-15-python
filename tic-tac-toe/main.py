from helpers import (
    get_current_player,
    get_valid_choice,
    get_options,
    fill_choice,
    is_win,
)


def main():
    board = [
        [None, None, None],  # 1, 2, 3
        [None, None, None],  # 4, 5, 6
        [None, None, None]  # 7, 8, 9
    ]

    winner = None
    current_step = 0

    while current_step < 9:
        player = get_current_player(current_step)
        print(f"Player {player} is your turn.")

        available_options = get_options(board)
        print("Available options: ", available_options)

        choice = get_valid_choice(available_options)
        print(f"Player {player} chose: {choice}")

        board = fill_choice(board, player, choice)
        is_game_won = is_win(board)

        if is_game_won:
            winner = player
            break

        current_step += 1

    if winner:
        print(f"Congrats, Player {winner}! You won the game")
    else:
        print("Game ended as a draw.")


if __name__ == "__main__":
    main()
