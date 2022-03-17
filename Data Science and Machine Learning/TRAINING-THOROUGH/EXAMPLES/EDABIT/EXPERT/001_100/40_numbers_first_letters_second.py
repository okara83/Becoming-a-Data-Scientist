"""
Numbers First, Letters Second
Write a function that sorts list while keeping the list structure. Numbers should be first then letters both in ascending order.

Examples
num_then_char([
  [1, 2, 4, 3, "a", "b"],
  [6, "c", 5], [7, "d"],
  ["f", "e", 8]
]) ➞ [
  [1, 2, 3, 4, 5, 6],
  [7, 8, "a"],
  ["b", "c"], ["d", "e", "f"]
]

num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
]) ➞ [
  [0, 0.5, 1, 2, 3, 4.4],
  [8],
  [12, 18, "X", "Y", "Z"],
  ["a", "b", "d"],
  ["e", "f", "f"],
  ["p", "s"]
]
Notes
Test cases will containg integer and float numbers and single letters.
"""

def num_then_char(lst):
    a= len(lst)
    ALF=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    alf= ALF.lower()
    b, c, d, dig, up, low=[], [], [], [], [], []
    for i in lst:
        b.append([])
        c.append(len(i))
        for j in i:
            if j in list(ALF):
                up.append(j)
            elif j in list(alf):
                low.append(j)
            else:
                dig.append(j)    
    d = sorted(dig) + sorted(up) + sorted(low)    
    for i in range(a):
        b[i]=d[:c[i]]
        d=d[c[i]:]    
    return b

num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
])