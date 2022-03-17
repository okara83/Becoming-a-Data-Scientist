"""
Product of Two Prime Numbers
Write a function that returns True if the given number num is a product of any two prime numbers.

Examples
product_of_primes(2059) ➞ True
# 29*71=2059

product_of_primes(10) ➞ True
# 2*5=10

product_of_primes(25) ➞ True
# 5*5=25

product_of_primes(999) ➞ False
# There are no prime numbers.
Notes
num is always greater than 0.
0 and 1 aren't prime numbers.
"""
def product_of_primes(n):
    
    pri = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if pri[i//2]:
            pri[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    a= [2] + [2*i+1 for i in range(1,n//2) if pri[i]]

    for i in a:
        for j in a:
            if (i * j) == n:
                return True
    return False

#product_of_primes(2059) #, True)
#product_of_primes(7) #, False)
#product_of_primes(25) #, True)
#product_of_primes(39) #, True)
product_of_primes(5767) #, True)
#product_of_primes(77) #, True)
#product_of_primes(12) #, False)