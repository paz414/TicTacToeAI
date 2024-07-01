# Tic-Tac-Toe with AI

A Python implementation of the classic Tic-Tac-Toe game, featuring an unbeatable AI opponent using the Minimax algorithm.

## Features

- Play against an AI that uses the Minimax algorithm
- Choose to play as either 'X' or 'O'
- Clear visual representation of the game board
- Error handling for invalid moves

## How to Play

1. Run the script in a Python environment.
2. Choose your symbol ('O' or 'X') by entering 1 or 2 respectively.
3. Enter the X and Y coordinates (1-3) for your move when prompted.
4. Try to beat the AI!

## Game Rules

- The game is played on a 3x3 grid.
- Players take turns placing their symbol ('X' or 'O') in empty cells.
- The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins.
- If all cells are filled and no player has won, the game is a draw.

## Technical Details

- The game board is represented as a 5x5 array to include separators for better visualization.
- The Minimax algorithm is used to determine the best move for the AI.
- The AI is designed to be unbeatable; at best, you can achieve a draw.

## Functions

- `display(Board)`: Displays the current state of the game board.
- `isFill(Board)`: Checks if the board is completely filled.
- `isEmpty(i,j)`: Checks if a specific cell is empty.
- `Wins(Board)`: Checks if there's a winner.
- `CompMove()`: Determines the best move for the AI using the Minimax algorithm.
- `minimax(isMax)`: Implements the Minimax algorithm for the AI's decision-making.

## Requirements

- Python 3.x

## Future Improvements

- Add a graphical user interface (GUI)
- Implement difficulty levels for the AI
- Add option for two human players

## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
