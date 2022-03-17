"""
https://edabit.com/challenge/HqpZQPZiHbPK4HgEB

Maxie and Minnie
Maxie is the largest number that can be obtained by swapping two digits, Minnie is the smallest. 
Write a function that takes a number and returns Maxie and Minnie. Leading zeros are not permitted.

Examples
maxmin(12340) ➞ (42310, 10342)

maxmin(98761) ➞ (98761, 18769)

maxmin(9000) ➞ (9000, 9000)
# Sometimes no swap needed.

maxmin(11321) ➞ (31121, 11123)
"""
def maxmin(n):   
    a=[]
    for i in range(len(str(n))):
        for j in range(i,len(str(n))):
            b=list(str(n))
            b[i], b[j] = b[j], b[i]
            if b[0]!="0" :
                if not int("".join(b)) in a: a.append(int("".join(b)))
    return(max(a),min(a))
  
    
maxmin(9876543210)#, (9876543210, 1876543290))
#maxmin(1234567890)#, (9234567810, 1034567892))