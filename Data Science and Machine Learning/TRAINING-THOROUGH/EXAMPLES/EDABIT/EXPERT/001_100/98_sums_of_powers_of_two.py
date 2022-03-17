"""
https://edabit.com/challenge/yyCGJKP442qtTD9Ek

Sums of Powers of Two
Every number can be expressed as the sum between unique powers of two. For example, the number 21 can be expressed as 1 + 4 + 16, which can also be written as 2^0 + 2^2 + 2^4.

Create a function that returns a sorted list of powers of two, which add together to make n.

Examples
sums_of_powers_of_two(21) ➞ [1, 4, 16]
sums_of_powers_of_two(8) ➞ [8]
sums_of_powers_of_two(63) ➞ [1, 2, 4, 8, 16, 32]
Notes
Tests will only include positive whole numbers.
"""
def sums_of_powers_of_two(n):
    a=[]
    lst = list(bin(n)[2:][::-1])
    for i in range(len(lst)):
        if int(lst[i]): a.append(2**i)
    return a


sums_of_powers_of_two(556846320)#, [16, 32, 64, 128, 1024, 2048, 16384, 32768, 1048576, 2097152, 16777216, 536870912])
#sums_of_powers_of_two(509104470)#, [2, 4, 16, 64, 256, 4096, 16384, 524288, 1048576, 4194304, 33554432, 67108864, 134217728, 268435456])
#sums_of_powers_of_two(929640411)#, [1, 2, 8, 16, 64, 128, 256, 512, 1024, 2048, 8192, 65536, 524288, 2097152, 4194304, 16777216, 33554432, 67108864, 268435456, 536870912])    