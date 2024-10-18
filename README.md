# Tic Tac Toe Game

Welcome to **Tic Tac Toe**—a simple and fun game built using Python and Tkinter. This project lets you play either in **Single Player (AI)** mode or **Multiplayer** mode with another human. The game has a graphical interface where you click to place your move, and it automatically checks for winners or draws.

---

## Features

- **Two Game Modes:**
  - **Single Player (AI mode):** Play against a simple AI that uses the Minimax algorithm to make optimal moves.
  - **Multiplayer mode:** Play against another person locally on the same machine.
  
- **Dynamic Win/Draw Detection:** 
  - The game checks for a win or draw automatically after each move.
  - Displays the winner or if the game is drawn.
  
- **Restart Game Option:** Allows players to reset the board for a new game without restarting the program.

---

## How to Play

1. **Choose the game mode** by clicking either "Single Mode" to play against AI or "Multiple Mode" to play with a friend.
2. **Make your move** by clicking on one of the 9 squares on the Tic Tac Toe board.
3. The game alternates between players (Player 1 = X, Player 2 or AI = O).
4. The game announces the winner or a draw once the game ends.
5. To play again, click the **"Restart Game"** button to reset the board.

---

## Game Rules

1. The game is played on a 3x3 grid.
2. Players take turns to place their symbol (`X` or `O`) in any empty square.
3. The first player to align three symbols in a row (horizontally, vertically, or diagonally) wins.
4. If all 9 squares are filled without any winner, the game is a draw.

---

## Code Structure

- **Main Game Window**: 
  - Created using Tkinter, a Python GUI toolkit.
  - The game window is fixed at a size of `325x550` pixels and contains three main sections: title, optional buttons (game mode), and the game board.

- **Game Logic**: 
  - The game logic is based on a dictionary `board` where each key (1-9) represents a position on the grid.
  - The function `play(event)` is triggered when a player clicks a square, updating the board and checking for a win, draw, or switching turns.
  
- **AI Algorithm**: 
  - The AI opponent uses the **Minimax algorithm** to calculate the best possible move in `AIplays()`. This ensures the AI always plays optimally.

- **Win/Draw Detection**: 
  - The function `checkForWin(player)` verifies if a player has won by checking all possible winning combinations.
  - The function `checkForDraw()` checks if all squares are filled, resulting in a draw.

---

## How to Run

1. Ensure you have Python installed (preferably Python 3).
2. Install Tkinter, which is usually bundled with Python:
    ```bash
   sudo apt-get install python3-tk 
3. Clone this repository:
   ```bash
   git clone https://github.com/tanishkakumari111/AI-Tic-Tac-Toe.git
4. Navigate to the directory:
   ```bash
   cd tic-tac-toe-game
5. Run the program:
   ```bash
   python tic_tac_toe.py

## Future Improvements
- Add a difficulty setting for the AI.
- Include sound effects or animations for a more dynamic game experience.
- Implement an online multiplayer option.

## Contributing
If you'd like to contribute, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License—see the LICENSE file for more details.
