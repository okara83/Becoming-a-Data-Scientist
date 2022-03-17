"""
Fraction to Mixed Number
Create a function that takes a string representing a fraction, and return a string representing that input as a mixed number.

Mixed numbers are of the form 1 2/3 — note the space between the whole number portion and the fraction portion.
Resulting fractions should be fully reduced (see example #2).
If a result is a whole number with no fractional remainder, return only the whole number portion (see example #3).
If a result is only fractional with no whole number, return only the fractional portion (see example #4).
If a result is negative, the whole number should carry the negative sign. 
If the result would not have a whole number portion, the numerator of the fractional portion should carry the negative sign (see examples #5 - #7).
Examples
mixed_number("5/4") ➞ "1 1/4"

mixed_number("6/4") ➞ "1 1/2"

mixed_number("8/4") ➞ "2"

mixed_number("4/6") ➞ "2/3"

mixed_number("-1/4") ➞ "-1/4"

mixed_number("-5/4") ➞ "-1 1/4"

mixed_number("-8/4") ➞ "-2"
Notes
All provided inputs will be formatted similarly, negative numbers will be provided in the numerator portion only, and all inputs will contain no spaces, invalid characters, or zero denominators.
"""
def mixed_number(frac):
    a = frac
    if a[0] == "0":
        return "0"
    elif a[0] == "-":
        r1="-"  
        r2 = (a[1:].split("/"))[0]
        r3 = (a[1:].split("/"))[1]
    else:
        r1=""
        r2 = (a.split("/"))[0]
        r3 = (a.split("/"))[1]

    if int(r2) % int(r3) == 0:
        return(r1 + str(int(int(r2) / int(r3))))
    if int(r2)<int(r3):
        r4=""
        r22= r2
    else:
        r4 = str(int(int(r2) / int(r3)))
        r22= str(int(r2)-int(r4)*int(r3))
    if int(r22)>1:
        num = int(r22)
        pf=[]  #Prime Factorization of an Integer
        for i in range(2,num+1):
            while num>1:
                if num%i == 0:
                    num = num /i
                    pf.append(i)
                else:
                    break        
        for i in pf:
            if int(r3)% i == 0:
                r3 = str(int(int(r3)/ i))
                r22 = str(int(int(r22)/ i))
    if r4=="":
        return (r1+r22+"/"+r3)
        
    
    return (r1+r4+" "+r22+"/"+r3)
    
#mixed_number("5/4") #➞ "1 1/4"
#mixed_number("12/8") #➞ "1 1/2"
#mixed_number("8/4") #➞ "2"
#mixed_number("4/6") #➞ "2/3"
#mixed_number("-1/4") #➞ "-1/4"
#mixed_number("-5/4") #➞ "-1 1/4"
#mixed_number("-8/4") #➞ "-2"
mixed_number("-2037450/204")  #, "-9987 1/2"