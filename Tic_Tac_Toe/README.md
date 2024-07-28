# Tic Tac Toe Game

This is a graphical implementation of the classic Tic Tac Toe game using Python and Pygame. The game features a user-friendly interface, AI opponent using the Minimax algorithm, and a restart button to play multiple rounds.

## Features

1. Player vs AI: Play against a challenging AI opponent.
2. Graphical Interface: Clean and intuitive design with a restart button.
3. Minimax Algorithm: AI uses the Minimax algorithm to make optimal moves.
4. Game End Detection: Detects win, loss, and tie conditions.
5. Restart Functionality: Restart the game at any time.

## Installation

To run this game, you need to have Python and Pygame installed on your machine.

Step-by-Step Guide

1. Install Python
   Download and install Python from the official website.
2. Install Pygame
   Use pip to install Pygame :
   pip install pygame
3. Clone the Repository :
   git clone https://github.com/yourusername/TicTacToe-AI.git
4. Navigate to the Directory :
   cd TicTacToe-AI
5. Run the Game :
   python tictactoe.py

## How to Play

1. The player always starts first and is assigned the 'X' mark.
2. Click on any empty square to place your mark.
3. The AI opponent, which uses the 'O' mark, will automatically make its move after the player.
4. The game continues until a player wins or the board is full, resulting in a tie.
5. To restart the game, click the restart button.

## Code Structure

1. Importing Libraries : 
The script starts by importing the necessary libraries: pygame, sys, and numpy.
2. Initializing Pygame and Setting Up Colors and Dimensions : 
Pygame is initialized, and various colors and dimensions for the game are defined.
3. Drawing Functions : 
Functions to draw the grid lines and the X and O figures on the board.
4. Game Logic Functions : 
Functions to handle marking squares, checking for available squares, checking if the board is full, and determining the winner.
5. Minimax Algorithm for AI : 
The Minimax algorithm to determine the best move for the AI.
6. Finding the Best Move for the AI : 
Function to find and execute the best move for the AI.
7. Restart Function : 
Function to restart the game.
8. Drawing Text on Screen : 
Setting up the font and function to draw text on the screen.
9. Button Class for Restart : 
Class to handle the restart button.
10. Initializing and Drawing Initial Elements :
Initializing the restart button and drawing the initial elements on the screen.
11. Main Game Loop : 
The main game loop that handles events, updates the game state, and renders the game.

## License

This project is open source and available under the MIT License.

## Support

For any questions or feedback, please contact pchithra611@gmail.com

## Contributing

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
