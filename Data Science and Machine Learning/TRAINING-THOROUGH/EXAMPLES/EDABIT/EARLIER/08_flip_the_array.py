"""
Flip the Array
Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.

In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.

Examples
flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.

flip_list([[5], [6], [9]]) ➞ [5, 6, 9]
# Take a vertical list and flip it horizontal.

flip_list([]) ➞ []
Notes
If given an empty list [], return an empty list [].
"""
def flip_list(lst):
    
    a= []
    if len(lst) == 0: return []
        
    if type(lst[0]) == list:
        for i in lst:
            a.append(i[0])
    else:        
        for i in range(len(lst)):
            a.append([])
            a[i].append(lst[i])            
    return (a)    

    
    
#flip_list([1, 2, 3, 4]) #➞ [[1], [2], [3], [4]]    
flip_list([[5], [6], [9]]) #➞ [5, 6, 9]    
#flip_list([]) #➞ []    