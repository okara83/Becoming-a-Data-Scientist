"""
https://edabit.com/challenge/SQZoHFDfizBTP4HSx

Find Missing Alphabets
Create a function that takes a string txt containing only letters from a to z in lowercase and returns the missing letter(s) in alphabetical order a-z.

A set of letters is given by abcdefghijklmnopqrstuvwxyz.
Two sets of alphabets means two or more alphabets.
Examples
missing_alphabets("abcdefghijklmnopqrstuvwxy") ➞ "z"
# "z" is missing.

missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") ➞ "zz"
# Given string has a set of two alphabets so output will be "zz"

missing_alphabets("edabit") ➞ "cfghjklmnopqrsuvwxyz"
Notes
If the string contains all letters from a-z, return an empty string "".
"""
def missing_alphabets(txt):
    a="abcdefghijklmnopqrstuvwxyz"
    b,c,s = [], [], sorted(list(set(txt)))
    for i in txt:c.append(txt.count(i))
    cnt=max(c)
    for i in a: b.append(i*cnt)
    b= (list("".join(b)))    
    for i in txt:
        if i in b :b.remove(i)
    if len(b)==0 : return ""
    return "".join(b)

#missing_alphabets("abcdefghijklmnopqrstuvwxy") #➞ "z"
#missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") #➞ "zz"
#missing_alphabets("edabit") #➞ "cfghjklmnopqrsuvwxyz"
missing_alphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy")  #,"ayzz"