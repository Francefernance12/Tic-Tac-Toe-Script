from random import choice
from game_configs import BoardConfigs, instructions

# config object
board_configs = BoardConfigs()

# restart game
def restart_game():
    restart = input("Do you want to play again? (yes/no): ").lower()
    return restart == 'yes'


# Check if win condition met
def check_win():
    board_configs.game_board()
    for combination in board_configs.WIN_CONDITION:
        # if any of the win conditions match, player wins
        if board_configs.BOARD_POSITION[combination[0]] == board_configs.BOARD_POSITION[combination[1]] == \
                board_configs.BOARD_POSITION[combination[2]] != ' ':
            # prints the player's symbol
            print(f"Player {board_configs.BOARD_POSITION[combination[0]]} wins!")
            return False

    # if win condition is not met
    if ' ' not in board_configs.BOARD_POSITION:
        print("It's a draw!")
        return False

    # continues the game
    return True


# Adds the player's position into the board. Player arg is either X or O
def add_position(position, player):
    # check if the position is empty
    if board_configs.BOARD_POSITION[position] == ' ':
        print(f"Player {player} chooses position {position}")
        board_configs.BOARD_POSITION[position] = player
        return True

    print("Position occupied, please try again")
    return False


# Bot logic
def bot_move_position(difficulty):
    # positions available in the board
    available_pos = [i for i, spot in enumerate(board_configs.BOARD_POSITION) if spot == ' ']
    # print(available_positions)

    # winnable and blockable positions
    for combination in board_configs.WIN_CONDITION:
        # Logic for winnable and blockable positions for the bot
        opportunities = [board_configs.BOARD_POSITION[c_pos] for c_pos in combination]
        # winning opportunities
        if opportunities.count('O') == 2 and opportunities.count(' ') == 1:  # Bot can win
            return combination[opportunities.index(' ')]
        if difficulty == 1:
            # blocking opportunities
            if opportunities.count('X') == 2 and opportunities.count(' ') == 1:  # Block opponent
                return combination[opportunities.index(' ')]

    # Checks if available positions match one of the position in the win conditions
    for pattern in board_configs.BOT_PATTERN:
        for pos in available_pos:
            # if the position is in the win condition
            if pos in pattern:
                return pos
            else:
                continue

    # if no win condition
    return choice(available_pos)


def player_input():
    while True:
        try:
            position = int(input("Enter a number from 0 to 8: "))
            if 0 <= position <= 8:
                return position
            print("Input out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Game Mode (Human vs Human or Human vs Bot)
def game_mode():
    game_mode = int(input("Type 0 to play with Bot player, type 1 to play with human player: "))
    if game_mode == 0:
        difficulty = int(input("Type 0 for Easy difficulty, 1 for Hard difficulty: "))
        if difficulty == 0 or difficulty > 1:
            print("Bot difficulty is now Easy.")
        else:
            print("Bot difficulty is now Hard.")
    return game_mode if game_mode in [0, 1] else 0, difficulty if game_mode == 0 else 0


# Main game
def start_game():
    instructions()
    current_player = 'X'
    current_game_mode, current_difficulty = game_mode()
    game_on = True

    while game_on:
        # ensuring that the player types
        try:
            if current_game_mode == 0:  # Human vs Bot
                # Player
                if current_player == 'X':
                    p1_position = player_input()
                    if add_position(p1_position, 'X'):
                        game_on = check_win()
                        current_player = 'O'
                # Bot
                else:
                    bot_position = bot_move_position(current_difficulty)
                    if bot_position is not None:
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
        # Handles difficulty options input errors
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # restart game
    if restart_game():
        board_configs.reset_board()
        start_game()


# initializes the game
if __name__ == "__main__":
    start_game()
