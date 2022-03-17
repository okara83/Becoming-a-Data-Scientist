"""
QUESTION:
This is an interview question asked by Amazon.
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
"""
def staircase(s):
    return n if s <= 3 else (staircase(s-1) + staircase(s-2))
staircase(4)