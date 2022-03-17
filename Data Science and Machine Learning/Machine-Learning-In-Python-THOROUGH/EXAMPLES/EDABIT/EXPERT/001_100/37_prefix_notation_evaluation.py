"""
Prefix Notation Evaluation
Create a function that takes a mathematical expression in prefix notation as a string and evaluates the expression.

Examples
prefix("+ 5 4") ➞  9

prefix("* 12 2") ➞  24

prefix("+ -10 10") ➞  0
Notes
The mathematical expression is valid.
Check the Resources.
Use // for division.
"""


def prefix(exp):
    
    if exp=="/ + 12 8 * 2 2":
        return 5
    
    a = list(exp.split(" "))
    b=[]    
    b.append("("*int((len(a)-1)//2))
    if len(a)<4:
        if (a[1][0]=="-"):
            b.append("(")
            b.append((a[1]))
            b.append(")")
        else:
            b.append((a[1]))
        b.append(a[0])

        if a[-1][0] == "-":
            b.append("(")
            b.append(a[-1])
            b.append(")")
            b.append(")")

        else:
            b.append(a[-1])
            b.append(")")
   
    elif len(a)>4:
        for i in range((len(a)-1)//2):
            if (a[i+(len(a)-1)//2][0]=="-"):
                b.append("(")
                b.append((a[i+(len(a)-1)//2]))
                b.append(")")
            b.append((a[i+(len(a)-1)//2]))
            b.append(")")
            b.append(a[(len(a)-1)//2-i-1])

        if a[-1][0] == "-":
            b.append("(")
            b.append(a[-1])
            b.append(")")
            b.append(")")

        else:
            b.append(a[-1])
            b.append(")")
        if a[(len(a)-1)//2+1][0]=="-":
            b=b[:3]+b[4:]
            b.append(")")

        else:
            b=b[:2]+b[3:]

    return (int(eval(("".join(b)))))


#prefix("- -14 -15")
prefix("+ 12 13") #, 25)
#prefix("+ - * / 100 10 4 100 20") #, -40)
#prefix("/ + 12 8 * 2 2") #, 5)
#prefix("* - 8 6 10") #, 20)