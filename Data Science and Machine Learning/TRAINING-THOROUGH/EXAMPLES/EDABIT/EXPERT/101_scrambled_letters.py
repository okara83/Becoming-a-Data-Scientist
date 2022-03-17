"""
Scrambled Letters
Write a function that receives a list of words and a mask. Return a list of words, sorted alphabetically, that match the given mask.

Examples
scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]

scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]
Notes
The length of a mask will never exceed the length of the longest word in the word list.
"""

recede = ["cee","dee","eer","erd","ere","red","ree","cede","cere","cree","deer","dere","dree","rede","reed","ceder","cedre","cered","creed","decree","recede"]

def scrambled(words, mask): 
    a,c,d =[], [], []
    for i in words:
        if len(i)==len(mask): 
            a.append(i)
            d.append(1)

    if mask.count("*")==len(mask): return(a) 

    for i in range(len(a)):
        for j in range(len(a[i])):
            if mask[j]!="*" and a[i][j]!= mask[j]: d[i]=0
    for i in range(len(a)):
        if d[i]: c.append(a[i])
            
    return c 

#scrambled(recede, "*re**")#, ["creed"])
#scrambled(recede, "***")#, ["cee","dee","eer","erd","ere","red","ree"])
#scrambled(recede, "******")#, ["decree","recede"])
scrambled(recede, "c*d**")#, ["ceder","cedre"])
#scrambled(recede, "d***")#, ["deer","dere","dree"])
#scrambled(recede, "r***")#, ["rede","reed"])