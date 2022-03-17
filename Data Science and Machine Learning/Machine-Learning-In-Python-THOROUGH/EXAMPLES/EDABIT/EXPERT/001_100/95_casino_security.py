"""
https://edabit.com/challenge/2jcxK7gpn6Z474kjz

Casino Security
You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.

If there is no guard between thief and money, return "ALARM!"
If the money is protected, return "Safe"
String Components
x - Empty Space
T - Thief
G - Guard
$ - Money
Examples
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
"""
# SOLUTION WITHOUT REGEX!!!

def security(txt):
    
    a, x, T, G, S = [], [], [], [], []
    
    for i in txt: 
        if i != "x": a.append(i)
    
    for i in range(len(a)):
        if a[i]=="T": T.append(i)
        elif a[i]=="G": G.append(i)    
        elif a[i]=="$": S.append(i)    
    
    if len(T) == 0 or len(S)==0: return "Safe"

    for i in T:
        for j in S:
            if abs(i-j) == 1: return "ALARM!"

    return "Safe"

security("xxTxxx$xxxTxxxGxxT")#, "ALARM!")
#security("xxxxTTxGxx$xxTxxx") #➞ "ALARM!"
#security("xxTxxG$xxxx$xxxx") #➞ "Safe"
#security("TTxxxx$xxGxx$Gxxx") #➞ "ALARM!"
#security("xxxTxxxxT")#, "Safe")
#security("xxGxxxGGG")#, "Safe")
#security("x$xx$x$x$xx")#, "Safe")