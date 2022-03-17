"""
Split 25 (Part 1)
About a month ago I stumbled upon an interesting problem — something called the 25 split. In the problem, you had to break up 25 into parts that add to it, and, from those parts, try to create the biggest product.

For example, 3 * 22 = 66 or 5 * 5 * 5 * 5 * 5 = 3125. With this first part, return the value of the biggest product possible using natural number parts from a given number, x.

Examples
split(5) ➞ 6
# 3 times 2

split(10) ➞ 36
# 3 * 3 * 4

split(1) ➞ 1
Notes
3's are useful...
"""
def split(number):
    if number <2: return number    
    if number%3 == 0:   return int(3**(number/3))
    elif number%3 == 1: return int((3**((number-4)/3))*4)
    else: return int((3**((number-2)/3))*2)

#split(25) #, 8748)
split(20) #, 1458)