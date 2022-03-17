"""
Volume of a Spherical Shell
The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

Volume of Inner Sphere Formula

Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.

Spherical Shell Image

Examples
vol_shell(3, 3) ➞ 0

vol_shell(7, 2) ➞ 1403.245

vol_shell(3, 800) ➞ 2144660471.753
Notes
The inputs are always positive numbers. r1 could be the inner radius or the outer radius, don't return a negative number.
"""


import math
def vol_shell(r1, r2):
    return round((4/3)*(math.pi)*(abs(r1**3-r2**3)),3)


#vol_shell(17, 36), 174852.67)
vol_shell(3, 4)  #, 154.985)