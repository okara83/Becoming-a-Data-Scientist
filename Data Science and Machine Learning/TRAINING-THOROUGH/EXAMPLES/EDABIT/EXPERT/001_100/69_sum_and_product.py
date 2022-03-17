"""
Sum and Product
Write a function that takes in two floating-point numbers s and p and returns a tuple of two floating-point numbers (x, y), where x + y = s and x * y = p. Round x and y to three decimal places.

If there are multiple solutions, return the solution with the lesser x (or lesser y, if the x values are equal).

Imaginary/complex number solutions are not allowed. If no real-valued solutions exist, return None.

Examples
sum_and_product(2, -15) ➞ (-3.0, 5.0)

sum_and_product(144, 144) ➞ (1.007, 142.993)

sum_and_product(-42.7, 144.5) ➞ (-38.994, -3.706)

sum_and_product(10, 30) ➞ None
Notes
To solve this problem, consider setting up a system of two equations and solving for x and y.

tests = [
    ((2, -15), (-3.0, 5.0)),
    ((144, 144), (1.007, 142.993)),
    ((-42.7, 144.5), (-38.994, -3.706)),
    ((10, 30), None),
    ((-11, 33), None),
    ((-13, -99), (-18.385, 5.385)),
    ((1111, 1234), (1.112, 1109.888)),
    ((1234, 1111), (0.901, 1233.099)),
    ((34, 289), (17.0, 17.0)),
    ((-26.6, 176.89), (-13.3, -13.3)),
    ((0, -25), (-5.0, 5.0)),
    ((0, 25), None),
    ((-25, 0), (-25.0, 0.0)),
    ((25, 0), (0.0, 25.0)),
    ((0, 0), (0.0, 0.0)),
]
"""
def sum_and_product(s, p):
    if (s**2<4*p): return None
    a=[]
    x1= (s-((s**2-4*p)**(1/2))) / (2)
    x2= (s+((s**2-4*p)**(1/2))) / (2)
    a.append(round(min(x1,x2),3))
    a.append(round((s-min(x1,x2)),3))
    return a[0],a[1]

#sum_and_product(2, -15) #➞ (-3.0, 5.0)
sum_and_product(144, 144) #➞ (1.007, 142.993)
#sum_and_product(-42.7, 144.5) #➞ (-38.994, -3.706)
#sum_and_product(10, 30) #➞ None