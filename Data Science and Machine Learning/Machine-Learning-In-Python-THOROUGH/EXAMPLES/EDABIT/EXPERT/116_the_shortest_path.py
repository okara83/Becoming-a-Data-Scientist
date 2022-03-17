"""
https://edabit.com/challenge/RoEn338P4xAf7mNNg

The Shortest Path
Given a rectangular grid of m by n spaces, signaled by 0s, and a number of points, signaled by 1, 2, 3..., return the number of moves for the shortest path that starts at 1 and goes over all the other points in ascending order.

Examples
shortest_path([
  ("001"),
  ("002"),
  ("003")
]) ➞ 2

shortest_path([
  ("00000"),
  ("01006"),
  ("02000"),
  ("30050"),
  ("00004")
]) ➞ 13

shortest_path([
  ("00020000"),
  ("01000000")
]) ➞ 3
Notes
Only horizontal and vertical movements are allowed.
All movements from one place to an adjacent one count as 1 regardless of direction.
The points range from 1 to at most 9 with no repeating or missing digits.

"""
def shortest_path(lst):
    a, count = [] , 0
    mm=int(max("".join(lst)))   
    for k in range(1,mm+1):
        for i in lst:
            for j in i:
                if str(j)==str(k): a.append([lst.index(i),i.index(j)])
        count += abs(a[k-1][0]-a[k-2][0]) + abs(a[k-1][1]-a[k-2][1])     
    return count

shortest_path([
  ("00000"),
  ("01006"),
  ("02000"),
  ("30050"),
  ("00004")
]) #➞ 13