"""
Add Two String Numbers
Write a function that adds two numbers. The catch, however, is that the numbers will be strings.

Examples
add_str_nums("4", "5") ➞ "9"

add_str_nums("abcdefg", "3") ➞ "-1"

add_str_nums("1", "") ➞ "1"

add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ 1874682736267235927391936562808774986
Notes
If there are any non-numerical characters, return "-1".
If one option is blank the code should still work.
Python supports the addition of integers without limit, try this challenge without using this functionality.
Your function doesn't have to add negative numbers.
"""
def add_str_nums(num1, num2):
    
    if list(num1)==[]:
        a = 0
    else:
        a=("").join(list(num1))
    if list(num2)==[]:
        b = 0    
    else:
        b=("").join(list(num2))    
    if not (list(num1)==[] or list(num2)==[]):
        if not (a.isnumeric() and b.isnumeric()):
            return str(-1)    
    return str(int(a)+int(b))

#add_str_nums("", "") #➞ "9"
add_str_nums("abcdefg", "3") #➞ "-1"
#add_str_nums("1", "") #➞ "1"
