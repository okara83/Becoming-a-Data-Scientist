"""
Solve a Linear Equation
Create a function that returns the value of x (the "unknown" in the equation). Each equation will be formatted like this:

x + 6 = 12
Examples
solve("x + 43 = 50") ➞ 7

solve("x - 9 = 10") ➞ 19

solve("x + 300 = 100") ➞ -200
Notes
"x" will always be in the same place (you will not find an equation like 6 + x = 12).
Every equation will include either subtraction (-) or addition (+).
"x" may be negative.
"""
def solve(eq):
    
    a= eq.split(" ")
    if a[1] == "+":
        return int(a[4]) - int(a[2])
    if a[1] == "-":
        return int(a[4]) + int(a[2])        
    




#solve("x + 43 = 50") #➞ 7
solve("x - 9 = 10") #➞ 19
#solve("x + 300 = 100") #➞ -200
