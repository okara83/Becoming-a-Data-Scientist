"""
https://edabit.com/challenge/BDjhphREEa6Ds44Ty

Where's the Bomb?
A large flat field measures 50x50 kilometers. At a time t = 0, a bomb explodes somewhere on the field. There are 3 scattered sensors with synchronized clocks that record the exact time (in seconds) that the sound of the exploding bomb reaches them.

Given the x, y coordinates of each of the 3 sensors and the recorded time of each, find the location of the bomb:

bomb([[x1, y1, t1], [x2, y2, t2], [x3, y3, t3]]) ➞ (xb, yb)
# Bomb location
Examples
bomb([[0, 0, 72.886], [0, 50, 72.886], [25, 25, 72.886]]) ➞ (0, 25)

bomb([[0, 50, 145.773], [50, 50, 206.154], [50, 0, 145.773]]) ➞ (0, 0)

bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]) ➞ (21, 13)

bomb([[18, 42, 35.558], [39, 16, 106.004], [7, 24, 32.202]]) ➞ (8, 35)
Notes
The origin is at one corner of the square field so all the coordinates are positive integers in km units.
The bomb's coordinates are integers.
The speed of sound in air is 0.343 km/sec.
"""


def bomb(lst):
    
    [[x1, y1, t1], [x2, y2, t2], [x3, y3, t3]], vson = lst, 0.343
    
    if x1==x2==x3 and y1==y2==y3: return (x1,y1)

    
    dis1 = t1 * vson
    dis2 = t2 * vson
    dis3 = t3 * vson
   
    k = 2*(x2 - x1)
    p = 2*(y2 - y1)
    q = 2*(x3 - x1)
    r = 2*(y3 - y1)
    
 
    m = dis1**2 - dis2**2 - x1*x1 + x2*x2 - y1*y1 + y2*y2
    n = dis1**2 - dis3**2 - x1*x1 + x3*x3 - y1*y1 + y3*y3
 

    x = (m - n*p/r) / (k - q*p/r)
    
    if p == 0:  y = (n - x*q) / r
    else: y = (m - x*k) / p

    return(int(round(x,0)),int(round(y,0)))
   

bomb([[5, 8, 48.872], [12, 21, 35.107], [24, 20, 22.203]]) #➞ (21, 13)