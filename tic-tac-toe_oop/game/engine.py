from game.players import Player
from game.board import Board

WIN_OPTIONS = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


class GameEngine:
    def __init__(self):
        self.__current_step = 0  # name mangling => obj._GameEngine__current_step
        self.__players = [
            Player("X"),
            Player("O")
        ]
        self.__current_player = None
        self.__winner = None
        self.__board = Board()

    @property
    def winner(self):
        return self.__winner

    def __set_current_player(self):
        self.__current_player = self.__players[self.__current_step % 2]
        print(f"Player {self.__current_player} is your turn.")

    def __get_available_options(self):
        return self.__board.get_available_options()

    def is_won(self):
        for win_option in WIN_OPTIONS:
            cell_1_row_index, cell_1_col_index = win_option[0]
            cell_2_row_index, cell_2_col_index = win_option[1]
            cell_3_row_index, cell_3_col_index = win_option[2]

            cell_1 = self.__board.get_cell_by_indices(cell_1_row_index, cell_1_col_index)
            cell_2 = self.__board.get_cell_by_indices(cell_2_row_index, cell_2_col_index)
            cell_3 = self.__board.get_cell_by_indices(cell_3_row_index, cell_3_col_index)

            cell_values = {cell_1.value, cell_2.value, cell_3.value}
            if cell_values == {"X"} or cell_values == {"O"}:
                return True

        return False

    def run(self):
        while self.__current_step < 9:
            self.__set_current_player()

            available_options = self.__get_available_options()
            print("Available options:", available_options)

            choice = self.__current_player.get_choice(available_options)
            self.__board.fill(self.__current_player, choice)

            if self.is_won():
                self.__winner = self.__current_player
                break

            self.__current_step += 1
