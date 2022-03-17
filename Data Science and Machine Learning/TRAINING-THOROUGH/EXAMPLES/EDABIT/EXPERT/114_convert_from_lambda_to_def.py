"""
https://edabit.com/challenge/5S97Me79PDAefLEXv

Convert from lambda to def
Given a piece of code with a function assigned by lambda, rewrite it into a function assigned by def. The code given would be in string.

Overview
This is a quick example of a lambda expression:

func = lambda a, b: a * (b - 2)
... is the same as ...

def func(a, b):
  return a * (b - 2)
Examples
lambda_to_def("func = lambda w: w + 'lambda'") ➞ "def func(w):\n\treturn w + 'lambda'"

lambda_to_def("z = lambda lambdadef: lambdadef.split(':')") ➞ "def z(lambdadef):\n\treturn lambdadef.split(':')"
Visualisation:

print(lambda_to_def("func = lambda w: w + 'lambda'"))

def func(w):
  return w + 'lambda'
print(lambda_to_def("z = lambda lambdadef: lambdadef.split(':')"))

def z(lambdadef):
  return lambdadef.split(':')
Notes
The new code should follow PEP8 guidelines.
For the sake of convenience, use \t for indentation.
Assume all lambda expressions are valid.
"""
def lambda_to_def(code):    
    a = code.split(" ")[0]    
    if code.count(":") > 1 and code.index(":") > code.index("'"):
            ix = code[::-1].index(":")
            b = code[code.index("lambda") + 7 : -ix - 1]    
            c = code[-ix:]    
    else:
        b = code[code.index("lambda") + 7 : code.index(":")]
        c = code[code.index(":") + 1 :]
    return "def " + a + "(" + b + "):\n\treturn" + c

lambda_to_def("func = lambda w: w + 'lambda'") #➞ "def func(w):\n\treturn w + 'lambda'"
#lambda_to_def("func = lambda a, b: a * (b - 2)") #,"def func(a, b):\n\treturn a * (b - 2)"
#lambda_to_def("t = lambda s='t = lambda s: s + 1': s + 's'") #"def t(s='t = lambda s: s + 1'):\n\treturn s + 's'"
#lambda_to_def("z = lambda lambdadef: lambdadef.split(':')") #"def z(lambdadef):\n\treturn lambdadef.split(':')"