"""
Economical Numbers
A number is Economical if the quantity of digits of its prime factorization (including exponents greater than 1) is equal to or lower than the digit quantity of the number itself.

Given an integer n, implement a function that returns a string:

"Equidigital" if the quantity of digits of the prime factorization (including exponents greater than 1) is equal to the quantity of digits of n;
"Frugal" if the quantity of digits of the prime factorization (including exponents greater than 1) is lower than the quantity of digits of n;
"Wasteful" if none of the two above conditions is true.
Examples
is_economical(14) ➞ "Equidigital"
# The prime factorization of 14 (2 digits) is [2, 7] (2 digits)
# Exponents equal to 1 are not counted

is_economical(125) ➞ "Frugal"
# The prime factorization of 125 (3 digits) is [5^3] (2 digits)
# Notice how exponents greater than 1 are counted

is_economical(1024) ➞ "Frugal"
# The prime factorization of 1024 (4 digits) is [2^10] (3 digits)

is_economical(30) ➞ "Wasteful"
# The prime factorization of 30 (2 digits) is [2, 3, 5] (3 digits)
Notes
Any given n will be a positive integer greater than 1.
Remember to count also the exponents greater than 1 into the prime factorization: 2¹ = 2 (one digit), 2² = 22 (two digits), 2¹° = 210 (three digits)...
"""

def is_economical(n):
    
    ln = len(list(str(n)))
  
    nums = set(range(n, 1, -1))
    primes, power = [], []
    while nums:
        p = nums.pop()
        primes.append(p)
        nums-=set(range(p * 2 , n + 1 , p))
    
    prim_fact = [i for i in primes if not n%i]


    count = 0
    for i in prim_fact:
        while (not n % i):
            n = n / i
            count = count +1
        power.append(count)
        count = 0
    
    rr,ss = [],[]
    for i in range(len(power)):
        if (power[i]) == 1:
            rr.append(prim_fact[i])
        else:
            rr.append(prim_fact[i])
            rr.append(power[i])
    
    for i in rr:
        ss.append(str(i))
    
    if ln == len(("".join(ss))):
        return "Equidigital"
    elif ln > len(("".join(ss))):
        return "Frugal"
    elif ln < len(("".join(ss))):
        return "Wasteful"    

is_economical(1267)