"""
https://edabit.com/challenge/F77JQs68RSeTBiGtv

Diamond Sum
Given an nxn grid of consecutive numbers, return the grid's Diamond Sum. The diamond sum is defined as the sum of the numbers making up the diagonals between adjacent sides.

Examples
diamond_sum(1) ➞ 1

[1]
diamond_sum(3) ➞ 20

[
  [1, _, 3],
  [_, 5, _],
  [7, _, 9]
]

# The numbers behind the underscores make up the Diamond Sum.
# 2 + 4 + 6 + 8 = 20
diamond_sum(5) ➞ 104

[
  [1, 2, _, 4, 5],
  [6, _, 8, _, 10],
  [_, 12, 13, 14, _],
  [16, _, 18, _, 20],
  [21, 22, _, 24, 25]
]

# 3 + 7 + 9 + 11 + 15 + 17 + 19 + 23 = 104
Notes
n is always an odd number.
Bonus points for solving it mathematically!
"""
def diamond_sum(n):
    
    if n==1:return 1
    else:
        a,b=[],[]
        for i in range(n):
            a.append([])
            for j in range(n):
                a[i].append(i*n+1+j)
        b.append(a[0][n//2])
        for i in range(1,n//2):
            b.append(a[i][n//2-i])
            b.append(a[i][-n//2+i])
        b.append(a[n//2][0])
        b.append(a[n//2][-1])
        for i in range(n//2+1,n-1):
            b.append(a[i][i-3])
            b.append(a[i][-i+2])
        b.append(a[n-1][n//2])

    return (sum(b))

diamond_sum(9)