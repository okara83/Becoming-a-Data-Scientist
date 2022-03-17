"""
https://edabit.com/challenge/88WesDgd2Ge9JEiJM

Almost Uniform Sequence
Find the length of the longest sub-sequence of two distinct numbers whose difference is 1. 
A sub-sequence can be made by deleting any numbers in between.

Examples
almost_uniform([1, 3, 2, 2, 5, 2, 3, 7]) ➞ 5
# [3, 2, 2, 2, 3]

almost_uniform([1, 2, 3, 4]) ➞ 2
# [1, 2] or [2, 3] or [3, 4]

almost_uniform([1, 1, 1, 1]) ➞ 0
# There is no sub-sequence of two distinct numbers.
Notes
N/A
"""
def almost_uniform(nums):
    lst, a, b = list(set(nums)), [], []
    nums.sort()
    lst.sort()
    for i in range(len(lst)): 
        a.append([])
        for j in range(nums.index(lst[i]),len(nums)):
            if nums[j] - lst[i] in [0,1]: a[i].append(nums[j])
            else: break  
    for i in a:
        if len(set(i))>1: b.append(len(i))
    if len(b)==0: return 0
    return max(b)

#almost_uniform([1, 3, 2, 2, 5, 2, 3, 7]) #➞ 5
# [3, 2, 2, 2, 3]
#almost_uniform([1, 2, 3, 4]) #➞ 2
# [1, 2] or [2, 3] or [3, 4]
#almost_uniform([1, 1, 1, 1]) #➞ 0
almost_uniform([-3, 7, 9, 1, -2, 9, 7, 1, -2, 9, -3, 9, 2, 7, 2, 9, 1, 9, 2, 7, -2, 1, 7, 2, 9, 7, 9, -3, 7, -3, 9, 7, 9, -3, 7, -2, 7]) #, 9)
