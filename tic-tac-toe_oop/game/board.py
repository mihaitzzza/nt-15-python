class Cell:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if self.__value is not None:
            raise ValueError("Cell is not available.")

        self.__value = value

    @property
    def is_available(self):
        return self.__value is None

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self):
        self.__cells = [
            [Cell(), Cell(), Cell()],  # 1, 2, 3
            [Cell(), Cell(), Cell()],  # 4, 5, 6
            [Cell(), Cell(), Cell()],  # 7, 8, 9
        ]

    def fill(self, player, choice):
        row_index = (choice - 1) // 3
        cell_index = (choice - 1) % 3
        cell = self.__cells[row_index][cell_index]
        cell.value = str(player)

    def get_cell_by_indices(self, row_index, col_index):
        return self.__cells[row_index][col_index]

    def get_available_options(self):
        available_options = []

        for row_index, row in enumerate(self.__cells):
            for cell_index, cell in enumerate(row):
                if cell.is_available:
                    available_options.append(row_index * 3 + cell_index + 1)

        return available_options
