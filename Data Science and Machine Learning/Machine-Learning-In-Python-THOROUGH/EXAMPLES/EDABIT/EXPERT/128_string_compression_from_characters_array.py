"""
https://edabit.com/challenge/6RHxTTndfASnPyp8Z  EXPERT

String Compression from Characters Array
The function is given an array of characters. Compress the array into a string using the following rules. For each group of consecutively repeating characters:

If the number of repeating characters is one, append the string with only this character.
If the number n of repeating characters x is greater than one, append the string with "x" + str(n).
Examples
compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

compress(["a"]) ➞ "a"

compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"
"""
def compress(chars):
    a, b = [], chars[0]
    count = 1    
    for i in chars[1:]:
        if i == b:count += 1
        else:
            a.append(b)
            if count > 1: a.append(str(count))
            b, count = i , 1            
    a.append(b)
    if count > 1: a.append(str(count))
    return "".join(a)



#compress(["a", "a", "b", "b", "c", "c", "c"]) #➞ "a2b2c3"

#compress(["a"]) #➞ "a"

#compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) #➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) #➞ "a3b2a2"