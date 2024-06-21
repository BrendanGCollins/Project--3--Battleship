# Battleship Game

Battleship is a classic guessing game where a player tries to sink all the computer's ships. This version is implemented in Python and can be played in the console. Unlike classic Battleship you only have 20 tries to sink the computer's fleet or you loose!

## Features

### Existing Features

- Game Introduction
    - Brief message to explain how the game works and the format required to guess where a ship is.

- Random Ship Placement
    - Ships are placed randomly on the computer's board. They can be placed both horizontally or vertically and they cannot overlap. All ships fit within the board's boundries.

- Player Guesses
    - The player has 20 guesses to sink the computer's fleet of ships. Each guess provides feedback on if it was a hit or miss. The guess board is shown after each guess and the player is shown their remaining guesses.

- Coloured Game Board
    - The game board uses colours to make this text based game more visually appealing. Green for hit, red for a miss. At the end of the game the winning message is displayed in green and the game over message in red.

- Input Validation
    - Extensive validation for player input. All guesses must be in the correct format and within the game board. It also prevents guessing the same cell more than once and the guess count does not change unless a guess is entered correctly. If a user enters an invalid guess they will receive a message asking them to try again and reminding them of the correct format.

- End of Game Message
    - The game tracks a players total guesses. Once you reach 20 completed guesses a message will appear to let you know that you lost. If you manage to sink all ships before you run out of guesses a winning message will appear instead.

