"""
https://edabit.com/challenge/oxf7b7vroXvWBJ9Nq     EXPERT ----


Discount! Discount! Discount!
We all love a little bargain.

Your function will get a price, and a load of discounts. Your job is to write the function so that it calculates the maximum possible discount.

The price is a Number.
The load of discounts is a string like: 15%, 8, 50%.
So, percentages, with %, and amounts, without %.
You have to think about the order of applying the discounts.
Round the output amount to the nearest hundreth.
Output a Number.
Examples
discount(64, "50%, 50%") ➞ 16
# Reduce 50% twice.

discount(24, "20, 2") ➞ 2
# Subtract 20 and 2.

discount(20, "10, 10%") ➞ 8
# Apply 10% discount first and then subtract 10.
Notes
N/A
"""
def discount(n, txt):
    if txt=="":return n 
    
    prc=[float(i[:-1]) for i in txt.split(", ") if i[-1]=="%"]
    amnt = [float(i) for i in txt.split(", ") if i[-1]!="%"]

    for i in prc: n *= (1 - i/100)

    return round(n-sum(amnt),2)
    
#discount(64, "50%, 50%") #➞ 16
#discount(24, "20, 2") #➞ 2
#discount(20, "10, 10%") # ➞ 8
discount(12345, '4%, 21, 33.6%, 87, 3%, 80.12')  #7445