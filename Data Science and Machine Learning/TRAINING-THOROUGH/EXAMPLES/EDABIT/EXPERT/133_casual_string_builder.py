"""
https://edabit.com/challenge/F9r7cuye3EbNRBtjx    EXPERT

Casual String Builder
The function is given a string with some square brackets in it. You need to build the outcome string using the rule: k[substring] is replaced by the substring inside the square brackets being repeated exactly k times.

Examples
string_builder("3[a]2[bc]") ➞ "aaabcbc"

string_builder("3[a2[c]]") ➞ "accaccacc"

string_builder("2[abc]3[cd]ef") ➞ "abcabccdcdcdef"
Notes
k is a positive integer.
"""


def string_builder(s):
    
    #t_sec = 0.001053
    if len(s)==0: return ''
    if s[0]>'9': return s[0]+string_builder(s[1:])
    
    n= s.index(']')
    while s[:n].count('[') > s[:n+1].count(']'):
        n=s.index(']',n+1)

    st=1
    if s[1]<='9': st=2
    return string_builder(s[st+1:(n)]*int(s[0:st])) + string_builder(s[n+1:])


#REGEX
#import re
#t_sec = 0.000412

#def string_builder(s):
    #while '[' in s:
        #s = re.sub(r'(\d+)\[(\w+)\]', lambda x: int(x.group(1)) * x.group(2), s)
    #return s


string_builder("3[a]2[bc]") #➞ "aaabcbc"

#string_builder("3[a2[c]]") #➞ "accaccacc"

#string_builder("2[abc]3[cd]ef") #➞ "abcabccdcdcdef"