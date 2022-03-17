"""
Word Chain 2.0
Let's update our previous word-chain definition. In this 2.0 version, a word-chain is an array of words, where the next word is formed by either:

Changing exactly one letter from the previous word
Adding or subtracting one letter
Note: You can only do one (not both) for each word change.

Examples
isWordChain(["row", "crow", "crown", "brown", "brawn"]) ➞ True
# add "c" to "row" to get "crow", "n" to get "crown", etc. 

isWordChain(["flew", "flaw", "flan", "flat", "fat", "rat", "rot", "tot"]) ➞ True

isWordChain(["meek", "meet", "meat", "teal"]) ➞ False
# "meat" => "teal" changes 2 letters (can only change 1)

isWordChain(["run", "runny", "bunny"]) ➞ False
# "run" => "runny" adds 2 letters (can only add 1)
Notes
All words will be in lower-case.
"""
def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)

def isWordChain(words):
    
    leven= []
    for i in range(len(words)-1):
        leven.append((words[i],words[i+1]))    
    for i in leven:
        (a,b) = i
        if not a: return len(b)
        if not b: return len(a)
        if min(levenshtein(a[1:], b[1:])+(a[0] != b[0]), levenshtein(a[1:], b)+1, levenshtein(a, b[1:])+1)>1: return False
    return True


isWordChain(["row", "crow", "crown", "brown", "brawn"]) #, True)
#isWordChain(["flew", "flaw", "flan", "flat", "fat", "rat", "rot", "tot"]) #, True)
#isWordChain(["meek", "meet", "meat", "teal"]) #, False)
#isWordChain(["run", "runny", "bunny"]) #, False)
#isWordChain(["fun", "fund", "find", "bind", "wind", "wild", "wile", "wiles"]) #, True)
#isWordChain(["nut", "but", "bot", "boot", "loot", "look", "book", "brook"]) #, True)
#isWordChain(["some", "tome", "tame", "lame", "flame", "flamer", "blamer", "blamers"]) #, True)
#isWordChain(["a", "at", "hat", "that", "what", "flat"]) #, False)
#isWordChain(["link", "blink", "wink", "sink"]) #, False)