"""
https://edabit.com/challenge/Z2mhqFLe9g9ouZY64

Validate Subsequences   EXPERT
Given two non-empty lists, write a function that determines whether the second list is a subsequence of the first list.

For instance, the numbers [1, 3, 4] form a subsequence of the list [1, 2, 3, 4], and so do the numbers [2, 4].

Examples
is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) ➞ False

is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) ➞ True

is_valid_subsequence([1, 2, 3, 4], [2, 4]) ➞ True

"""

def is_valid_subsequence(lst, sequence):
    for i in sequence:
        if i in lst: lst = lst[lst.index(i) + 1:]            
        else:return False
    return True


#is_valid_subsequence([1, 1, 6, 1],[1, 1, 1, 6]) #➞ False

#is_valid_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6]) #➞ True

is_valid_subsequence([1, 2, 3, 4], [2, 4]) #➞ True