"""
Syllabification
The syllabic structure of Persian language is CV(C)(C). C stands for consonants and V stands for Vowels. The CV(C)(C) means that there are three types of syllables in Persian:

CV
CVC
CVCC
Write a function that takes the phonetic transcription of a Persian word as an argument and returns the syllabified word based on the syllabic structure. In other word, put a period between syllables.

Examples
syllabification("kAr") ➞ "kAr"

syllabification("bArAn") ➞ "bA.rAn"

syllabification("tA") ➞ "tA"

syllabification("deraxt") ➞ "de.raxt"

syllabification("pust") ➞ "pust"

syllabification("lAjevard") ➞ "lA.je.vard"
Notes
Mono-syllabic words don't need syllabification.
Persian has six vowels: a, A, e, i, o, u
Persian has 23 consonants: p, b, t, d, k, g, G, ?, f, v, s, z, S, Z, x, h, c, j, m, n, r, l, y
Try to solve the problem by using RegEx.
Hint
Since each syllable has only one vowel, it's not necessary to know the consonants. Just knowing that there are only one consonant before the vowel and 0 to 2 consonants after the vowel is enough to solve the challenge.
"""
def syllabification(word):

    vo = ['A', 'a', 'e', 'i', 'o', 'u']  #1
    co = ['p', 'b', 't', 'd', 'c', 'J', 'G', '?', 'f', 'v', 's', 'z', 'F', '3', 'x', 'h', 'T', 'D', 'm', 'n', 'r', 'l', 'j'] #2
    a,b,d=[],[],[]    
    w= list(word)
    for i in w:
        if i in vo : a.append("1")            
        else: a.append("2")
    b="".join(a)  
    k=len(w)
    while k>0:       
        if b[-4:] == "2122":
            d.append("".join(w[-4:]))
            w,b = w[:-4], b[:-4]
        else:
            if b[-3:] == "212":
                d.append("".join(w[-3:]))
                w,b=w[:-3],b[:-3]
            else:
                if b[-2:] == "21":
                    d.append("".join(w[-2:]))
                    w,b=w[:-2],b[:-2]
        k=len(w)

    return ".".join(d[::-1])

#syllabification("kAr")#, "kAr", "example #1")
#syllabification("bArAn")#, "bA.rAn", "example #2")
#syllabification("tA")#, "tA", "example #3")
#syllabification("deraxt")#, "de.raxt", "example #4")
#syllabification("pust")#, "pust", "example #5")
#syllabification("lAjevard")#, "lA.je.vard", "example #6")
#syllabification("barAbar")#, "ba.rA.bar")
#syllabification("panjare")#, "pan.ja.re")
#syllabification("?eZdehA")#, "?eZ.de.hA")
syllabification("?Aheste")#, "?A.hes.te")