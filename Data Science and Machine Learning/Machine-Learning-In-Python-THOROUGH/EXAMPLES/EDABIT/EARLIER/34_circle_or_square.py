"""
Circle or Square
Given the radius of a circle and the area of a square, return True if the circumference of the cirlce is greater than the square's perimeter and False if the square's perimeter is greater then the circumference of the circle.

Examples
circle_or_square(16, 625) ➞ True


circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True
Notes
You can use PI to 2 decimal places (3.14).
Circumference of a circle equals 2*PI*Radius.
"""
def circle_or_square(rad, area):
    if (2*3.14*rad)> (4*(area**(1/2))): return True
    return False


circle_or_square(16, 625)  #➞ True