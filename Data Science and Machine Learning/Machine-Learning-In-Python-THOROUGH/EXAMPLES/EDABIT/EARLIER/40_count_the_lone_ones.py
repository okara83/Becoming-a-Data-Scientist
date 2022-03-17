"""
Count the Lone Ones
Create a function which counts how many lone 1s appear in a given number. Lone means the number doesn't appear twice or more in a row.

Examples
count_lone_ones(101) ➞ 2

count_lone_ones(1191) ➞ 1

count_lone_ones(1111) ➞ 0

count_lone_ones(462) ➞ 0
"""


def count_lone_ones(n):
    a, count = list(str(n)), 0
    if a == ["1"] :return 1
    if not "1" in a: return 0 
    for i in range(1,len(a)-1):
        if a[i] == "1":
            if a[i+1] != "1" and a[i-1]!="1":
                count +=1    
    if a[0]=="1" and a[1]!="1":
        count +=1
    if a[-1]=="1" and a[-2]!="1":
        count +=1       
    return count



#count_lone_ones(101) #, 2)
#count_lone_ones(1191) #, 1)
#count_lone_ones(1111) #, 0)
#count_lone_ones(11101) #, 1)
#count_lone_ones(462) #, 0)
count_lone_ones(12131415161718191) #, 9)
#count_lone_ones(11231212111) #, 2)
#count_lone_ones(1) #, 1)
#count_lone_ones(0) #, 0)