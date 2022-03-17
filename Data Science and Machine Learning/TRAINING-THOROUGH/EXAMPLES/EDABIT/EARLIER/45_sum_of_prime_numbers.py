"""
Sum of Prime Numbers
Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17

sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87

sum_primes([]) ➞ None
Notes
Given numbers won't exceed 101.
A prime number is a number which has exactly two divisors.
"""
def sum_primes(lst):
    if lst == []: return None 
    a=[]
    for i in lst:
        count=0
        for j in range(1,i+1):
            if not (i%j):
                count +=1
        if count == 2:
            a.append(i)
    return sum(a)        

   

#sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #➞ 17
sum_primes([2, 3, 4, 11, 20, 50, 71]) #➞ 87
#sum_primes([]) #➞ None