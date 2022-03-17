"""
How Many Digits between 1 and N
Imagine you took all the numbers between 0 and n and concatenated them together into a long string. How many digits are there between 0 and n? Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.

Examples
digits(1) ➞ 0

digits(10) ➞ 9

digits(100) ➞ 189

digits(2020) ➞ 6969
Notes
The numbers are going to be rather big so creating that string won't be practical.
"""
def digits(number):
    return (sum([(10**(x+1) - 10**x) * (x+1) for x in range(len(str(number))-1)]) + (number-10**(len(str(number))-1))*(len(str(number))))
   
#digits(1), 0)
#digits(10), 9)
#digits(100) #, 189)
#digits(2020) #, 6969)
#digits(103496754) #, 820359675)
#digits(3248979384) #, 31378682729)
#digits(122398758003456), 1724870258940729)
digits(58473029386609125789) #, 1158349476621071404669)