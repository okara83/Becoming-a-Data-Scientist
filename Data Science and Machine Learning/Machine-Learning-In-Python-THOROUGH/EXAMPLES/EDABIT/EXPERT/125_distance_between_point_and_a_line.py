"""
https://edabit.com/challenge/JHubqEB54KxbWP3sR   EXPERT ----

Distance between Point and a Line
Given the formula for a straight line y = ax + b and the x, y coordinates of a point, find the distance between that point and the line. Round the result to two decimal points.

Examples
dist("y=(-3/4)x-5/4", 5, 2) ➞ 5.6

dist("y=(5+1/3)x-2.3", 1, 4) ➞ 0.18

dist("y=2.2x-(3+1/5)", 3, -2) ➞ 2.23
"""
def dist(line, r, s):

    # ax + by + c = 0
    a = eval(line.split("x")[0].split("=")[-1])
    b = -1
    c = eval(line.split("x")[1])    
    
    return round(abs(a*r+b*s+c)/((a**2+b**2)**.5),2)
    

#dist("y=(-3/4)x-5/4", 5, 2) #➞ 5.6
#dist("y=(5+1/3)x-2.3", 1, 4) #➞ 0.18
dist("y=2.2x-(3+1/5)", 3, -2) #➞ 2.23