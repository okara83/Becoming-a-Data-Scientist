"""
https://edabit.com/challenge/9Px2rkc9TPhK54wDb
The ECG Sequence
In the ECG Sequence (that always starts with the numbers 1 and 2), every number that succeeds is the smallest not already present in the sequence and that shares a factor (excluding 1) with its preceding number. Every number in the ECG Sequence (besides 1 and 2) has a different index from its natural index in a normal numeric sequence. See the example below to establish the ECG Sequence Index of number 3.

# Find the smallest number that is not in sequence...
# This number shares a factor with the preceding?

SEQUENCE = [1, 2]

3 = no factors shared with 2
4 = shares factor 2 with number 2

SEQUENCE = [1, 2, 4]

3 = no factors shared with 4
5 = no factors shared with 4
6 = shares factor 2 with number 4

SEQUENCE = [1, 2, 4, 6]

3 = shares factor 3 with number 6

SEQUENCE = [1, 2, 4, 6, 3]

Number 3 is at index 4 in the ECG Sequence.
Given an integer n implement a function that returns its ECG Sequence Index.

Examples
ecg_seq_index(3) ➞ 4

ecg_seq_index(5) ➞ 9

ecg_seq_index(7) ➞ 13
Notes
ECG is the acronym for the electrocardiogram: if you try to graphically represent the trend of the sequence, a similar scheme appears.
Curiosity: every odd prime p in the sequence is preceded by 2p and followed by 3p.
"""

from fractions import Fraction as frac 
def ecg_seq_index(n):
    a,b,c=[] , [1, 2], []
    for i in range(3,3*n):
        a.append(i)
    
    while not n in b:
        for k in range(2*len(a)):
            txt=str(a[k]) + "/" + str(b[-1])
            if str(frac(txt)) != str(txt): 
                b.append(a[k])
                a.remove(a[k])
                break
            else:
                for m in range(k):
                    txt2 = str(a[m]) + "/" + str(b[-1])
                    if str(frac(txt2)) != str(txt2):
                        if not a[m] in b:
                            b.append(a[m])
                            a.remove(a[m])
                            break
    return b.index(n)

ecg_seq_index(300)