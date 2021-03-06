"""
QUESTION:
This is an interview question asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5. 
"""

def adj_max(lst):
    
    if len(lst) == 0: return 0
    else : return max(adj_max(lst[1:]), lst[0] + adj_max(lst[2:]))    
        

adj_max([2, 4, 6, 2, 5])