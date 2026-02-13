# Welcome to Tic-Tac-Toe (Game Preview)

👋 **Welcome to this project!**

Now it's time to apply your OOP skills to create a Tic-Tac-Toe game.

We will write and test these classes step by step:

- `Move`
- `Player`
- `Board`

Then, we will implement the game logic by working with the objects and their attributes and methods. You will see how we can use objects like bricks that can work together to build more complex functionality.

## ◼️ Game Rules

Let's talk a little bit about the rules of Tic-Tac-Toe:

In Tic-Tac-Toe, two players try to fill a row,  a column, the diagonal, or the antidiagonal of a 3x3 game board.

This will be our game board:

```text
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
```

The user will enter an integer from 1 to 9 (inclusive) to select the position on the board.

**Gameplay:**

1. On each turn, each player will select a particular position on the board and a marker will be added to that position.
2. A human player will play against a computer player, which will select a random position.
3. **Important:** If the player selected a position that is already taken, he/she **loses the turn**.
4. When a row, a column, the diagonal, or the antidiagonal is full with the player's markers, the game is over and that player wins the game.
5. If the board is full but none of the players has won the game, then there is a tie.

**Post-Game:**
When the game is over, we will ask the user if he/she would like to continue playing. We will take user input and start a new round if the player chooses to continue the game.

## ◼️ Sample Output

To give you an idea of the project that we will be building, here is a sample game output:

```text
**************************
  Welcome to Tic-Tac-Toe  
**************************
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   |   |   |
|   |   |   |
|   |   |   |
 
Please enter your move (1-9): 4
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   |   |   |
| X |   |   |
|   |   |   |
 
Computer move (1-9):  8
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   |   |   |
| X |   |   |
|   | O |   |
 
Please enter your move (1-9): 2
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X |   |
| X |   |   |
|   | O |   |
 
Computer move (1-9):  2
This position is already taken. Please enter another one.
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X |   |
| X |   |   |
|   | O |   |
 
Please enter your move (1-9): 3
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X | X |
| X |   |   |
|   | O |   |
 
Computer move (1-9):  7
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X | X |
| X |   |   |
| O | O |   |
 
Please enter your move (1-9): 3
This position is already taken. Please enter another one.
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X | X |
| X |   |   |
| O | O |   |
 
Computer move (1-9):  5
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X | X |
| X | O |   |
| O | O |   |
 
Please enter your move (1-9): 1
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
| X | X | X |
| X | O |   |
| O | O |   |
 
Awesome. You won the game! 🎉
Would you like to play again? Enter X for YES or O for NO: Y
Your input was not valid but I will assume that you want to play again. 💡
*************
  New Round  
*************
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   |   |   |
|   |   |   |
|   |   |   |
 
Please enter your move (1-9): 8
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   |   |   |
|   |   |   |
|   | X |   |
 
Computer move (1-9):  4
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   |   |   |
| O |   |   |
|   | X |   |
 
Please enter your move (1-9): 2
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X |   |
| O |   |   |
|   | X |   |
 
Computer move (1-9):  9
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
|   | X |   |
| O |   |   |
|   | X | O |
 
Please enter your move (1-9): 1
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
| X | X |   |
| O |   |   |
|   | X | O |
 
Computer move (1-9):  5
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
| X | X |   |
| O | O |   |
|   | X | O |
 
Please enter your move (1-9): 3
 
Positions:
| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
Board:
| X | X | X |
| O | O |   |
|   | X | O |
 
Awesome. You won the game! 🎉
Would you like to play again? Enter X for YES or O for NO: O
Bye! Come back soon 👋
```


💡 **Are you ready?**

Let's start working on the first class of our project: the `Move` class.