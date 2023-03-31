win_options = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


def get_current_player(step: int):
    if step % 2 == 0:
        return "X"

    return "O"


def get_options(board):
    options = []

    for row_index, row in enumerate(board):  # [0, 1, 2]
        for cell_index, cell in enumerate(row):  # [0, 1, 2]
            if cell is None:  # this is an available option!
                options.append(row_index * 3 + cell_index + 1)

    return options


def get_choice(available_choices):
    user_input = input("Pick a value: ")
    user_input = int(user_input)

    if user_input not in available_choices:  # invalid choice!
        raise ValueError()

    return user_input


def get_valid_choice(available_choices):
    while True:
        try:
            choice = get_choice(available_choices)
        except ValueError:
            print("Your choice is not valid.")
            continue

        return choice


def fill_choice(board, player, choice):
    new_board = board.copy()

    real_value = choice - 1
    row_index = real_value // 3
    cell_index = real_value % 3

    new_board[row_index][cell_index] = player

    return new_board


def is_win(board: list):
    """
    Decides if the game is won or not. We don't care who won.
    :param board: The board configuration.
    :return: True/False
    """

    for win_option in win_options:
        cell_1 = board[win_option[0][0]][win_option[0][1]]
        cell_2 = board[win_option[1][0]][win_option[1][1]]
        cell_3 = board[win_option[2][0]][win_option[2][1]]

        # values = [cell_1, cell_2, cell_3]
        # if values.count("X") == 3 or values.count("O") == 3:
        #     return True

        values = {cell_1, cell_2, cell_3}
        if len(values) == 1 and None not in values:
            return True

    return False
