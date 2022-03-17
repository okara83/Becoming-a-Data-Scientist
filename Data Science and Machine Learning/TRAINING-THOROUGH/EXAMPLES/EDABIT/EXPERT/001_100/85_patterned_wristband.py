"""
https://edabit.com/challenge/grorumaEjyFDmZQCx

Patterned Wristband
A wristband can have 4 patterns:

horizontal: each item in a row is identical.
vertical: each item in each column is identical.
diagonal left: each item is identical to the one on it's upper left or bottom right.
diagonal right: each item is identical to the one on it's upper right or bottom left.
You are shown an incomplete section of a wristband.

Write a function that returns True if the section can be correctly classified into one of the 4 types, and False otherwise.

Examples
is_wristband([
  ["A", "A"],
  ["B", "B"],
  ["C", "C"]
]) ➞ True 
# Part of horizontal wristband.

is_wristband([
  ["A", "B"],
  ["A", "B"],
  ["A", "B"]
]) ➞ True 
# Part of vertical wristband.

is_wristband([
  ["A", "B", "C"],
  ["C", "A", "B"],
  ["B", "C", "A"],
  ["A", "B", "C"]
]) ➞ True
# Part of diagonal left wristband.

is_wristband([
  ["A", "B", "C"],
  ["B", "C", "A"],
  ["C", "A", "B"],
  ["A", "B", "A"]
]) ➞ True
# Part of diagonal right wristband.
"""
def is_wristband(lst):
    h,v,dl,dr,result=[], [], [], [], []
    
    #check for horizontal:
    for i in lst:
        for j in range(1,len(lst[0])):
            if i[j]==i[j-1]: h.append(1)
            else: h.append(0)
        
    #check for vertical:
    for i in range(len(lst[0])):
        for j in range(1,len(lst)):
            if lst[j][i] == lst[j-1][i]: v.append(1)
            else: v.append(0)
                
    #check for diagonal left:
    for i in range(1,len(lst)):
        for j in range(1,len(lst[0])):
            if lst[i][j] == lst[i-1][j-1]: dl.append(1)
            else: dl.append(0)

    #check for diagonal right:
    for i in range(1,len(lst)):
        for j in range(1,len(lst[0])):
            if lst[::-1][i][j] == lst[::-1][i-1][j-1]: dr.append(1)
            else: dr.append(0)
    
    for i in (h,v,dl,dr):
        if not 0 in i: result.append(1) 
        
    
    if sum(result) > 0 :return True
    return False

is_wristband(
[['A', 'B', 'C'], 
['B', 'A', 'B'], 
['D', 'C', 'A'], 
['E', 'D', 'C']]) #, False)