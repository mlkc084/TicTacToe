# This runs in Python 3.

# We will use three "control" characters to dictate what is stored at a given
# location on the board.
# 'X' denotes X piece
# 'O' denotes O piece
# 'E' denotes an unoccupied position

# imports
import time
from random import randint


# Functions
# print_board:
# Prints the game board
def print_board(game_board):
    for row in game_board:
        print("|", end="")
        for item in row:
            # only print a piece that is there
            if item == 'E':
                print("_", end="")
            else:
                print(item, "|", end="")
        print("|", end="")
        print()


# check_location_available
# Determine if the specified location is available or occupied
# Caller is responsible for making sure row and column on in-bounds to game_board
def check_location_available(row, column, game_board):
    if game_board[row][column] == 'E':
        return True
    else:
        return False


# position_in_bounds
# Check that position specified was in bounds
def position_in_bounds(x, y):
    if x < 3 and y < 3:
        return True
    else:
        return False


# get_user_position:
# Ask the user for the row and column for which to place their piece.
# Return the row and column specified
def get_user_position(game_board):
    invalid_entry = True
    while invalid_entry:
        choose_row = int(input("Choose Row: "))
        choose_column = int(input("Choose Column: "))

        if position_in_bounds(choose_row, choose_column):
            if check_location_available(choose_row, choose_column, game_board):
                invalid_entry = False
            else:
                print("Position not available")
        else:
            print("Position specified is out of bounds")

    return choose_row, choose_column


# get_cpu_position
# Get a board position from the cpu
def get_cpu_position(game_board):
    invalid_entry = True

    while invalid_entry:
        row = randint(0, 2)
        column = randint(0, 2)

        if check_location_available(row, column, game_board):
            invalid_entry = False

    return row, column


# This gameLoop() function will be the entry point into our TicTacToe game
# To start the game call gameLoop()
def game_loop():
    game_over = False
    game_board = []
    winner = 0

    # Initialize game board (3x3 array)
    for x in range(3):
        game_board.append(['E'] * 3)

    print("Welcome to TicTacToe!")
    # Run the game until game_over is set to True
    while not game_over:

        # The following is placeholder until we have routines to run the game
        for i in range(3):
            print(i)
            time.sleep(1)

        # display Board
        print_board(game_board)

        # ask user for piece position

        # place user's piece on the board using the position they chose

        # display board

        # sleep for 1-3 seconds so it looks like cpu is thinking

        # generate random position for cpu to place its piece

        # place the cpu's piece on the board

        # check if anyone has won, and if so print board then set game_over to True
        game_over = True

    # When game finishes, wrap up and close the program


# Here is where the game actually starts
game_loop()
