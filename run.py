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