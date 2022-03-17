"""
https://edabit.com/challenge/H7Z8enQWipfBMXTx7      EXPERT

Recursion: Fibonacci String
A Fibonacci string is a precedence of the Fibonacci series. It works with any two characters of the English alphabet (as opposed to the numbers 0 and 1 in the Fibonacci series) as the initial items and concatenates them together as it progresses similarly to that of the Fibonacci series.

Examples
fib_str(3, ["j", "h"]) ➞ "j, h, hj"

fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"
Notes
All values for n will be at least 2.
It is expected from the challenge-takers to come up with a solution using the concept of recursion or the so-called recursive approach.
You can read more topics about recursion (see Resources tab) if you aren't familiar with it yet or hasn't fully understood the concept behind it before taking up this challenge or unless otherwise.
An iterative version of this challenge can be found via this link.

"""
def fib_str(n, f):
    return ', '.join(f) if len(f) == n else fib_str(n, f + [f[-1]+f[-2]])

fib_str(3, ["j", "h"]) #➞ "j, h, hj"
fib_str(5, ["e", "a"]) #➞ "e, a, ae, aea, aeaae"
fib_str(6, ["n", "k"]) #➞ "n, k, kn, knk, knkkn, knkknknk"