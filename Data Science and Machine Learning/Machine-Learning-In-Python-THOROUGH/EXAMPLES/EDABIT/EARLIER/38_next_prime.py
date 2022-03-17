"""
Next Prime
Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

Examples
next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
"""
def next_prime(num):
  
    prime = []
    for i in range(num, num*2):
        count = 0
        for k in range(1,i+1):
            if not (i % k) : count +=1
        if count == 2:
            prime.append(i)
    return (prime[0])


#next_prime(12) #, 13)
#next_prime(24) #, 29)
#next_prime(11) #, 11)
#next_prime(13) #, 13)
#next_prime(14) #, 17)
next_prime(33) #, 37)