"""
https://edabit.com/challenge/XGKSYNExDBRWLzDmm
Just Another Sum Problem But... 😰😱
Ok, the challenge is kind of easy, right?

The problem is not adding, the problem is that the numbers are not in order, create a function that organizes the numbers and adds the numbers in the range between X and Y.

Here is an example:

X = -10 | Y=1
So this will be the range of numbers:

-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1
This will be your result:

-54
You must sum a number range between X and Y to get the result.

Remember, X and Y are disorganized, so to get to the result you know what you have to do.

"""
def just_another_sum_problem(a, b):
    if a*b < 0:return ((max(a,b)*(max(a,b)+1))//2 - (abs(min(a,b))*(abs(min(a,b))+1))//2)  
    else:return ((max(a,b)*(max(a,b)+1))//2 - (abs(min(a,b))*(abs(min(a,b))-1))//2)  
    
#just_another_sum_problem(13,-1000000000) #, -500000000499999909)
#just_another_sum_problem(-10,1)#, -195   
just_another_sum_problem(7, 1000000000)#, 500000000499999979)