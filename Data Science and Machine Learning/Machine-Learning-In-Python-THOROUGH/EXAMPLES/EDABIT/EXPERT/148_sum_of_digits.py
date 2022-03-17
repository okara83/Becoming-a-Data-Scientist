"""
https://edabit.com/challenge/K7NbqZBYD5xzZLro9        EXPERT----



Sum of Digits
Create a function that takes a range of numbers and returns the sum of each digit from start to stop.

Examples
digits_sum(1, 10) ➞ 46
# total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46

digits_sum(1, 20) ➞ 102

digits_sum(1, 100) ➞ 901
Notes
start and stop are inclusive in the range.
"""

import math
def sum_d(n):
    if n<10:
        return n*(n+1)//2
    logn=int(math.log10(n))
    p= 10**logn #pow(10,d)
    coff=n//p
    return (coff*45*logn*10**(logn-1))+(coff*(coff-1)//2*p)+(coff*(1+n%p)+sum_d(n%p))

def digits_sum(start, stop):
	return sum_d(stop)-sum_d(start-1)
    
    
#digits_sum(1, 20) #➞ 102

digits_sum(1, 100) #➞ 901
digits_sum(1, 100000000) #, 3600000001)