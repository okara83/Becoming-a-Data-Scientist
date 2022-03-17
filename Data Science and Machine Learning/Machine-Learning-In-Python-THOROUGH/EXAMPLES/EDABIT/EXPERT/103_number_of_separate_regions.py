"""
https://edabit.com/challenge/FGzWE8vNyxtTrw3Qg

Number of Separate Regions
The function is given a rectangular matrix consisting of zeros and ones. Count the number of different regions and return the result. A separate region is a collection of ones interconnected horizontally and vertically. A region can have holes in it.

Examples
num_regions([
  [1, 1, 1, 1, 0],
  [1, 1, 0, 1, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]) ➞ 1


num_regions([
  [1, 1, 1, 1, 0],
  [1, 0, 0, 1, 0],
  [1, 1, 1, 1, 0],
  [0, 0, 0, 0, 1]
]) ➞ 2

# The region on the upper left looks like a doughnut.


num_regions([
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 1]
]) ➞ 3
"""
def num_regions(grid):
    result = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                result +=1
                set_grid = [(i,j)]
                while set_grid:
                    x, y = set_grid.pop()
                    grid[x][y] = 0
                    for (s,t) in [(x,y+1), (x,y-1), (x+1,y),(x-1,y)]:
                        if 0 <= s < len(grid) and 0 <= t < len(grid[0]):
                            if grid[s][t]: set_grid.append((s,t))
    return result



num_regions([
  [1, 1, 1, 1, 0],
  [1, 0, 0, 1, 0],
  [1, 1, 1, 1, 0],
  [0, 0, 0, 0, 1]
]) #➞ 2