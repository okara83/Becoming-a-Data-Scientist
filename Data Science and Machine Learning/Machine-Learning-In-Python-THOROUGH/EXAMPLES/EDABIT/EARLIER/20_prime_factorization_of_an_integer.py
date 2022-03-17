"""
Prime Factorization of an Integer
Create a function that returns a list containing the prime factors of whatever integer is passed to it.

Examples
prime_factors(20) ➞ [2, 2, 5]

prime_factors(100) ➞ [2, 2, 5, 5]

prime_factors(8912234) ➞ [2, 47, 94811]
Notes
Implement your solution using trial division.
Your solution should not require recursion.
"""
def prime_factors(num):

    a = []
    
    for i in range(2,num+1):
        while num>2:
            if num%i == 0:
                num = num /i
                a.append(i)
            else:
                break
    return (a)

    
#prime_factors(20) #➞ [2, 2, 5]
prime_factors(100) #➞ [2, 2, 5, 5]
#prime_factors(8912234) #➞ [2, 47, 94811]