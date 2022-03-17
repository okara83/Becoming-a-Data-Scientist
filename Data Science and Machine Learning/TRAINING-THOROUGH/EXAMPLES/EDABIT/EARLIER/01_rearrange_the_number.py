"""
Rearrange the Number
Given a number, return the difference between the maximum and minimum numbers that can be formed when the digits are rearranged.

Examples
rearranged_difference(972882) ➞ 760833
# 988722 - 227889 = 760833

rearranged_difference(3320707) ➞ 7709823
# 7733200 - 23377 = 7709823

rearranged_difference(90010) ➞ 90981
# 91000 - 19 = 90981
Notes
N/A
"""
def rearranged_difference(num):

    return (int("".join(sorted(list(str(num)),reverse = True)))) - int("".join(sorted(list(str(num)))))
    
rearranged_difference(3320707)