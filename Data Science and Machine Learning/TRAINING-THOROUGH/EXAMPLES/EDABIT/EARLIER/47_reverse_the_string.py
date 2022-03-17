"""
Reverse the String (with a catch)
Create a function that takes a string and returns the reversed string. However there's a few rules to follow in order to make the challenge interesting:

The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
Spaces must be kept in the same order as the original string (see example #3).
Examples
special_reverse_string("Edabit") ➞ "Tibade"

special_reverse_string("UPPER lower") ➞ "REWOL reppu"

special_reverse_string("1 23 456") ➞ "6 54 321"
"""

def special_reverse_string(txt):
    a = list(txt)
    l=len(a)
    t=list("".join(txt.split() ))[::-1]
    ALF=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alf = list("abcdefghijklmnopqrstuvwxyz")
    ALFalf = ALF + alf
    b = []    
    for i in range(l):
        if a[0] == " ":
            b.append(" ")
        elif a[0] in ALF:        
            if t[0] in (ALFalf):
                b.append(t[0].upper())
                t = t[1:]
            elif not t[0] in (ALFalf):
                b.append(t[0])
                t = t[1:]
        else: 
            if t[0] in (ALFalf):
                b.append(t[0].lower())
                t = t[1:]
            elif not t[0] in (ALFalf):
                b.append(t[0])
                t = t[1:]              
        a = a[1:]
    return("".join(b))



#special_reverse_string('Edabit') #, 'Tibade')
#special_reverse_string('UPPER lower') #, 'REWOL reppu')
#special_reverse_string('1 23 456') #, '6 54 321')
#special_reverse_string('Hello World!') #, '!dlro Wolleh')
special_reverse_string("Where's your dog Daisy?") #, "?ysiadg odru oys 'erehw")
#special_reverse_string('addition(3, 2) = 5') #, '5=)2,3(noit id d a')
#special_reverse_string("It's known that CSS means Cascading Style Sheets") #, "Stee hsely tsgn IDA csacs Naemsscta Htnwo Nks'ti")                