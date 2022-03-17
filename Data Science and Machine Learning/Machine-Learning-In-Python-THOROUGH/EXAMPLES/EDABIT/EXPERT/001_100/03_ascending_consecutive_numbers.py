"""
Ascending Consecutive Numbers
Write a function that returns True if a string consists of ascending or ascending AND consecutive numbers.

Examples
ascending("232425") ➞ True
# Consecutive numbers 23, 24, 25

ascending("2324256") ➞ False
# No matter how this string is divided, the numbers are not consecutive.

ascending("444445") ➞ True
# Consecutive numbers 444 and 445.
"""

def ascending ( txt ) :
    splitted_txt=[split_txt(txt,step) for step in range(1,len(txt)//2+1)]
    return any([is_iterate(txt) for txt in splitted_txt])
def split_txt(txt,step):
    ch,s,splited_txt='',step,[]
    for i in txt:
        ch+=i;s-=1
        if not s: splited_txt.append(ch);ch,s='',step
    if ch!='': splited_txt.append(ch)
    return splited_txt
def is_iterate(txt):
    start,boolList=int(txt[0]),[]
    for i in txt[1:]:
        if int(i)!=start+1: return False
        else: start=int(i)
    return True