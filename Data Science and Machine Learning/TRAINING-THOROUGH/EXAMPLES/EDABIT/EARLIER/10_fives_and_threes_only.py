"""
Fives and Threes Only
Starting with either 3 or 5 and given these operations:

add 5
multiply by 3
You should say if it is possible to reach the target number n.

Examples
only_5_and_3(14) ➞ True
# 14 = 3*3 + 5

only_5_and_3(25) ➞ True
# 25 = 5+5+5+5+5

only_5_and_3(7) ➞ False
# There exists no path to the target number 7
Notes
You can solve this problem by recursion or algebra.
"""
def only_5_and_3(n):
    
    m3, m5 = [0], []
    for i in range(1,n+1):
        if 3**i in range(1,n+1):
            m3.append(3**i)
    for j in range(n+1):
        if j%5==0:
            m5.append(j)
    
    
    for p in m3:
        for r in m5:
            if (p + r) == n: 
                return True
    return False
#only_5_and_3(14) #➞ True 
only_5_and_3(25) #➞ True
#only_5_and_3(7) #➞ False