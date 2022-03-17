"""
Point within Triangle
Create a function that takes four tuples. The first three are (x, y) coordinates of three corners of a triangle. Return True if the fourth tuple — the (x, y) coordinates of a test point — lies within the triangle, False if it doesn't.

Examples
within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) ➞ True

within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) ➞ False

within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) ➞ True
Notes
N/A


"""
def within_triangle(p1, p2, p3, test):
    x1,y1,x2,y2,x3,y3,x,y=p1[0],p1[1],p2[0],p2[1],p3[0],p3[1],test[0],test[1]
    d=((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / d
    b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / d
    c = 1 - a - b    
    if (0<=a<=1) and (0<=b<=1) and (0<=c<=1):return True
    else: return False    

#within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) #, True)
#within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) #, False)
#within_triangle((1, 7), (2, 4), (9, 3), (2, 6)) #, True)
#within_triangle((1, 7), (2, 4), (9, 3), (6, 5)) #, False)
within_triangle((-2, 6), (12, -3), (1, 7), (9, -1)) #, True)
#within_triangle((-2, 6), (12, -3), (1, 7), (4, 2)) #, False)
#within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) #, True)
#within_triangle((-6, 2), (-2, -2), (8, 4), (0, -4)) #, False)