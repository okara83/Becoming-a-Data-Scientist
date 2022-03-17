"""
Frequency by Level of Nesting
Create a function that takes in a nested list and an element and returns the frequency of that element by nested level.

Examples
freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)
➞ [[0, 1], [1, 2], [2, 3]]
# The list has one 1 at level 0, 2 1's at level 1, and 3 1's at level 2.

freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)
➞ [[0, 3], [1, 4], [2, 0]]

freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)
➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]
Notes
Start the default nesting (a list with no nesting) at 0.
Output the nested levels in order (e.g. 0 first, then 1, then 2, etc).
Output 0 for the frequency if that particular level has no instances of that element (see example #2).
"""

def freq_count(lst, el):
    
    nest, b, c, f, result= [0], [], [[]], [[]], []
    a=lst
    t = 0
    while t < len(lst)+5: 
        e,d,g=[],[],[]
        for i in a:
            if i ==el: f[nest[-1]].append(i)
            if type(i)==list: d.append(i)        
        if len(d)>0:
            f.append([])
            nest.append(nest[-1]+1)
            for i in d:
                e=e+i
            for i in e:    
                if i == el: f[nest[-1]].append(i)
        
        if len(e)==0:
                break
        for i in e:
            if type(i)==list: g.append(i)
        a=g
        t+=1  
    
    for i in range(len(nest)):        
        result.append([nest[i],len(f[i])])
    return (result) 



freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1)   #, [[0, 1], [1, 2], [2, 3]])    
#freq_count([[[1]]], 1)  #, [[0, 0], [1, 0], [2, 1]])
#freq_count([1, 1, 2, [1]], 1)  #, [[0, 2], [1, 1]]) 
#freq_count([[[1]]], 1)   #, [[0, 0], [1, 0], [2, 1]])
#freq_count([1, 1, 2, [[1]]], 1)  #, [[0, 2], [1, 0], [2, 1]])        
#freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5)  #, [[0, 3], [1, 4], [2, 0]])
#freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2)   #➞ [[0, 0], [1, 1], [2, 1], [3, 1], [4, 1]]