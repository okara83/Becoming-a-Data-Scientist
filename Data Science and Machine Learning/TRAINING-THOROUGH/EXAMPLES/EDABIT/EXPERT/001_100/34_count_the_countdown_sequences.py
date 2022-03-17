"""
Count the Countdown Sequences
5, 4, 3, 2, 1 is a countdown sequance example. Write a function that returns a list [x, y] where x is the number that represents how many of countdown sequences are in a given list and y is a list of those sequences in order which they appear in the list.

Examples
final_countdown([4, 8, 3, 2, 1, 2]) ➞ [1, [[3, 2, 1]]]
# In this example we have 1 countdown sequence: 3, 2, 1

final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) ➞ [2, [[5, 4, 3, 2, 1], [3, 2, 1]]]
# We have 2 countdown sequences:
# 5, 4, 3, 2, 1 and 3, 2, 1

final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) ➞ [3, [[4, 3, 2, 1], [3, 2, 1], [1]]]
# We have 3 countdown sequences:
# 4, 3, 2, 1 ; 3, 2, 1 and 1

final_countdown([1, 1, 2, 1]) ➞ [3, [[1], [1], [2, 1]]]

final_countdown([]) ➞  [0, []]
Notes
[1] is a valid countdown sequence.
All numbers will be greater than 0.
"""
def final_countdown(lst):
    if lst == []: return [0, []]
    a= lst[::-1]
    b,c,d = [], [], []    
    for k in a:
        b.append([])    
    for i in range(len(a)):
        if a[i] == 1:
            b[i].append(a[i])
            for j in range(i+1, len(a)):
                if a[j] - a[j-1] == 1:
                    b[i].append(a[j])
                else: break     
    for i in range(len(b)):
        if b[i] != []:
            c.append(b[i][::-1])
    d.append(len(c))
    d.append(c[::-1])
    
    return d
 
#final_countdown([5,4,3,2,1]) #, [1, [[5, 4, 3, 2, 1]]])
#final_countdown([2,5,4,3,2,1,2]) #, [1, [[5, 4, 3, 2, 1]]])
#final_countdown([2,3,2,1,4,3,2,1]) #, [2, [[3, 2, 1], [4, 3, 2, 1]]])
#final_countdown([4,3,2,5,4,3]) #, [0, []])
#final_countdown([4,3,2,5,4,3,1]) #, [1, [[1]]])
#final_countdown([3,2,1,5,5,3,2,1,5,5]) #, [2, [[3, 2, 1], [3, 2, 1]]])
#final_countdown([4, 8, 3, 2, 1, 2]) #, [1, [[3, 2, 1]]])
#final_countdown([4, 4, 5, 4, 3, 2, 1, 8, 3, 2, 1]) #, [2, [[5, 4, 3, 2, 1], [3, 2, 1]]])
final_countdown([4, 3, 2, 1, 3, 2, 1, 1]) #, [3, [[4, 3, 2, 1], [3, 2, 1], [1]]])
#final_countdown([1,2,1,1]) #, [3, [[1] #, [2, 1], [1]]])
#final_countdown([1,2,3,4,3,2,1]) #, [2, [[1], [4, 3, 2, 1]]])
#final_countdown([]) #, [0, []])
#final_countdown([2,1,2,1]) #, [2, [[2, 1], [2, 1]]])
