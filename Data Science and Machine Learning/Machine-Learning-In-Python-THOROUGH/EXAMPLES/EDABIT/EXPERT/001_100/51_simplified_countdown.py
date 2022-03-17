"""
Simplified Countdown
Many British visitors to edabit will be familiar with Countdown, a quiz program that ran for many years on UK television. 
One of its challenges required contestants to come up with an expression (using some randomly generated numbers) 
to meet or get as close as possible to a chosen target number.

This challenge is a simplified version of that. Write a function that takes in a tuple of unique positive integers
and a target positive integer and returns a string containing an expression that combines the numbers in the
tuple so that they meet the target, subject to certain rules explained in the notes below.

Examples
countdown((1, 2), 3) ➞ "1+2"

countdown((2, 3, 5, 75), 158) ➞ "3+5+2*75"
Notes
The tuple of operands consists of a minimum of 2 and a maximum of 5 unique positive integers presented in ascending order. An acceptable answer must use each operand once only, combining to meet the target.
The operators to use are the standard Python arithmetic operators: +, -, * and //. Normal operator precedence rules apply. Do not use parentheses.
Each puzzle has at least one answer which meets the above criteria. In the tests, a checker function checks that the expression returned evaluates to the target and that the rules on operands and operators are met.
"""

def countdown(operands, target):
    op=list(operands)
    v, w, x, y= [], [], [], ["+", "-", "*", "//"]
    t=["1"]
    if len(op)==2:
        for a in op:
            for b in op:
                x.append([str(a),str(b)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]       
            for p in y:
                    x[i][1]=p
                    if eval("".join(x[i]))==target:
                        return("".join(x[i]))  

    if len(op)==3:
        for a in op:
            for b in op:
                for c in op:
                    x.append([str(a),str(b),str(c)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]+t+[x[i][2]]        
            for p in y:
                    for q in y:
                        x[i][1],x[i][3]=p,q
                        if eval("".join(x[i]))==target:
                            return("".join(x[i])) 
    if len(op)==4:
        for a in op:
            for b in op:
                for c in op:
                    for d in op:
                        x.append([str(a),str(b),str(c),str(d)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]+t+[x[i][2]]+t+[x[i][3]]      
            for p in y:
                    for q in y:
                        for r in y:
                            x[i][1],x[i][3],x[i][5] =p,q,r
                            if eval("".join(x[i]))==target:
                                return("".join(x[i]))                          
                        
    if len(op)==5:
        for a in op:
            for b in op:
                for c in op:
                    for d in op:
                        for e in op:
                            x.append([str(a),str(b),str(c),str(d),str(e)])
        for i in x:
            for j in i:
                if i.count(j)>1:
                    v.append(i)
        for i in v:
            if i in x:
                x.remove(i)
        for i in range(len(x)):
            x[i]=[x[i][0]]+t+[x[i][1]]+t+[x[i][2]]+t+[x[i][3]]+t+[x[i][4]]        
            for p in y:
                    for q in y:
                        for r in y:
                            for s in y:
                                x[i][1],x[i][3],x[i][5],x[i][7] =p,q,r,s
                                if eval("".join(x[i]))==target:
                                    return("".join(x[i]))                          
                        
                        
#countdown((1,2), 3)
countdown((2, 3, 5, 75), 158) #➞ "3+5+2*75"