"""
Find the Pattern and Write the Function
By looking at the inputs and outputs below, try to figure out the pattern and write a function to execute it for any number.

Examples
func(3456) ➞ 2

func(89265) ➞ 5

func(97) ➞ 12

func(2113) ➞ -9
"""
def func(num):
    
    a=(list(str(num)))
    b = len(a)
    
    count = 0
    for i in a:
        count = count + (int(i)-b)
    return count

func(89265) #➞ 5