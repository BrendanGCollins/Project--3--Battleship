import random

#Game class
class Battleship_game:
    def __init__(self):
        """
        Initialize the game.
        Set game board size, add ships and their sizes, create boards for the computer and player guesses,
        and place ships on the computer's board.
        """
        self.board_size = 5
        #Add ships and their size
        self.ships = {"A": 2, "B": 3, "C": 4, "D":5}
        self.computer_board = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        #Create boards for guesses
        self.player_guess = [["" for _ in range(self.board_size)] for _ in range(self.board_size)]
        #Place ships on computers board
        for ship , size in self.ships.items():
            self.place_ships(self.computer_board, ship, size)

    def print_board(self, board):
        """
        Print the game board.
        """
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
                    #If none of above add the letter of the ship on the cell.
                    row_string += f" {cell} "

            #Print the row
            print(row_string)

    def place_ships(self, board, ship, size):
        """
        Place a single ship on the board at a random position and orientation.
        Ensures the chosen position is free before placing the ship.
        """
        #Check if the ship is placed
        placed = False
        #Repeat until the ships are successfully placed
        while not placed:
            # Randomly choose horizontal or vertical orientation
            orientation = random.choice(["H", "V"])
            if orientation == "H":
                # Randomly select a row and starting column
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - size)
                # Check if space is free
                space_free = True
                for i in range(size):
                    if board[row][col + i] != "":
                        space_free = False
                        # Exit loop once a cell that is not empty is found
                        break
                # Place ship if there is a free space
                if space_free:
                    for i in range(size):
                        board[row][col + i] = ship
                    placed = True
            else:
                # Random selection for vertical orientation
                row = random.randint(0, self.board_size - size)
                col = random.randint(0, self.board_size - 1)
                # Check if space is free
                space_free = True
                for i in range(size):
                    if board[row + i][col] != "":
                        space_free = False
                        # Exit loop once a cell that is not empty is found
                        break
                # Place ship if there is a free space
                if space_free:
                    for i in range(size):
                        board[row + i][col] = ship
                    placed = True