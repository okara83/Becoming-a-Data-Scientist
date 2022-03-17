"""
https://edabit.com/challenge/xzaREqFLW3tZdGnTA   EXPERT  

The Most Overlapped Block of the Grid
Create a function that takes two arguments as input:

A positive integer that describes the size of a grid. For example, when the value of the argument is 10, a 10x10 grid will be used.
A list of one or more tuples of size 3. Each tuple represents a block of the grid, and the meanings of the tuple's elements are: 1. The x coordinate. 2. The y coordinate. 3. The range of the block.
The range of a block is the maximum distance from the block situated at the x and y coordinates to other blocks. The distance can't be calculated vertically. The function returns the block that has the most overlaps.

Worked Examples
The tuple (3, 3, 2) covers the following blocks: (1, 3), (2, 4), (2, 3), (2, 2), (3, 5), (3, 4), (3, 3), (3, 2), (3, 1), (4, 4), (4, 3), (4, 2), (5, 3).

Here is a visualization of that, when the first argument is 5, and the second argument is [(3, 3, 2)]:

00100
01110
11111
01110
00100
The 1s represent the blocks covered by (3, 3, 2), while the 0s represent empty blocks. The biggest value on the grid is 1, hence most_overlapped_block(5, [(3, 3, 2)]) returns 1.

If the first argument is 5, and the second argument is [(3, 3, 2), (1, 1, 2)], the grid will look like this:

00100
01110
21111
12110
11200
The 2s represent the blocks of (3, 3, 2) and (1, 1, 2) that overlap. The biggest value on the grid is 2, hence most_overlapped_block(5, [(3, 3, 2, (1, 1, 2))]) returns 2.

Examples
most_overlapped_block(10, [(3, 3, 3), (1, 1, 4)]) ➞ 2

most_overlapped_block(10, [(5, 5, 2), (1, 1, 1)]) ➞ 1

most_overlapped_block(10, [(1, 1, 1), (1, 1, 2), (1, 1, 3)]) ➞ 3
Notes
There can be more than one tuples that look the same in the second argument, like [(3, 3, 2), (3, 3, 2)].
Remember to not count the blocks that are outside the grid.
most_overlapped_block(1, [(10, 10, 1), (10, 10, 1)]) returns 0.

"""


def most_overlapped_block(grid_width, points):
    lst = [[0]*grid_width for i in range(grid_width)]
    for x, y, z in points:        
        x = grid_width - x
        y = y-1
        
        for i in range(x - z, x + z + 1):
            zzz = abs(z - abs(x - i))
            for j in range(y - zzz, y + zzz + 1):
                if i>=0 and i<grid_width: 
                    if j>=0 and j<grid_width:    
                        lst[i][j] += 1

    return(max(map(max, lst)))




most_overlapped_block(10, [(3, 3, 3), (1, 1, 4)]) #➞ 2

#most_overlapped_block(10, [(5, 5, 2), (1, 1, 1)]) #➞ 1

#most_overlapped_block(10, [(1, 1, 1), (1, 1, 2), (1, 1, 3)]) #➞ 3