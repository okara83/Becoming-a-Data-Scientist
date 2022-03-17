"""
LCM of More Than Three Numbers
Create a function that takes an array of more than three numbers as an argument and returns the Least Common Multiple (LCM).

Examples
lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 2520

lcm_of_list([13, 6, 17, 18, 19, 20, 37]) ➞ 27965340

lcm_of_list([44, 64, 12, 17, 65]) ➞ 2333760
Notes
The LCM is the smallest positive number that is a multiple of two or more numbers.
"""

def lcm_of_list(numbers):
    
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
#lcm_of_list([1]) #, 1)
#lcm_of_list([5, 5, 5]) #, 5)
#lcm_of_list([67, 34, 12, 3, 2]) #, 13668)
#lcm_of_list([79, 18, 7, 3, 1]) #, 9954)
#lcm_of_list([10, 20, 30, 40, 50]) #, 600) 
#lcm_of_list([2, 3, 5, 7, 11, 13, 17]) #, 510510)
#lcm_of_list([91, 92, 93, 94, 95]) #, 3476431140)
#lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #, 2520)
#lcm_of_list([13, 6, 17, 18, 19,20, 37]) #, 27965340)
#lcm_of_list([44, 64, 12, 17, 65]) #, 2333760)
lcm_of_list([200, 30, 18, 11, 8, 64, 34]) #, 2692800)