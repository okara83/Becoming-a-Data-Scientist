"""
https://edabit.com/challenge/L2nw2N2YqZCboiaYM

Repeated Sub-String Pattern
Create a solution that checks if a given string contains a sub-string pattern repeated multiple times to return True or False.

Examples
repeated("a") ➞ False

repeated("ababab") ➞ True

repeated("aba") ➞ False

repeated("abcabcabcabc") ➞ True

repeated("aaxxtaaxztaaxxt") ➞ False

"""
def repeated(s):
    
    for i in range(2,len(s)//2+1):
        if not len(s)%i==0: continue
        a=[]
        for j in range(len(s)//i):
            if s[i*j:i*j+i]==s[:i]: a.append(1)
            else:a.append(0)
        if sum(a)==len(a): return True    
    return False



#repeated("a") #, False)
#repeated("ababab") #, True)
#repeated("aba") #, False)
#repeated("abcabcabcabc") #, True)
repeated("aaxxtaaxztaaxxt") #, False)