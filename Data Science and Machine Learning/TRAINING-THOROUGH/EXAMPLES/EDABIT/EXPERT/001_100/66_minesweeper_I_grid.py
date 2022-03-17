"""
Minesweeper I — Grid
This challenge is based on the game Minesweeper.

Create a function that takes a grid of # and -, where each hash (#) represents a mine and each dash (-) represents a mine-free spot. Return a list where each dash is replaced by a digit indicating the number of mines immediately adjacent to the spot (horizontally, vertically, and diagonally).

Examples
num_grid([
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "0", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "1", "#", "1", "0"],
  ["0", "1", "1", "1", "0"],
  ["0", "0", "0", "0", "0"],
]

num_grid([
  ["-", "-", "-", "-", "#"],
  ["-", "-", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "-", "-", "-", "-"],
  ["#", "-", "-", "-", "-"]
]) ➞ [
  ["0", "0", "0", "1", "#"],
  ["0", "1", "1", "2", "1"],
  ["0", "1", "#", "1", "0"],
  ["1", "2", "1", "1", "0"],
  ["#", "1", "0", "0", "0"]
]

num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) ➞ [
  ["1", "1", "2", "#", "#"],
  ["1", "#", "3", "3", "2"],
  ["2", "4", "#", "2", "0"],
  ["1", "#", "#", "2", "0"],
  ["1", "2", "2", "1", "0"],
]
"""

def num_grid(lst):
    a=[[[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]]]
    b=[
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]
    
    
    for i in range(1,len(lst)-1):
        for j in range(1,len(lst[i])-1):
            if lst[i][j] == "#":
                a[i][j].append("#")
                a[i-1][j-1].append(1)
                a[i-1][j].append(1)
                a[i-1][j+1].append(1)
                a[i+1][j-1].append(1)
                a[i+1][j].append(1)
                a[i+1][j+1].append(1)
                a[i][j-1].append(1)
                a[i][j+1].append(1)

    
    for j in range(1,4):
        if lst[0][j] == "#":
                a[0][j].append("#")
                a[1][j-1].append(1)
                a[1][j].append(1)
                a[1][j+1].append(1)
                a[0][j-1].append(1)
                a[0][j+1].append(1)
        if lst[4][j] == "#":
                a[4][j].append("#")
                a[3][j-1].append(1)
                a[3][j].append(1)
                a[3][j+1].append(1)
                a[4][j-1].append(1)
                a[4][j+1].append(1)

                
    for i in range(1,4):
        if lst[i][0] == "#":
                a[i][0].append("#")
                a[i-1][1].append(1)
                a[i][1].append(1)
                a[i+1][1].append(1)
                a[i-1][0].append(1)
                a[i+1][0].append(1)
        if lst[i][4] == "#":
                a[i][4].append("#")
                a[i-1][3].append(1)
                a[i][3].append(1)
                a[i+1][3].append(1)
                a[i-1][4].append(1)
                a[i+1][4].append(1)                
                
    if lst[0][0] == "#":
        a[0][0].append("#")
        a[0][1].append(1)
        a[1][1].append(1)
        a[1][0].append(1)

    if lst[0][4] == "#":
        a[0][4].append("#")
        a[0][3].append(1)
        a[1][3].append(1)
        a[1][4].append(1)     
                
    if lst[4][0] == "#":
        a[4][0].append("#")
        a[3][0].append(1)
        a[3][1].append(1)
        a[4][1].append(1)

    if lst[4][4] == "#":
        a[4][4].append("#")
        a[4][3].append(1)
        a[3][3].append(1)
        a[3][4].append(1)      
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            if "#" in a[i][j]:
                b[i][j] = "#"
            else:
                b[i][j] = str(sum(a[i][j]))
    
    return b





num_grid([
  ["-", "-", "-", "#", "#"],
  ["-", "#", "-", "-", "-"],
  ["-", "-", "#", "-", "-"],
  ["-", "#", "#", "-", "-"],
  ["-", "-", "-", "-", "-"]
]) #➞ [
  #["1", "1", "2", "#", "#"],
  #["1", "#", "3", "3", "2"],
  #["2", "4", "#", "2", "0"],
  #["1", "#", "#", "2", "0"],
  #["1", "2", "2", "1", "0"],