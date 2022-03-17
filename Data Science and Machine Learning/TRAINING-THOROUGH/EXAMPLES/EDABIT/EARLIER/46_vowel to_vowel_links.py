"""
Vowel to Vowel Links
Given a sentence as txt, return True if any two adjacent words have this property: 
One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
Notes
You can expect sentences in only lowercase.
"""
def vowel_links(txt):
    
    a, v = list(txt.split(" ")), "aeiou"
    for i in range(len(a)-1) :
        if (a[i][-1] in v) and ((a[i+1])[0] in v):
            return True
    return False    

vowel_links("a very large appliance") #➞ True
#vowel_links("go to edabit") #➞ True
#vowel_links("an open fire") #➞ False
#vowel_links("a sudden applause") #➞False