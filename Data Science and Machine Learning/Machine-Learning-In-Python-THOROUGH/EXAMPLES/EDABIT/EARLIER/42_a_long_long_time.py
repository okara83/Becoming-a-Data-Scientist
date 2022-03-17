"""
A Long Long Time
Create a function that takes three values:

h hours
m minutes
s seconds
Return the value that's the longest duration.

Examples
longest_time(1, 59, 3598) ➞ 1

longest_time(2, 300, 15000) ➞ 300

longest_time(15, 955, 59400) ➞ 59400
Notes
No two durations will be the same.
"""
def longest_time(h, m, s):
    a, b, c = h*3600, m*60, s
    if max(a,b,c) == a:
        return h
    elif max(a,b,c) == b:
        return m
    elif max(a,b,c) == c:
        return s
    

    

longest_time(1, 59, 3598)
#longest_time(15, 955, 59400) #➞ 59400