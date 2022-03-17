"""
Recursion: Harshad Number
A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.

Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12
 
is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171
 
is_harshad(481) ➞ True

is_harshad(89) ➞ False

is_harshad(516) ➞ True

is_harshad(200) ➞ True
Notes
You are expected to solve this challenge via recursion.
You can check on the Resources tab for more details about recursion.
A non-recursive version of this challenge can be found here
"""
def is_harshad(n):
    
    a,b=list(str(n)), []
    for i in a: b.append(int(i))
    if n%sum(b) == 0 :return True
    else: return False



is_harshad(481) #➞ True
#is_harshad(89) #➞ False
#is_harshad(516) #➞ True
#is_harshad(200) #➞ True
