"""
Intro to Nested Loops
Imagine a school that kids attend for 6 years. In each year, there are five groups started, marked with the letters a, b, c, d, e. For the first year, the groups are 1a, 1b, 1c, 1d, 1e and for the last year, the groups are 6a, 6b, 6c, 6d, 6e.

Write a function that returns the groups in the school by year (as a string), separated with a comma and a space in the form of "1a, 1b, 1c, 1d, 1e, 2a, 2b (....) 5d, 5e, 6a, 6b, 6c, 6d, 6e".

Examples
print_all_groups() ➞ "1a, 1b, 1c, 1d, 1e, 2a, 2b, 2c, 2d, 2e, 3a, 3b, 3c, 3d, 3e, 4a, 4b, 4c, 4d, 4e, 5a, 5b, 5c, 5d, 5e, 6a, 6b, 6c, 6d, 6e "
Notes
Use nested "for" loops to achieve this, as well as the array of ["a", "b", "c", "d", "e"] groups.
"""
def print_all_groups():
    
    a = "123456"
    b = "abcde"
    c=[]
    
    for i in a:
        for j in b:
            print(i+j)
            c.append(i+j)
            
    return ", ".join(c)     

    


print_all_groups()
