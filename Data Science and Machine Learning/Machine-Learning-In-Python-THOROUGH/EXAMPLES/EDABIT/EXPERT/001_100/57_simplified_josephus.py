"""
Simplified Josephus
Given n people find the survivor, starting from the first person he kills the person to the left and the next surviving person kills the person to his left, this keeps happening until 1 person survives return that person's number.

Examples
josephus(1) ➞ 1

josephus(8) ➞ 1

josephus(41) ➞ 19
Notes
Check the rescources if you are confused about the instructions.


"""
def josephus(people):    
    if people == 1: return people   
    k=2
    a = list(range(people)) 
    z=0    
    while len(a)>1:
        b = [i for i in a if (a.index(i) + 1 + z) % k == 0]                           
        z = (z + len(a)) % k
        a=[i for i in a if not i in b]               
    return a[0]+1


#josephus(1) #, 1)
josephus(41) #, 19)
#josephus(8) #, 1)
#josephus(5) #, 3)
#josephus(7) #, 7)