"""
Connecting Words
Write a function that connects each previous word to the next word by the shared letters. Return the resulting string (removing duplicate characters in the overlap) and the minimum number of shared letters across all pairs of strings.

Examples
join(["oven", "envier", "erase", "serious"]) ➞ ["ovenvieraserious", 2]

join(["move", "over", "very"]) ➞ ["movery", 3]

join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", 1]

# "to" and "ops" share "o" (1)
# "ops" and "psy" share "ps" (2)
# "psy" and "syllable" share "sy" (2)
# the minimum overlap is 1

join(["aaa", "bbb", "ccc", "ddd"]) ➞ ["aaabbbcccddd", 0]
Notes
More specifically, look at the overlap between the previous words ending letters and the next word's beginning letters.
"""
def join(lst):
    a, b, c, d, e = [], [], [], [], []
    for i in range(len(lst)):
        a.append(list(lst[i]))
    b=a    
    for i in range(1,len(a)):
        for j in range(min(len(a[i]),len(a[i-1]))+1):            
            if a[i][:j] == a[i-1][-j:]:
                c.append(j)
                b[i]=b[i][j:]
                a[i]=a[i-1]+b[i]
    if len(c)==0 : 
        d.append("".join(lst))
        d.append(0)
        return d
        
    e.append("".join(b[-1]))
    e.append((min(c)))
    return e




#join(["oven", "envier", "erase", "serious"]) #➞ ["ovenvieraserious", 2]
#join(["move", "over", "very"]) #➞ ["movery", 3]
#join(["to", "ops", "psy", "syllable"]) #➞ ["topsyllable", 1]
#join(["aaa", "bbb", "ccc", "ddd"]) #, ["aaabbbcccddd", 0])
join(["abcde", "bcdefghi", "efghi", "fghij", "ghijklmnop"]) #, ["abcdefghijklmnop", 4])