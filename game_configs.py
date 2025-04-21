from random import shuffle

def instructions():
    print("Starting game")
    input("Press enter to play")
    print("Player 1: X")
    print("Player 2: O")
    print("0 to 8 represents the position in the game board starting from top to bottom, left to right")
    print("""
    0 | 1 | 2 
    --+---+--
    3 | 4 | 5 
    --+---+--
    6 | 7 | 8
    """)


class BoardConfigs:
    def __init__(self):
        # Board positions
        self.BOARD_POSITION = [' ' for _ in range(9)]

        # Win conditions
        self.WIN_CONDITION = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]

        # Changing the bot's pattern
        self.BOT_CONDITION = self.WIN_CONDITION[:]
        shuffle(self.BOT_CONDITION)
        self.BOT_PATTERN = self.BOT_CONDITION[:]

    # Create the board
    def game_board(self):
        print(f"{self.BOARD_POSITION[0]} | {self.BOARD_POSITION[1]} | {self.BOARD_POSITION[2]}")
        print("--+---+--")
        print(f"{self.BOARD_POSITION[3]} | {self.BOARD_POSITION[4]} | {self.BOARD_POSITION[5]}")
        print("--+---+--")
        print(f"{self.BOARD_POSITION[6]} | {self.BOARD_POSITION[7]} | {self.BOARD_POSITION[8]} \n")

    def reset_board(self):
        self.BOARD_POSITION = [' ' for _ in range(9)]