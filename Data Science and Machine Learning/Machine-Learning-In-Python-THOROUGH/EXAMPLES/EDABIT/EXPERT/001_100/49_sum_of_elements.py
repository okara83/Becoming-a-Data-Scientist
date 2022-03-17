"""
Sum of Elements
Write a function that returns the sum of all the elements included in the root list.

Examples
func([ [], [] ,[] ]) ➞ 3
# 1 + 1 + 1 = 3
# The three empty lists inside the root list.

func([ [3], [2] ,[1,2] ]) ➞ 7
# 1 + 1 + 1 = 3
# The three lists inside the root list.
# 1 + 1 + 2 = 4
# The elements inside the previous lists.
# 4 + 3 = 7

func([]) ➞ 0
# The root list is empty thus there are no elements.

func([[[]]]) ➞ 2
# 1
# The only list in the root list.
# 1
# The empty list in the previous list.
# 1 + 1 = 2
Notes
If a list is empty return/add 0.
"""

def func(lst):    
    a,c,d = [], [], []
    c.append(len(lst))    
    a= lst
    t=0
    while t<len(lst):    
        for i in a:
            if type(i)==list:
                c.append(len(i))
                d=d+i
        a=d
        t+=1
    return sum(c)

#func([ [], [] ,[] ]) #, 3)
#func([ [3], [2] ,[1,2] ]) #, 7)
#func([]) #, 0)
#func([[[]]]) #, 2)
#func([ [1,2], ["3"] ,["F"] ]) #, 7)
func([ [[[]]], [2] ,[[[[[[]]]]]] ]) #, 11)