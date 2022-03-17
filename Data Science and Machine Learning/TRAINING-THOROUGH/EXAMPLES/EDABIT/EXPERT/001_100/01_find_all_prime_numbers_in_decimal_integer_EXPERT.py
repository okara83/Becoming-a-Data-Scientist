"""
Find All Prime Numbers in Decimal Integer
Create a function that takes an integer argument and returns a list of prime numbers found in the decimal representation of that number.

For example, extract_primes(1717) returns [7, 7, 17, 17, 71].

The list should be in acending order. If a prime number appears more than once, every occurance should be listed. 
If no prime numbers are found, return an empty list.

Examples
extract_primes(1) ➞ []

extract_primes(7) ➞ [7]

extract_primes(73) ➞ [3, 7, 73]

extract_primes(103) ➞ [3]

extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]
Notes
All test cases are positive real integers.
Some numbers will have leading zeros. For example, the number 103 contains the prime number 3, but also contains 03. 
These should be treated as the same number, so the result would simply be [3].

Test.assert_equals(extract_primes(1), [])
Test.assert_equals(extract_primes(2), [2])
Test.assert_equals(extract_primes(3), [3])
Test.assert_equals(extract_primes(13), [3, 13])
Test.assert_equals(extract_primes(101), [101])
Test.assert_equals(extract_primes(313), [3, 3, 13, 31, 313])
Test.assert_equals(extract_primes(10234), [2, 3, 23])

"""

def extract_primes(num):
    
    a = []
    b = []
    ln = len(list(str(num)))
    
    if ln == 1:
        a.append(num)
        
    if ln > 1:
        for i in range(1,ln+2):
            for n in range(ln+1-i):
                a.append("".join(list(str(num))[n:n+i]))
    d = []
    e = []
    for n in a:
        
        if str(n)[0] != "0":
            d.append(int(n))
        else:
            e.append(int(n))
    
    for m in e:
        if not m in d:
            d.append(m)
            
    c = (sorted(d))
   
    for k in c:
        if k > 1:
            for i in range(2 , k):
                if (k % i) == 0:
                    break
            else:                
                b.append(k)
    return b

extract_primes(10234)