"""
Sort the String
Create a function that takes a string consisting of lowercase letters, uppercase letters and numbers and returns the string sorted in the same way as the examples below.

Examples
sorting("eA2a1E") ➞ "aAeE12"

sorting("Re4r") ➞ "erR4"

sorting("6jnM31Q") ➞ "jMnQ136"
Notes
N/A
"""
def sorting(s):
    a="azertyuiopqsdfghjklmwxcvbn"
    u = sorted(list(a.upper()))
    l= sorted(list(a.lower()))
    n ="0123456789"    
    b = []    
    for i in range(len(u)):
        if l[i] in s:
            b.append(l[i])
        if u[i] in s:
            b.append(u[i])
    for i in range(len(n)):
        if n[i] in s:
            b.append(n[i])          
    return ("".join(b))
    
sorting("eA2a1E") #➞ "aAeE12"
#sorting("Re4r") #➞ "erR4"
#sorting("6jnM31Q") #➞ "jMnQ136"
#sorting("f5Eex")  #, "eEfx5")
#sorting("846ZIbo")  #, "bIoZ468")
#sorting("2lZduOg1jB8SPXf5rakC37wIE094Qvm6Tnyh")  #, "aBCdEfghIjklmnOPQrSTuvwXyZ0123456789")
