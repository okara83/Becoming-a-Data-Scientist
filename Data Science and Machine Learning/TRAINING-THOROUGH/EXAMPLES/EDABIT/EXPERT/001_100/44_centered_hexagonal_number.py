"""
Centered Hexagonal Number
As stated on the On-Line Encyclopedia of Integer Sequences:

The hexagonal lattice is the familiar 2-dimensional lattice in which each point has 6 neighbors.

A centered hexagonal number is a centered figurate number that represents a hexagon with a dot in the center and all other dots surrounding the center dot in a hexagonal lattice.

At the end of that web page the following illustration is shown:

Illustration of initial terms:
.
.                                 o o o o
.                   o o o        o o o o o
.         o o      o o o o      o o o o o o
.   o    o o o    o o o o o    o o o o o o o
.         o o      o o o o      o o o o o o
.                   o o o        o o o o o
.                                 o o o o
.
.   1      7          19             37
.
Write a function that takes an integer n and returns "Invalid" if n is not a centered hexagonal number or its illustration as a multiline rectangular string otherwise.

Examples
hex_lattice(1) ➞ " o "
# o

hex_lattice(7) ➞ "  o o  \n o o o \n  o o  "
#  o o
# o o o
#  o o

hex_lattice(19) ➞ "   o o o   \n  o o o o  \n o o o o o \n  o o o o  \n   o o o   "
#   o o o
#  o o o o
# o o o o o
#  o o o o
#   o o o

hex_lattice(21) ➞ "Invalid"
"""

def hex_lattice(n):
    b=[]
    if n ==1: return " o "
    if (3+((12*n-3)**.5))%6 != 0: return "Invalid"    
    a = int((3+((12*n-3)**.5))/6)    
    for i in range(a):
        b.append(((a-1-i)*" ") + ((2*a+1) - (a+1-i))*"o " + ((a-1-i)*" "))   
    for i in range(1,a):
        b.append(((i)*" ") + ((2*a-1-i)*"o ")+((i)*" "))
    return " " + "\n ".join(b)

hex_lattice(19)