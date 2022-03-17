"""
https://edabit.com/challenge/kBXHbwQZPiLmwjrMy

English to Pig Latin Translator
Pig latin has two very simple rules:

If a word starts with a consonant move the first letter(s) of the word, till you reach a vowel, to the end of the word and add "ay" to the end.
have ➞ avehay
cram ➞ amcray
take ➞ aketay
cat ➞ atcay
shrimp ➞ impshray
trebuchet ➞ ebuchettray
If a word starts with a vowel add "yay" to the end of the word.
ate ➞ ateyay
apple ➞ appleyay
oaken ➞ oakenyay
eagle ➞ eagleyay
Write two functions to make an English to pig latin translator. The first function translate_word(word) takes a single word and returns that word translated into pig latin. The second function translate_sentence(sentence) takes an English sentence and returns that sentence translated into pig latin.

Examples
translate_word("flag") ➞ "agflay"

translate_word("Apple") ➞ "Appleyay"

translate_word("button") ➞ "uttonbay"

translate_word("") ➞ ""

translate_sentence("I like to eat honey waffles.") ➞ "Iyay ikelay otay eatyay oneyhay afflesway."

translate_sentence("Do you think it is going to rain today?") ➞ "Oday ouyay inkthay ityay isyay oinggay otay ainray odaytay?"
Notes
Regular expressions will help you not mess up the punctuation in the sentence.
If the original word or sentence starts with a capital letter, the translation should preserve its case (see examples #2, #5 and #6).
"""
# import re
# SOLUTION WITHOUT REGEX

vwl = "AEIOUaeiou"
uppr = "ZRTYPQSDFGHJKLMWXCVBN"
alf="AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn"
a,b,c,d,e,f = [], [], [], [], [], []
def translate_word(word):
    a,b,c,d,e,f = [], [], [], [], [], []

    if len(word)==0:return ""
    
    if word[0] in vwl :
        if word[-1] not in alf:
            c.append(word[-1])
            word = word[:-1]
        if len(c): return word + "yay"+c[0]
        else: return word + "yay"
        
    if word[-1] not in alf:
        c.append(word[-1])
        word = word[:-1]
    for i in range(len(word)):
        if word[i] not in vwl: b.append(word[i])
        else:
            a = word[i:]
            break
            
    if word[0] in uppr : return  (a + "".join(b)+"ay").title()  
    else: 
        if len(c): return a + "".join(b)+"ay" +c[0]
        else: return a + "".join(b)+"ay"

def translate_sentence(sentence):
    a,b,c,d,e,f = [], [], [], [], [], []
    if len(sentence)==0:return ""
    
    if '"' in list(sentence):
        s1 = sentence.split('"')[0]
        s2 = sentence.split('"')[1]

        lst1 = s1.split(" ")[:-1]
        for i in lst1: e.append(translate_word(i))

        lst2 = s2.split(" ")
        for i in lst2: f.append(translate_word(i))

        if len(c): return (" ".join(e)+' "'+ +" ".join(f) + c[0]+'"')
        else: return (" ".join(e)+' "'+ " ".join(f) +'"')    
    
    else:
        lst = sentence.split(" ")
        for i in lst: d.append(translate_word(i))
        
        if len(c): return (" ".join(d) + c[0])
        else : return (" ".join(d))

#translate_word("Apple") #➞ "Appleyay"

#translate_word("honey") #➞ "uttonbay"
#translate_sentence("I like to eat honey waffles.") #➞ "Iyay ikelay otay eatyay oneyhay afflesway."

translate_sentence('He said, "When will this all end?"')#, 'Ehay aidsay, "Enwhay illway isthay allyay endyay?"')
#translate_sentence("")#, "")