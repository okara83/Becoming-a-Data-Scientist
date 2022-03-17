"""
https://edabit.com/challenge/KjCnfEm8WzJcnuPYt

Indices of Zeroes for the Longest Run of Contiguous Ones
You are given a list of binary integers and k, the number of flips allowed.

Write a function that returns the indices of zeroes of which, when flipped, 
return the longest contiguous sequence of ones.

Examples
zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) ➞ [1]

zero_indices([1, 0, 0, 0, 0, 1], 1) ➞ [1]

zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) ➞ [6, 7, 9]

zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) ➞ [7, 8, 9]
Notes
If multiple combinations of indices tie for longest one sequence, 
return the indices which occur first (see examples #2, #3).


"""

def zero_indices(lst, k):
    
    start, count, block = 0, 0, 0  
    index = 0  
    for i in range(len(lst)):

        if lst[i] == 0: count = count + 1
        while count > k:
            if lst[start] == 0: count = count - 1
            start += 1
        if i - start + 1 > block:
            block = i - start + 1
            index = start    
    rr=[]
    for i in range(index, index + block):
        if lst[i] == 0: rr.append(i)
    
    return (rr)



#zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) #➞ [1]
#zero_indices([1, 0, 0, 0, 0, 1], 1) #➞ [1]
zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) #➞ [6, 7, 9]
#zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) #➞ [7, 8, 9]