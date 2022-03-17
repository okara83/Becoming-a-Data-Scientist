"""
Simultaneous Linear Equations
Given two simultaneous linear equations in this form: a*x + b*y = c, d*x + e*y = f, 
devise a function that returns the values of x and y as (x, y). The numbers a through f are non-zero integers. 
If there is not a unique solution or if there is no solution at all, return False. 
Input is given as: [[a, b, c], [d, e, f]]. Solutions, if they exist, will be integers.

Examples
sle([[3, 4, 19], [2, -1, 9]]) ➞ (5, 1)

sle([[3, 2, -2], [2, 5, -5]]) ➞ (0, -1)

sle([[4, -3, 18], [8, -6, 36]]) ➞ False

sle([[2, 3, 13], [5, -1, 7]]) ➞ (2, 3)
Notes
Can you do this without using numpy?

"""
def sle(m):
    a, b, c, d, e, f = m[0][0], m[0][1], m[0][2], m[1][0], m[1][1], m[1][2]
    if (a*e==b*d): return False
    x = (c*e-b*f)/(a*e-b*d)
    y = (a*f-c*d)/(a*e-b*d) 
    return (int(x),int(y))



#sle([[3, 2, -2], [2, 5, -5]]) #➞ (0, -1)
#sle([[1, 2, -1], [2, -3, 5]]) #, (1, -1))
#sle([[3, -4, 1], [2, 3, 12]]) #, (3, 2))
#sle([[1, -4, 12], [3, -12, 36]]) #, False)
#sle([[3, 2, -4], [2, 5, 1]]) #, (-2, 1))
sle([[5, 3, -11], [2, 4, -10]]) #, (-1, -2))
#sle([[3, 1, 38], [3, 1, 83]]) #, False)