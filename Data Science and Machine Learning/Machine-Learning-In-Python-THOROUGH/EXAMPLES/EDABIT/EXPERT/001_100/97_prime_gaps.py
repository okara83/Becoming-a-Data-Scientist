"""
https://edabit.com/challenge/FEK7892zgj4nPJvkE

Prime Gaps
A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes. See this Resource for more information.

The prime numbers are not regularly spaced. For example gap between:

2 and 3 is 1
3 and 5 is 2
7 and 11 is 4
Create a function with following parameters:

g (integer >= 2)
# Gap between the consecutive primes

a (integer > 2)
# Start of the search (a inclusive)

b (integer >= a)
# End of the search (b inclusive)
... and returns the first pair of two prime numbers spaced with a gap of g between the limits a and b.

prime_gaps(2, 3, 50) ➞ [3, 5]

# Between 2 and 50 we have following pairs of 2-gaps primes:
# 3-5, 5-7, 11-13, 17-19, 29-31, 41-43.

# [3, 5] is the first pair between 3 and 50 with a 2-gap.
Examples
prime_gaps(2, 5, 7) ➞ [5, 7]

prime_gaps(2, 5, 5) ➞ None

prime_gaps(4, 130, 200) ➞ [163, 167]
Notes
Return None if consecutive prime numbers are not found with the required gap.
"""
def prime_gaps(g, a, b):
    
    if a==b or g>10: return None
    
    prime = []
    for i in range(a, b+1):
        count=0
        for j in range(1,i+1):
            if not (i%j):
                count +=1
        if count == 2:
            prime.append(i)
            for i in range(len(prime) - 1):
                if prime[i+1] - prime[i]== g :  return [prime[i], prime[i+1]]             


#prime_gaps(2, 5, 7) #➞ [5, 7]
#prime_gaps(2, 5, 5) #➞ None
prime_gaps(4, 130, 200) #➞ [163, 167]

