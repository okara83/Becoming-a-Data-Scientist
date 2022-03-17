"""
QUESTION:
This is an interview question asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.
"""
def sum10(n):
    perf=[]
    x=0
    while len(perf)<n:
        if sum([int(a) for a in str(x)])==10: perf.append(x)
        x+=1       
    return perf[n-1]

sum10(2)