"""
https://edabit.com/challenge/zhqL89ZWgbxbixsdD

Recursion: Exact Factorial Bounds
Create a recursive function that tests if a number is the exact upper bound of the factorial of n. 
If so, return a list that contains the exact factorial bound and n, or otherwise, the string "Not exact!".

Examples
is_exact(6) ➞ [6, 3]
is_exact(24) ➞ [24, 4]
is_exact(125) ➞ "Not exact!"
is_exact(720) ➞ [720, 6]
is_exact(1024) ➞ "Not exact!"
is_exact(40320) ➞ [40320, 8]
Notes
It is expected from the challenge-takers to come up with a solution using the concept of recursion or
the so-called recursive approach.
You can read on more topics about recursion (see Resources tab) if you aren't familiar with it yet or 
hasn't fully understood the concept behind it before taking up this challenge or unless otherwise.
There will be no exceptions to handle, all inputs are positive integers.
"""
def factorial_recursive(a):
    if a == 1: return 1
    else: return a * factorial_recursive(a-1)    
def is_exact(n):
    a=1
    while factorial_recursive(a) <=n : a+=1
    if n==factorial_recursive(a-1): return [n,a-1]
    else: return "Not exact!"    
    
#is_exact(24) #➞ [24, 4] 
is_exact(40320) #➞ [40320, 8]
#is_exact(41845579776000)