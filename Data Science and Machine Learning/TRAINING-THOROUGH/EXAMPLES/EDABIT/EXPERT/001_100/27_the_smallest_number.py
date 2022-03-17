"""
The Smallest Number
Given a positive integer n, implement a function that finds the smallest number that is evenly divisible by the integers 1 through n inclusive.

Examples
smallest(1) ➞ 1

smallest(5) ➞ 60

smallest(10) ➞ 2520

smallest(20) ➞ 232792560
"""

def smallest(n):

    numbers = list(range(n+1))
    
    a=sorted(list(set(numbers)), reverse = True)    
    if a==[1]: return 1
    pf=[]  #Prime Factorization of an Integer    
    for i in a:
        if i>1:
            numbers = i
            k=[]
            for i in range(2,numbers+1):
                while numbers>1:
                    if numbers%i == 0:
                        numbers = numbers /i
                        k.append(i)
                    else:
                        break 
            pf.append(k)   
    pf2=pf[0]
    for i in pf:
        for j in i: 
            if pf2.count(j)< i.count(j): pf2.append(j)

    result=1
    for i in pf2: result = result*i
        
    return (result)
    

    
#smallest(1) #➞ 1
#smallest(5) #➞ 60
#smallest(10) #➞ 2520
smallest(20) #➞ 232792560    