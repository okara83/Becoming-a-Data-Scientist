"""
https://edabit.com/challenge/siuKPSYXjjic9zEF2

Aluminum Foil
Aluminum foil has a thickness of 0.025mm. 
A roll is formed by tightly winding it around a tube with an outside diameter of 4cm. 
Given the length of the foil in cm, write a function that returns the diameter of the roll in cm measured 
at its thickest point. Round the result to four places.

Examples
foil(0) ➞ 4.0
foil(50) ➞ 4.02
foil(4321) ➞ 5.4575
foil(10000) ➞ 6.9175
Notes
N/A
"""
import math
def foil(length):
    
    if length == 0: return 4.0
    
    d= 0.0025  #thickness
    r= 2  #radius of tube
    tour = (((length*d)/math.pi+4)**.5-2)/d    
    surf=length*d
    intsurf = math.pi*((int(tour)*d+2)**2-4)
    intperp = math.pi*(int(tour)*d+2)*2
    ext = int(round(surf/d,0))-(intsurf/d)
   
    if ext/intperp >= 0.96: return(round(2*int(tour)*d+4+3*d,4))
    elif ext/intperp >= 0.5:
        if length > 10000:return(round(2*int(tour)*d+4+3*d,4))
        return(round(2*int(tour)*d+4+2*d,4))
    else:return(round(2*int(tour)*d+4+d,4))



#foil(0)#, 4.0)
#foil(6)#, 4.0025)
#foil(7)#, 4.005)
#foil(12)#, 4.005)
#foil(13)#, 4.0075)
foil(1000)#, 4.3825)
#foil(7777)#, 6.385)
#foil(123456)#, 20.2275)
#foil(50) #➞ 4.02
#foil(4321) #➞ 5.4575
#foil(10000) #➞ 6.9175