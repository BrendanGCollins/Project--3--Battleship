import random
from colorama import init, Fore

#Initialise colorama
init(autoreset=True)

#Game class
class BattleshipGame:
    def __init__(self):
        """
        Initialise the game.
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
        #Calculate total ship parts
        self.total_ship_parts = sum(self.ships.values())

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
                    row_string += Fore.BLUE + " UNKNOWN "
                elif cell == "H":
                    #Hits marked as ' HIT '
                    row_string += Fore.GREEN +" HIT "
                elif cell == "M":
                    #Misses marked as ' MISS '
                    row_string += Fore.RED + " MISS "
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
    
    def player_ship_guess(self):
        """
        Allows the player to guess computer ship positions
        """
        #Introduction to the game
        print("Welcome to Battleship!")
        print("you have 20 guesses to find all the ships")
        print("enter your guesses in the format: row col(e.g. 2 3)")
        print("Guesses range from 0 to 4 for both row and column")

        #Inital guess count and set maximum guesses allowed
        guess_count = 0
        max_guesses = 20
        #Inital hits count
        hits = 0

        while guess_count < max_guesses:
            #Show player remaining guesses
            print(f"{max_guesses - guess_count} guesses left")

            #Ask for player input
            guess = input("Enter your guess(row col):").split()
            #If you enter more than two characters you get an invalid message
            if len(guess) != 2:
                print("Invalid input. Please enter in the format: row col")
                continue
            try:
                row, col = int(guess[0]), int(guess[1])
                if (row == 0 and guess[0] != "0") or (col == 0 and guess[1] !="0"):
                    raise ValueError #Prevents leading 0 error i.e 01
            except ValueError:
                print("Invalid input. Please enter in the format: row col")
                continue

            #Check if guess is within the limits of the game board
            if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
                print("Invalid input. Please enter valid row and column within board limits")
                continue

            #Check if cell has already bee guessed
            if self.player_guess[row][col] in ["H", "M"]:
                print("You already guessed this cell")
                continue

            #Check if guess is a hit or miss
            if self.computer_board[row][col] != "":
                #If cell contains part of ship it is a hit
                print("Hit!")
                #Mark player board with 'H' for hit
                self.player_guess[row][col] = "H"
                #Remove  from computer board to prevent hitting same part again
                self.computer_board[row][col] = ""
                #Add one to hit count
                hits += 1
            else:
                #If guess is an empty cell then it is a miss
                print("Miss!")
                #Mark player guess board with a 'M' for miss
                self.player_guess[row][col] = "M"
            
            # Print player board
            self.print_board(self.player_guess)

            #Add 1 to guess count after each guess
            guess_count +=1

        #Loop to check hitting ships/ running out of guesses
        if hits == self.total_ship_parts:
            print(Fore.GREEN + "Winner! You sunk all the ships")
        else:
            print(Fore.RED + "Game over! You ran out of guesses")
            #Show the final game board to the player
            self.print_board(self.player_guess)

if __name__ == "__main__":
    #Create game and start player's guesses
    game = BattleshipGame()
    game.player_ship_guess()