"""
Recursive Digit
We define super digit of an integer x using the following rules:

If x has only 1 digit, then its super digit is x.
Otherwise, the super digit of x is equal to the super digit of the sum of the digits of x.
For example, the super digit of x will be calculated as:

  super_digit(9875)    9+8+7+5 = 29
  super_digit(29)      2 + 9 = 11
  super_digit(11)      1 + 1 = 2
  super_digit(2) = 2
You are given two numbers n and k. The number p is created by concatenating the string times. Continuing the above example where n = 9875, assume your value k=4. Your initial p = 9875 9875 9875 9875 (spaces added for clarity).

super_digit(p) = super_digit(9875987598759875)
  5+7+8+9+5+7+8+9+5+7+8+9+5+7+8+9 = 116

super_digit(p) = super_digit(116)
  1+1+6 = 8

super_digit(p) = super_digit(8)
All of the digits of p sum to 116. The digits of 116 sum to 8. 8 is only one digit, so it's the super digit.

Complete the super_digit() method. It must return the calculated super digit as an integer.

superDigit has the following parameter(s):

n: a string representation of an integer.
k: an integer, the times to concatenate n to make p.
Examples
super_digit("148", 3) ➞ 3

super_digit("123", 3) ➞ 9

super_digit("99999999999999999999999999", 104500) ➞ 9
"""
def super_digit(n, k):

    a, b =list(n), []
    for i in a:
        b.append(int(i))
    tot = (sum(b))*k
    n=str(tot)    
    while len(list(n)) >0:        
        a, b =list(n), []
        for i in a:
            b.append(int(i))
        tot = (sum(b)) 
        n=str(tot)        
        if len(n) == 1:
            break
    return int(n[0])

#super_digit("123", 3) #, 9)
#super_digit("9875", 4) #, 8)
#super_digit("148", 3) #, 3)
#super_digit("111", 10) #, 3)
#super_digit("543", 100) #, 3)
super_digit("99999999999999999999999999", 104500) #➞ 9