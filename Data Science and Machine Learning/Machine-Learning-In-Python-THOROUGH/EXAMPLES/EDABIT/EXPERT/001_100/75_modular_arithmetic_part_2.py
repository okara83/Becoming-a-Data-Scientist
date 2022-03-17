"""
https://edabit.com/challenge/zbqRGhB3sTDPgySiv

Modular Arithmetic (Part #2)
Modify the inefficient code in the Code tab so it can pass the tests.

Examples
mod(1, 1) ➞ 0

mod(5, 5) ➞ 34

mod(13, 27 ) ➞ 522956314

mod(8000, 30) ➞ 9157958657951075573395300940314
Notes
The variables will be natural numbers.
If necessary, there is a hint in the Tests tab.
"""
from math import factorial

def mod(base, key):
    k=(min(base,key))
    loop = 0
    key = factorial(key)
    for i in range(k):
        loop += factorial(i) % key
    return loop % key


#mod(5, 5) #, 34)
#mod(13, 27) #, 522956314)
#mod(8000, 30) #, 9157958657951075573395300940314)
mod(1000001, 42) #, 34289376947494122614363304694584807557656420940314)