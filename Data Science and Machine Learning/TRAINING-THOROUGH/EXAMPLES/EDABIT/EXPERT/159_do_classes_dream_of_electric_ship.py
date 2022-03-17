"""
https://edabit.com/challenge/pN7iSYmghjdnHiMvT         EXPERT--------

Do Classes Dream of Electric Ship?
In this challenge, you have to build a class that will store and manipulate the data of a simplified clone of Battleship, the popular strategy game.

The game is played on a 5x5 square board, with rows indexed by uppercase letters from A to E (from top to bottom), and columns indexed by numbers from 1 to 5 (from left to right).

Rules of the Game
There are two types of ship: the Patrol and the Cruiser. The Patrol occupies a single cell, the Cruiser occupies two cells, horizontally or vertically.
Three Patrols and three Cruisers will be placed randomly in the grid, without ships adjacent in rows and columns (in particular, two adjacent cells can only both be ship cells if they belong to the same Cruiser).
The player calls six different cells, trying to guess if there's a Patrol or a Cruiser in it.
Hits and misses are recorded on the board. For every hit Patrol or Cruiser, a point is gained, and if a Cruiser is sunk, two additional points are gained.
Class "Battleship"
Each instance of the Battleship class in the Tests tab will be declared with two parameters:

scheme is a list containing 9 strings which are the coordinates indicating where the ships are placed on the board.
guesses is a list containing 6 strings which are the coordinates of the guesses made by the player.
What do you have to implement?
The Tests will expect each instance of the Battleship class to possess four methods:

board() will return the final state of the board, based on the placement of the ships and the results of the player guesses, as a matrix of size 5x5. To vizually represent the state of the game, you will use four different characters:

' ' = a blank space on the board.
's' = a space occupied by a ship.
'.' = a miss (wrong guess).
'X' = a hit (a correct guess).
hits() will return the total number of hits made by the player (correct guesses), either on Patrols or on Cruisers.

sunk() will return the total number of sunk Cruisers (two adjacent correct guesses, either horizontally or vertically).
points() will return the total number of points gained by the player (1 for every hit, plus 2 for every sunk Cruiser).
Examples
scheme = ["A1", "C1", "B2", "B3", "D2", "E2", "E4", "E5", "A5"]

guesses = ["A1", "B2", "C3", "D4", "E5", "E4"]

battleship.board() ➞ [
  [X,  ,  ,  , s],
  [ , X, s,  ,  ],
  [s,  , .,  ,  ],
  [ , s,  , .,  ],
  [ , s,  , X, X]
]

battleship.hits() ➞ 4
# Total hits.

battleship.sunk() ➞ 1
# Sunk Cruisers only, sunk Patrols not included.

battleship.points() ➞ 6
# Hits + additional points given by sunk Cruisers.
Notes
If two cruisers are in the same row or the same column, there will be a blank cell between them, so that it will be possible to distinguish them as different ships.
The board is not given, you have to build it.
In the Examples above, the symbols in the board are not between quotation marks for readability, but they are strings.
"""

# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit

class Battleship:
    values = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

    def __init__(self, scheme, guesses):
        self.scheme = scheme
        self.guesses = guesses

    def board(self):
        board = [[' ']*5 for i in range(5)]
        for spot in self.scheme:
            board[self.values[spot[0]]][int(spot[1]) -1] = 's'
        for spot in self.guesses:
            if spot in self.scheme:
                board[self.values[spot[0]]][int(spot[1]) -1] = 'X'
            else:
                board[self.values[spot[0]]][int(spot[1]) -1] = '.'
        return board

    def hits(self):
        return sum(g in self.scheme for g in self.guesses)

    def sunk(self):
        b = self.board()
        sunk = 0
        for i in range(5):
            for j in range(1, 5):
                if b[i][j] == 'X' and b[i][j-1] == 'X':
                    sunk += 1
        for i in range(1, 5):
            for j in range(5):
                if b[i-1][j] == 'X' and b[i][j] == 'X':
                    sunk += 1
        return sunk

    def points(self):
        return self.hits() + self.sunk() * 2