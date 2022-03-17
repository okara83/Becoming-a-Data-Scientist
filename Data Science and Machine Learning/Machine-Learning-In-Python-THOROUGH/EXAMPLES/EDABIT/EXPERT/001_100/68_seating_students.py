"""
Seating Students
Create a function that reads a list of integers stored which will be in the following format: [[K, r1, r2, r3, ...]], where K represents the number of desks in a classroom, and the rest of the integers in the list will be in sorted order and will represent the desks that are already occupied. All of the desks will be arranged in two columns, where desk #1 is at the top left, desk #2 at the top right, desk #3 is below #1, desk #4 is below #2, etc.

Your program should return the number of ways two students can be seated next to each other. This means one student is on the left and one on the right, or one student is directly above or below the other student.

To illustrate:

[[12, 2, 6, 7, 11]]
This classroom will look like the following:

Column 1
[[#, 4, #, 8, 10, 12]]
# The first # is 2 and second # is 6 which are occupied.
Column 2
[[1, 3, 5, #, 9, #]]
# The first # is 7 and and second # is 11 which are occupied.
Based on the above arrangement of occupied desks, there are a total of six ways to seat two new students next to each other. The combinations are:

[[1, 3]], [[3, 4]], [[3, 5]], [[8, 10]], [[9, 10]], [[10, 12]]
For this input, your program should return 6. K will range from 2 to 24 and will always be an even number. After K, the number of occupied desks in the list can range from 0 to K.

Examples
seating_students([6, 4]) ➞ 4

seating_students([8, 1, 8]) ➞ 6

seating_students([12, 2, 6, 7, 11])  ➞ 6
"""

def seating_students(lst):
    
    K, S, P = lst[0], lst[1:], []
    a, b, c = [], [], []    
    for i in range((K-2)//2+1):
        a.append([])
        a[i].append(2*i+1)
        a[i].append(2*i+2)    
    for i in range((K-4)//2+1):
        b.append([])
        b[i].append(2*i+1)
        b[i].append(2*i+3)
    for i in range((K-4)//2+1):
        c.append([])
        c[i].append(2*i+2)
        c[i].append(2*i+4)
    D = (a+b+c)
    for i in D:
        if not i[0] in S:
            if not i[1] in S:
                P.append(i)
    return len(P)

seating_students([6, 4]) #➞ 4
#seating_students([8, 1, 8]) #➞ 6
#seating_students([12, 2, 6, 7, 11])  #➞ 6
#seating_students([10, 2, 9]) #, 9)
#seating_students([16, 2, 4, 6, 7, 8, 9, 10]) #, 9)