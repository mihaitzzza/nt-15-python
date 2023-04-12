class Player:
    def __init__(self, sign):
        self.__sign = sign

    def __get_input(self, available_options):
        choice = input(f"Player {self.__sign} pick a cell: ")
        choice = int(choice)

        if choice not in available_options:
            raise ValueError("Choice is not available.")

        return choice

    def get_choice(self, available_options):
        while True:
            try:
                choice = self.__get_input(available_options)
            except ValueError:
                print("Option is not available.")
                continue

            return choice

    def __str__(self):
        return self.__sign

    def __repr__(self):
        return self.__str__()
