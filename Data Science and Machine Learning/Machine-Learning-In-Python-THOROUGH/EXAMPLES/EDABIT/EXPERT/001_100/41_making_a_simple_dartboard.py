"""
Making a Simple Dartboard
Create a function which creates a square dartboard of side length n. The value of a number should increase, the closer it is to the centre of the board.

Examples
make_dartboard(3) ➞ [
  111,
  121,
  111
]

make_dartboard(8) ➞ [
  11111111,
  12222221,
  12333321,
  12344321,
  12344321,
  12333321,
  12222221,
  11111111
]

make_dartboard(5) ➞ [
  11111,
  12221,
  12321,
  12221,
  11111
]
Notes
If the size given is an even number, the centre should be made up of the 4 highest values.
"""

def make_dartboard(n):

    a, b, c, d = [], [], [], []
    
    if n == 1:
        return [1]
    
    if n%2 == 0:
        for i in range(1,n//2+2):
            a.append([])
            b.append([])
            for j in range(1,i):
                a[i-2].append(str(j))
        a, b = a[:-1], b[:-1]  
        for k in range(len(a)):
            for i in range(n - 2*len(a[k]) ):
                b[k].append(a[k][-1])
            b[k] = a[k] + b[k] + a[k][::-1]
        c = (b + b[::-1])

    if n%2 !=0:
        for i in range(1,n//2+3):
            a.append([])
            b.append([])
            for j in range(1,i):
                a[i-2].append(str(j))
        a, b = a[:-1], b[:-1]  
        for k in range(n//2):
            for i in range(n - 2*len(a[k]) ):
                b[k].append(a[k][-1])
            b[k] = a[k] + b[k] + a[k][::-1]
        b[-1]=a[-1]+a[-2][::-1]
        c = (b + b[::-1][1:])
    for i in c:
        d.append(int("".join(i))) 
    return (d)    


make_dartboard(9) 