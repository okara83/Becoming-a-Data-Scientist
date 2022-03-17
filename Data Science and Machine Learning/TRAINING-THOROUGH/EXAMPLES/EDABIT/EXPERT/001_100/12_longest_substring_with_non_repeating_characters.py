"""
Longest Substring with Non-repeating Characters
Write a function that returns the longest non-repeating substring for a string input.

Examples
longest_nonrepeating_substring("abcabcbb") ➞ "abc"

longest_nonrepeating_substring("aaaaaa") ➞ "a"

longest_nonrepeating_substring("abcde") ➞ "abcde"

longest_nonrepeating_substring("abcda") ➞ "abcd"
Notes
If multiple substrings tie in length, return the one which occurs first.
"""
def longest_nonrepeating_substring(txt):
        
    d = list(txt)
    b, c = [], []
    
    for i in range(len(d)-1):
        d = d[i:]
        while len(d)>1:
            for i in range(len(d)):
                if not d[i] in b:
                    b.append(d[i])
                elif d[i] in b:
                    break
            c.append("".join(b)) 
            d = d[i:]
            b = []
        d = list(txt)
        
    return (sorted(c,key = len, reverse = True)[0])
    
    
longest_nonrepeating_substring("kjlmjsdeee")  #"lmjsde"    
#longest_nonrepeating_substring("aaccddeeffb")  # "ac"    
#longest_nonrepeating_substring("abcabcbb") #➞ "abc"
#longest_nonrepeating_substring("aaaaaa") #➞ "a"
#longest_nonrepeating_substring("abcde") #➞ "abcde"
#longest_nonrepeating_substring("abcda") #➞ "abcd" 