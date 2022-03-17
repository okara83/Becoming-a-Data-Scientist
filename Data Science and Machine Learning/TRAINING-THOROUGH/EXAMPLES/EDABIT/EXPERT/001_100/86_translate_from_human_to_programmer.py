"""
https://edabit.com/challenge/kfwTnnJjo3SKG2pYx

Translate from Human to Programmer
Replace the numbers in a string with their binary form.

Examples
replace_nums("I have 2 sheep.") ➞ "I have 10 sheep."

replace_nums("My father was born in 1974.10.25.") ➞ "My father was born in 11110110110.1010.11001."

replace_nums("10hell76o4 boi") ➞ "1010hell1001100o100 boi"
Notes
There are possibly two or more numbers in a single word (I do not recommend splitting the text at spaces, it surely won't help).
Anything separates two numbers, even spaces ("2 2" --> "10 10").
"""
# with regex
#import re
#def replace_nums(string):
    #return re.sub(r"(\d+)", lambda m: bin(int(m.group()))[2:],string)

# without regex

def replace_nums(string):
    n, result= "", ""
    for i in string:
        if i.isnumeric(): n += i
        else:
            if not n == "":
                result += bin(int(n))[2:]
                n = ""
            result += i
            
    if not n == "": result += bin(int(n))[2:]
    return result



#replace_nums("I have 2 sheep.") #➞ "I have 10 sheep."
#replace_nums("My father was born in 1974.10.25.") #➞ "My father was born in 11110110110.1010.11001."
replace_nums("10hell76o4 boi") #➞ "1010hell1001100o100 boi"