"""
Change the Word
Given a string, reverse its order, change lowercase letters to uppercase and increment uppercase letters by 1 e.g. 
A becomes B, C becomes D, Z becomes A

Examples
changeString("ApPle") ➞ "ELQPB"

changeString("draGON") ➞ "OPHARD"

changeString("ZebrA") ➞ "BRBEA"
Notes
Remember capital 'Z' becomes 'A'
"""
def changeString(word):
    z=[]
    a="azertyuiopmlkjhgfdsqwxcvbn"
    b=sorted(list(a))
    c=sorted(list(a.upper()))
    d=word[::-1]    
    for i in d:
        if i in a:
            z.append(i.upper())
        elif i in c:
            if i == "Z":
                z.append("A")
            else:
                z.append(c[c.index(i)+1])    
    return ("".join(z))

#changeString("ApPle") #➞ "ELQPB"
#changeString("draGON") #➞ "OPHARD"
changeString("ZebrA") #➞ "BRBEA"