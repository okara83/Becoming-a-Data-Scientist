"""
3D Visual Block Sequence
A block sequence in three dimensions. We can write a formula for this one:

Sequence Step 1 - 5

Create a function that takes a number (step) as an argument and returns the amount of blocks in that step.

Examples
blocks(1) ➞ 5

blocks(5) ➞ 39

blocks(2) ➞ 12
Notes
Step 0 obviously has to return 0.
The input is always a positive integer.
"""
def blocks(step):
    if step == 0:
        return 0
    return ((step**2)/2 + (11*step)/2 - 1)
    
    
    
    
    
    
#blocks(1) #➞ 5
blocks(77) #➞ 39
#blocks(2) #➞ 12