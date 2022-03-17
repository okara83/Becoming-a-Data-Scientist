"""Distance to Nearest Vowel
Write a function that takes in a string and for each character, returns the distance to the nearest vowel in the string. If the character is a vowel itself, return 0.

Examples
distance_to_nearest_vowel("aaaaa") ➞ [0, 0, 0, 0, 0]

distance_to_nearest_vowel("babbb") ➞ [1, 0, 1, 2, 3]

distance_to_nearest_vowel("abcdabcd") ➞ [0, 1, 2, 1, 0, 1, 2, 3]

distance_to_nearest_vowel("shopper") ➞ [2, 1, 0, 1, 1, 0, 1]
Notes
All input strings will contain at least one vowel.
Strings will be lowercased.
Vowels are: a, e, i, o, u."""

def distance_to_nearest_vowel(txt):
    
    vow = list("aeiou")    
    a, b, c = [], [], []
    for i in range(len(txt)):
        b, c = [], []
        if txt[i] in vow:
            a.append(0)
        else:    
            for j in range(1,i+1):
                if txt[i-j] in vow:
                    b.append(j)
            for k in range(i,len(txt)):
                if txt[k] in vow:
                    c.append(k-i)
            if len(b)==0:a.append(min(c))
            elif len(c)==0:a.append(min(b))    
            else:a.append(min(min(b),min(c)))   
    return a

#distance_to_nearest_vowel("aaaaa") #➞ [0, 0, 0, 0, 0]
#distance_to_nearest_vowel("babbb") #➞ [1, 0, 1, 2, 3]
distance_to_nearest_vowel("abcdabcd") #➞ [0, 1, 2, 1, 0, 1, 2, 3]
#distance_to_nearest_vowel("shopper") #➞ [2, 1, 0, 1, 1, 0, 1]

