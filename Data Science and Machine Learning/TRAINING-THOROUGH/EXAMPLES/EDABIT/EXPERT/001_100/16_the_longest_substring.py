"""
The Longest Substring
Given a string of letters, create a function that returns a list with the separator that yields the longest possible substring, provided that:

the substring starts and ends with the separator, and
the separator doesn't occur inside the substring other than at the ends.
If two or more separators yield substrings with the same length, they should appear in alphabetical order.

Examples
max_separator('supercalifragilistic') ➞ ['s']
# The longest substring is 'supercalifragilis'

max_separator('laboratory') ➞ ['a', 'o', 'r']
# 'abora', 'orato' and 'rator' are the same length

max_separator('candle') ➞ []
# No possible substrings
Notes
All substrings should be at least of length 2 (i.e., no single-letter substrings).
Expect lowercase alphabetic characters only.
"""
def max_separator(lst):
    
    a = list(lst)
    c,d,e,f,g=[],[],[],[],[]   
    for p in range(len(a)):
        k = str("c"+str(p))
        k= []
        c.append(k)    
    for i in range(len(c)):
        c[i].append(a[i])
        for j in range(i+1,len(c)):
            c[i].append(a[j])          
            if a[j] == a[i]:
                d.append(c[i])
                break
    if len(d)==0:
        return []    
    ds = sorted(d,key=len,reverse=True)
    for i in ds:
        e.append(len(i))    
    f.append(e[0])
    for i in range(1,len(e)):
        if (e[i-1])!=(e[i]):
            break
        f.append(e[i])    
    for i in range(len(f)):
        g.append(ds[i])
    result = []
    for i in range(len(g)):
        result.append(sorted(g)[i][0])
    return result

max_separator('transmissive')  #, ['i', 's']
#max_separator('acquaintance')   #, ['c']
#max_separator('supercalifragilistic') #➞ ['s']
#max_separator('laboratory') #➞ ['a', 'o', 'r']
#max_separator('candle') #➞ []