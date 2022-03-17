"""
Operations
Write a function that does the following things: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge, the variable will be defined for you. All you have to do is look at the variable, do some string to integer conversions use some if conditionals, and combine them based on the operation.

The numbers and operation will be given as a string, and you should return the value as a string as well.

Examples
operation("1", "2", "add" ) ➞ "3"

operation("4", "5", "subtract") ➞ "-1"

operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as a string, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide go ahead and round down to an integer.
Test.assert_equals(operation("1", "2", "add"), "3")
Test.assert_equals(operation("1", "-20", "add"), "-19")
Test.assert_equals(operation("9", "0", "divide"), "undefined")
Test.assert_equals(operation("10", "10", "multiply"), "100")
Test.assert_equals(operation("-10", "-10", "multiply"), "100")
Test.assert_equals(operation("10", "10", "subtract"), "0")
Test.assert_equals(operation("0", "0", "subtract"), "0")
Test.assert_equals(operation("0", "1", "divide"), "0")
Test.assert_equals(operation("0", "25415", "divide"), "0")
Test.assert_equals(operation(operation("10", "10", "multiply"),operation("10","10","add"),"divide"), "5")
"""
def operation(a, b, op):
    
    if op == "add" : return str(int(a) + int(b))
    elif op == "subtract" : return str(int(a) - int(b))
    elif op == "multiply" : return str(int(a) * int(b))
    elif op == "divide" :
        if b == "0":return "undefined"
        return str(int(a) // int(b))


#operation("1", "2", "add") #, "3")
operation("9", "0", "divide")  #, "undefined")
#operation(operation("10", "10", "multiply"),operation("10","10","add"),"divide") #, "5")