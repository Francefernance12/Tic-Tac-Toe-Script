from random import choice, shuffle

# Board positions
BOARD_POSITION = [' ' for _ in range(9)]

# Win conditions
WIN_CONDITION = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
    [0, 4, 8], [2, 4, 6]  # diagonals
]

# Changing the bot's pattern
BOT_PATTERN = WIN_CONDITION[:]
shuffle(BOT_PATTERN)


# Create the board
def game_board():
    print(f"{BOARD_POSITION[0]} | {BOARD_POSITION[1]} | {BOARD_POSITION[2]}")
    print("--+---+--")
    print(f"{BOARD_POSITION[3]} | {BOARD_POSITION[4]} | {BOARD_POSITION[5]}")
    print("--+---+--")
    print(f"{BOARD_POSITION[6]} | {BOARD_POSITION[7]} | {BOARD_POSITION[8]}")


# returns False if there is a win else True
def check_win():
    game_board()
    for combination in WIN_CONDITION:
        # if any of the win conditions match, player wins
        if BOARD_POSITION[combination[0]] == BOARD_POSITION[combination[1]] == BOARD_POSITION[combination[2]] != ' ':
            # prints the player's symbol
            print(f"Player {BOARD_POSITION[combination[0]]} wins!")
            return False

    # if win condition is not met
    if ' ' not in BOARD_POSITION:
        print("It's a draw!")
        return False

    # continues the game
    return True


# Adds the player's position into the board. Player arg is either X or O
def add_position(position, player):
    # check if the position is empty
    if BOARD_POSITION[position] == ' ':
        BOARD_POSITION[position] = player
        return True

    print("Position occupied, please try again")
    return False


# Bot logic
def bot_move_position():
    # positions available in the board
    available_pos = [i for i, spot in enumerate(BOARD_POSITION) if spot == ' ']
    # print(available_positions)

    # winnable and blockable positions
    for combination in WIN_CONDITION:
        # reads
        opportunities = [BOARD_POSITION[c_pos] for c_pos in combination]
        # winning opportunities
        if opportunities.count('O') == 2 and opportunities.count(' ') == 1:  # Bot can win
            return combination[opportunities.index(' ')]
        # blocking opportunities
        if opportunities.count('X') == 2 and opportunities.count(' ') == 1:  # Block opponent
            return combination[opportunities.index(' ')]

    # Checks if available positions match one of the position in the win conditions
    for pattern in BOT_PATTERN:
        for pos in available_pos:
            # if the position is in the win condition
            if pos in pattern:
                print(f"AI chooses position {pos}")
                return pos
            else:
                continue

    # if no win condition
    return choice(available_pos)


# Instructions
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


# Game Mode (Human vs Human or Human vs Bot)
def game_mode():
    game_mode = int(input("Type 0 to play with Bot, type 1 to play with human player: "))
    return game_mode if game_mode in [0, 1] else None


# player input
def player_input():
    while True:
        try:
            position = int(input("Enter a number from 0 to 8: "))
            if 0 <= position <= 8:
                return position
            print("Input out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main game
def start_game():
    instructions()
    current_player = 'X'
    current_game_mode = game_mode()
    game_on = True

    while game_on:
        # ensuring that the player types
        try:
            # bot game mode
            if current_game_mode == 0:
                # Player
                if current_player == 'X':
                    p1_position = player_input()
                    if add_position(p1_position, 'X'):
                        game_on = check_win()
                        current_player = 'O'
                # Bot
                else:
                    bot_position = bot_move_position()
                    if bot_position is not None:
                        print(f"AI chooses position {bot_position}")
                        add_position(bot_position, 'O')
                        game_on = check_win()
                        current_player = 'X'
                    else:
                        print("No available positions left.")
                        game_on = False
            # Human vs Human
            elif current_game_mode == 1:  # Human vs Human
                # Player 1
                if current_player == 'X':
                    p1_position = player_input()
                    if add_position(p1_position, 'X'):
                        game_on = check_win()
                        current_player = 'O'
                # Player 2
                else:
                    p2_position = player_input()
                    if add_position(p2_position, 'O'):
                        game_on = check_win()
                        current_player = 'X'
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


# calling the function
start_game()
