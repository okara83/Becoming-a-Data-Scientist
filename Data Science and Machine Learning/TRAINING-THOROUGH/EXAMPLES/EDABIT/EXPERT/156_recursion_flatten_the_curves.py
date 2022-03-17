"""
https://edabit.com/challenge/2nciiXZN4HCuNEmAi      EXPERT------


Recursion: Flatten the Curves
The nesting of lists can be viewed indirectly as curves and barriers of the real data embedded in lists, thus, defeats the very purpose of directly accessing them thru indexes and slices. In this challenge, a function is required to flatten those curves (i.e. level, iron, compress, raze, topple) and expose those data as a single list and not as a list of lists.

Examples
flatten([[[[[["direction"], [372], ["one"], [[[[[["Era"]]]], "Sruth", 3337]]], "First"]]]])
➞ ["direction", 372, "one", "Era", "Sruth", 3337, "First"]

flatten([[4666], [5394], [466], [[["Saskia", [[[[["DXTD"]], "Lexi"]]]]]]])
➞ [4666, 5394, 466, "Saskia", "DXTD", "Lexi"]

flatten([[696], ["friend"], ["power"], [[[["Marcus"]]]], ["philus"]])
➞ [696, "friend", "power", "Marcus", "philus"]

flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])
➞ ["deep", "ocean", "Marge", "rase", 876]
Notes
There are no empty lists to handle.
You're expected to solve this challenge using a recursive approach.
You can read on more topics about recursion (see Resources tab) if you aren't familiar with it yet or haven't fully understood the concept behind it before taking up this challenge.
"""
def flatten(r):
    if r == []: return []
    if isinstance(r[0], list): return flatten(r[0]) + flatten(r[1:])
    return r[:1] + flatten(r[1:])

flatten([[["deep"], [[["ocean"]]], [["Marge"]], ["rase", 876]]])