# This runs in Python 3.

#imports
import time

# This gameLoop() function will be the entry point into our TicTacToe game
# To start the game call gameLoop()
def gameLoop():

    game_over = False
    game_board = []
    winner = 0

    print("Welcome to TicTacToe!")
    #Run the game until game_over is set to True
    while game_over != True:
        
        #The following is placeholder until we have routines to run the game
        for i in range(3):
            print("Hello %d" %(i))
            time.sleep(1)
        game_over = True

        #display Board

        #ask user for piece position

        #place user's piece on the board using the position they chose

        #display board

        #sleep for 1-3 seconds so it looks like cpu is thinking

        #generate random position for cpu to place its piece

        #place the cpu's piece on the board

        #check if anyone has won, and if so print board then set game_over to True

    #When game finishes, wrap up and close the program

# Here is where the game actually starts
gameLoop()