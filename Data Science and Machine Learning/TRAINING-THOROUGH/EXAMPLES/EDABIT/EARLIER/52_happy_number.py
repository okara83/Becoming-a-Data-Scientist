"""
https://edabit.com/challenge/rGAcibgZ6u9MtasfW
Happy Number
A happy number is a number which yields a 1 by repeatedly summing up the square of its digit. If such a process results in an endless cycle of numbers containing 4, the number is said to be an unhappy number.

Create a function that accepts a number and determines whether the number is a happy number or not. Return True if so, False otherwise.

Examples
is_happy(67) ➞ False

is_happy(89) ➞ False

is_happy(139) ➞ True

is_happy(1327) ➞ False

is_happy(2871) ➞ False

is_happy(3970) ➞ True
Notes
Hint: Your loop terminates if the value of n is either 1 or 4.
"""

def is_happy(n):
    
    for k in range(7):
        if n == 1: return True
        a=[]
        for i in (str(n)):
            a.append(int(i)**2)
        n=sum(a)
    return False
#is_happy(67) #➞ False

#is_happy(89) #➞ False

#is_happy(139) #➞ True

#is_happy(1327) #➞ False

#is_happy(2871) #➞ False

is_happy(3970) #➞ True