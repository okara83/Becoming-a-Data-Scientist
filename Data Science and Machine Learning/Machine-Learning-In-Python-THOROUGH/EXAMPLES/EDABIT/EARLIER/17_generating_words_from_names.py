"""
Generating Words from Names
Write a function that returns True if a given name can generate an array of words.

Examples
anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True

anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True

anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
# Not all letters are used

anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
# "s" does not exist in the original name
Notes
Each letter in the name may only be used once.
All letters in the name must be used.
"""
def anagram(name, *words):
    
    b = "".join(list(words[0]))
    c = "".join(name)    
    if sorted(b.lower()) == sorted(c.lower())[1:]:
        return True
    return False



#anagram("Justin Bieber", ["injures", "ebb", "it"]) #➞ True
#anagram("Natalie Portman", ["ornamental", "pita"]) #➞ True
#anagram("Chris Pratt", ["chirps", "rat"]) #➞ False
anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) #➞ False