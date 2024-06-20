import random

#Game class
class Battleship_game:
    def __init__(self):
        #Initalise game
        #Set game board size
        self.board_size = 5
        #Add ships and their size
        self.ships = {"A": 2, "B": 3, "C": 4, "D":5}
        #Create player board
        self.player_board = [["" for _ in range(self.board_size)] for _ in range (self.board_size)]
        self.computer_board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]


    #Function to print game board
    def print_board(self, board):
        #Goes through each row on the board
        for row in board:
            #Empty string to build current row
            row_string =""
            #Goes through each cell on the board
            for cell in row:
                if cell == "":
                    #Empty cells marked as ' UNKNOWN '
                    row_string += " UNKNOWN "
                elif cell == "H":
                    #Hits marked as ' HIT '
                    row_string +=" HIT "
                elif cell == "M":
                    #Misses marked as ' MISS '
                    row_string += " MISS "
                else:
                    # if none of above add the letter of the ship on the cell.
                    row_string += f" {cell} "
            
            #Print the row
            print(row_string)
