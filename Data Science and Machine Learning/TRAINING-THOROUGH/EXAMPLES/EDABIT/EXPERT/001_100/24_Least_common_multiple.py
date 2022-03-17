"""
Least Common Multiple
Given a list of integers, create a function that will find the smallest positive integer that is evenly divisible by all the members of the list. In other words, find the least common multiple (LCM).

Examples
lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520

lcm([5]) ➞ 5

lcm([5, 7, 11]) ➞ 385

lcm([5, 7, 11, 35, 55, 77]) ➞ 385
Notes
N/A
"""
def lcm(numbers):
    
    a=sorted(list(set(numbers)), reverse = True)    
    if a==[1]: return [1]
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
     
#lcm([1]) #, 1)
#lcm([5, 5, 5]) #, 5)
#lcm([67, 34, 12, 3, 2]) #, 13668)
#lcm([79, 18, 7, 3, 1]) #, 9954)
lcm([10, 20, 30, 40, 50]) #, 600)
#lcm([2, 3, 5, 7, 11, 13, 17]) #, 510510)
#lcm([91, 92, 93, 94, 95]) #, 3476431140) 