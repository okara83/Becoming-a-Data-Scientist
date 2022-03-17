"""
https://edabit.com/challenge/YxnrZQwKyrzgcMvT4

Rotate-Transform the Two-Dimensional Matrix
Create a function to rotate a two-dimensional matrix of N * N integer elements num times, where if num is positive, the rotation is clockwise, and if not, counterclockwise.

Examples
rotate_transform([
  [2, 4],
  [0, 0]
], 1) ➞ [
  [0, 2],
  [0, 4]
]
rotate_transform([
  [2, 4],
  [0, 0]
], -1) ➞ [
  [4, 0],
  [2, 0]
]

"""
def rotate_transform(lst, num):
    if num%4 == 0: return lst 
    for k in range(num%4):
        rt= []
        for i in range(len(lst)):
            rt.append([])
            for j in range(len(lst)): 
                rt[i].append(0)
                rt[i][j]=lst[len(lst)-1-j][i]
        lst=rt
    return rt

rotate_transform([
  [2, 4],
  [0, 0]
], -1)