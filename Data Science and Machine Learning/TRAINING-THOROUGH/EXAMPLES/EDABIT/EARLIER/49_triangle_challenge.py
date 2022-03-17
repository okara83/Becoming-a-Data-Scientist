"""
Triangle Challenge
Given the perimeter and the area of a triangle, devise a function that returns the length of the sides of all triangles that fit those specifications. The length of the sides must be integers. Sort results in ascending order.

triangle(perimeter, area) ➞ [[s1, s2, s3]]
Examples
triangle(12, 6) ➞ [[3, 4, 5]]

triangle(45, 97.42786) ➞ [[15, 15, 15]]

triangle(70, 210) ➞ [[17, 25, 28], [20, 21, 29]]

triangle(3, 0.43301) ➞ [[1, 1, 1]]
Notes
def triangle(p,a):
    r=[]
    s=p/2
    for x in range(1,p//2+1):
        for y in range(int(s-x+1),p//2+1):
                z=p-x-y
                if round((s*(s-x)*(s-y)*(s-z))**.5,5)==a:
                    new=sorted((x,y,z))
                    if new not in r:
                        r.append(new)
    return sorted(r)
"""

def triangle(perimeter,area):
    p,q=perimeter,[]
    u = [] 
    for a in range(1,p//2+1):
        for b in range(p//2+1-a,p//2+1):
            c= p - (a+b)                                       
            if round(((p/2)*(p/2-a)*(p/2-b)*(p/2-c))**0.5,3) == round(area,3):
                u.append(a)
                u.append(b)
                u.append(c)   
    for i in range(len(u)//3):
        if not sorted([u[3*i],u[3*i+1],u[3*i+2]]) in q:
            q.append (sorted([u[3*i],u[3*i+1],u[3*i+2]]))
    return q
##(p/2>a) and (p/2>b) and(p/2>c) and 
#triangle(3, 0.43301) #, [[1, 1, 1]])
#triangle(201, 49.99937) #, [[1, 100, 100]])
#triangle(98, 420) #, [[24, 37, 37], [25, 34, 39], [29, 29, 40]])
#triangle(70, 210) #, [[17, 25, 28], [20, 21, 29]])
#triangle(30, 30) #, [[5, 12, 13]])
triangle(1792, 55440) #, [[170, 761, 861], [291, 626, 875]])
#triangle(150, 420) #, [[26, 51, 73]])
#triangle(864, 23760) #, [[132, 366, 366], [135, 352, 377]])