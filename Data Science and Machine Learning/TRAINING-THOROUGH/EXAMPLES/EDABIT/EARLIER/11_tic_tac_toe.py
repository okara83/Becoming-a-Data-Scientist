"""
Tic Tac Toe
Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

Examples
tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]) ➞ "X"

tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]) ➞ "O"

tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]) ➞ "Draw"
Notes
Make sure that if O wins, you return the letter "O" and not the integer 0 (zero) and if it's a draw, make sure you return the capitalised word "Draw". 
If you return "X" or "O", make sure they're capitalised too.
"""

def tic_tac_toe(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        if board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"  
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return "X"
        if board[0][i] == board[1][i] == board[2][i] == "O":
            return "O" 
    
    if board[0][0] == board[1][1] == board[2][2] == "X" or  board[2][0] == board[1][1] == board[0][2] == "X":
            return "X"
    if board[0][0] == board[1][1] == board[2][2] == "O" or  board[2][0] == board[1][1] == board[0][2] == "O":
            return "O"   

    return "Draw"
    
tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]) #➞ "X"    
    