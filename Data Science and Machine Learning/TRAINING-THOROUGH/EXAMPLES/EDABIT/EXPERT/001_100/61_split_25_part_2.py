"""
Split 25 (Part #2)
Before you start, please try the first part of this challenge: Split 25 (Part #1)

After you completed the first part, you may have realized you could go higher by not using natural numbers. You could use negatives and positives, eventually reaching infinity, like so: -25 * 25 * 50 * -25 so on and so on continuing to add more factors. You could also use fractions and irrational numbers to increase it.

Being in the interest of not overcomplicating this part, attempt to find the highest product using fractions. For example, 10 could be broken up as 2.5 * 2.5 * 2.5 * 2.5 (which is (10/4)^4)and you could reach 39.0625, higher then 36 (3 3 4).

Given a positive integer to split, x, return the maximum product using rational numbers.

Examples
split(25) ➞ 9846.4
# (25 / 9) ** 9

split(15) ➞ 244.1
# (15 / 6) ** 6

split(1) ➞ 1
Notes
All responses should be rounded to one decimal place.
"""
def split(x):
    if x <2: return x
    a=[]    
    for i in range(1,x):
        a.append((x/i)**i)
    return (round(max(a),1))

#split(25) #, 9846.4)
split(30) #, 62088.9)
#split(1) #, 1)
#split(10) #, 39.1)
#split(20) #, 1554.3)
#split(50) #, 96951601.2)