"""
Sales Season
A retailer is having a store-wide "buy 3, get 1 free" sale. 
For legal reasons, they can't charge their customers $0 for an article so a discount is applied to all products instead. 
For example, if a customer gets three products a, b and c:

Product A	Product B	Product C
$15.99	$23.50	$10.75
She gets the cheapest one for free, so she ends up paying $15.99 + $23.50 = $39.49, but what her receipt says is:

Product A: $15.99 − Special Discount = $12.57
Product B: $23.50 − Special Discount = $18.47
Product C: $10.75 − Special Discount = $8.45
Total: $39.49
Create a function that takes in a list of prices for a customer's shopping cart and returns the prices 
with the discount applied. Round all prices to the cent.

Examples
discount([2.99, 5.75, 3.35, 4.99]) ➞[2.47, 4.74, 2.76, 4.12]
# First product for free.

discount([10.75, 11.68]) ➞ [10.75, 11.68]
# No discounts applied.

discount([68.74, 17.85, 55.99]) ➞ [60.13, 15.62, 48.98]
# Second product for free.
Notes
The discount is calculated in percentual terms.
The deal applies to sets of three products: if a customer gets 9 products, she will get the three cheapest ones for free, but if she gets 10 or 11 products, she will still get three for free. Buying a 12th product would get her a fourth free product.
No cart splitting allowed.
"""
def discount(lst):
    
    if len(lst)<3:
        return(lst)
    
    e = []
    a = len(lst)//3
    b = sorted(lst,reverse=True)
    c = sum(b)
    d= sum(b[:-a])
    
    for i in lst:
        e.append(round(i*(d/c),2))
    return (e)

#discount([2.99, 5.75, 3.35, 4.99]) #, [2.47, 4.74, 2.76, 4.12])
#discount([10.75, 11.68]) #, [10.75, 11.68])
#discount([68.74, 17.85, 55.99]) #, [60.13, 15.62, 48.98])
discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) #, [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16])
#discount([14.15, 9.45, 3.72, 5.99, 8.13, 8.85]) #, [11.42, 7.63, 3.0, 4.83, 6.56, 7.14])
#discount([2.98, 0.25, 1.25]) #, [2.81, 0.24, 1.18])
#discount([9.20]) #, [9.20])