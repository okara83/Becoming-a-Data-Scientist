"""
https://edabit.com/challenge/K7NbqZBYD5xzZLro9        EXPERT----



Sum of Digits
Create a function that takes a range of numbers and returns the sum of each digit from start to stop.

Examples
digits_sum(1, 10) ➞ 46
# total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46

digits_sum(1, 20) ➞ 102

digits_sum(1, 100) ➞ 901
Notes
start and stop are inclusive in the range.
"""
def sum1(start, stop):
	return sum(sum(map(int, str(i))) for i in range(start, stop + 1))

def sum2(digit):
	return 45 * digit * 10 ** (digit - 1)

def digits_sum(start, stop):
	digits = len(str(stop)) - 1
	return sum2(digits) - sum1(1, start - 1) + sum1(10 ** digits, stop)
    
#digits_sum(1, 20) #➞ 102

digits_sum(1, 100) #➞ 901
digits_sum(1, 100000000) #, 3600000001)