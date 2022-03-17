"""
https://edabit.com/challenge/KgBqna3XhRkoL2mo7

Decrypt the String from Digits to Letters
Given a string s consisting from digits and #, translate s to English lowercase characters as follows:

Characters ("a" to "i") are represented by ("1" to "9").
Characters ("j" to "z") are represented by ("10#" to "26#").
Examples
decrypt("10#11#12") ➞ "jkab"

decrypt("1326#") ➞ "acz"

decrypt("25#") ➞ "y"
Notes
N/A
"""
def decrypt(s):
    ds = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10#':'j', '11#':'k', '12#':'l',
      '13#':'m', '14#':'n', '15#':'o', '16#':'p', '17#':'q', '18#':'r', '19#':'s', '20#':'t', '21#':'u', '22#':'v',
      '23#':'w', '24#':'x', '25#':'y', '26#':'z'}
    ls=list(s)
    a, b = [], []
    
    for i in range(105): 
        if len(ls)==0:
            break
        if "#" in ls:
            for i in range(len(ls)-2):
                if ls[i+2]=="#":
                    a.append("".join(ls[i:i+3]))
                    ls=ls[:i]+ls[i+3:]
                    break
                else: 
                    a.append(ls[i])
                    ls.remove(ls[i])
                    break
        else:
            for i in range(len(ls)):
                a.append(ls[i])
                ls.remove(ls[i])
                break
    for i in a:
        b.append(ds[i])
    return "".join(b)


#decrypt("10#11#12") #, "jkab")
#decrypt("1326#") #, "acz")
#decrypt("25#") #, "y")
decrypt("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#") #, "abcdefghijklmnopqrstuvwxyz")

