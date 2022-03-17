"""
https://edabit.com/challenge/8jYLBswq9jnttZeox   EXPERT ----

Langton's Ant
Langton's ant is a two-dimensional Turing machine invented in the late 1980s. The ant starts out on a grid of black and white cells and follows a simple set of rules that has complex emergent behavior.

Langton's ant

The ant can travel in any of the four cardinal directions on each step. The ant moves according to the following rules:

At a white square (1), turn 90° right, flip the color of the square, and move forward one unit.
At a black square (0), turn 90° left, flip the color of the square, and move forward one unit.
The grid has no limits and therefore if the ant moves outside the borders, the grid should be expanded with 0s, respectively maintaining the rectangle shape.
Create a function Langton's Ant with the following parameters:

grid - a two-dimensional list of 1s and 0s
# representing white and black cells respectively

column - horizontal position of the ant

row - ant's vertical position

n - number of iterations

direction - ant's current direction
# 0 - north, 1 - east, 2 - south, 3 - west
# default value will be 0
... and returns the state of the grid after n iterations.

Examples
langtons_ant([[1]], 0, 0, 1, 0) ➞ [[0, 0]]
# Initially facing north (0), at the first iteration the ant turns
# right because it stands on a white square, 1. After that, it flips
# the square and moves forward.

langtons_ant([[0]], 0, 0, 1, 0) ➞ [[0, 1]]

langtons_ant([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 2, 2, 10, 1) ➞ [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1], [0, 0, 0, 1]]
Notes
N/A
"""

def langtons_ant(grid, column, row, n, direction=0):

	for i in range(n):
		
		if grid[row][column]==1:
			direction=(direction+1)%4
			grid[row][column]=0
		else:
			direction=(direction-1)%4
			grid[row][column]=1
            
		if direction==0: row-=1
		elif direction==2: row+=1
		elif direction==1: column+=1
		elif direction==3: column-=1
		
		if column>=len(grid[0]): grid=[x+[0] for x in grid]
		elif column<0:
			grid=[[0]+x for x in grid]
			column+=1
            
		if row>=len(grid): grid= grid+ [[0 for x in grid[0] ]]
		elif row<0:
			grid= [[0 for x in grid[0] ]] + grid
			row+=1

	
	return grid

langtons_ant([[0]], 0, 0, 1, 0) #➞ [[0, 1]]