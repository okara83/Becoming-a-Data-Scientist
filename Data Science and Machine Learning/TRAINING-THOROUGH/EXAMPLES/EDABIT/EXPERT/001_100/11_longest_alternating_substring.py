"""
Longest Alternating Substring
Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. If two or more substrings have the same length, return the substring that occurs first.

Examples
longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.
"""

def longest_substring(digits):
    
    even = "02468"
    odd = "13579"
    d = list(digits)
    d.append("2")
    d.append("2")
    d.append("2")
    b, c = [], []
        
    while len(d)>2:
        for i in range(len(d)-1):
            b.append(d[i])
            if len(b)>1:
                if (b[i-1] in odd and b[i] in even) or (b[i-1] in even and b[i] in odd):
                    continue
                else: 
                    break
        c.append("".join(b[:-1])) 
        d = d[len(b)-1:]
        b = []
    

    return (sorted(c,key = len, reverse = True)[0])




    
#longest_substring("225424272163254474441338664823") #➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") #➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

#longest_substring("721449827599186159274227324466") #➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first.