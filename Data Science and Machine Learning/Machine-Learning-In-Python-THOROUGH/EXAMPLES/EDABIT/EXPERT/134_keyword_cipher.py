"""
https://edabit.com/challenge/7Y2C8g3fXXyK2R9Bn  EXPERT 

Keyword Cipher
A Keyword Cipher is a monoalphabetic cipher which uses a keyword to provide encryption on given string of message.

Create a function that takes two arguments: a string message and a string key, and returns an encoded message.

For the encryption key, the keyword is placed at the beginning, followed by the rest of the characters in the alphabet in order (in other words, with the keyword characters removed):

A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z
The encrypted message substitutes each plaintext character with the encryption key character in the corresponding position.

Return the given message encrypted against the key:

eMessage = "KEYABC"
// A = K, B = E, C = Y, H = A, I = B, J = C
Examples
keyword_cipher("keyword", "abchij") ➞ "keyabc"

keyword_cipher("purplepineapple", "abc") ➞ "pur"

keyword_cipher("mubashir", "edabit") ➞ "samucq"
Notes
Don't forget to remove duplicates after concatenating string with keyword.
Non-alphabetic characters must be left as they are.
"""
def keyword_cipher(key, message):
    
    alph = list("abcdefghijklmnopqrstuvwxyz")
    new1 = []
    for i in key:
        if not i in new1: new1.append(i)       
    new = new1 + [j for j in alph if not j in list(key)] 
    a=[alph.index(i) if i in alph else i for i in message ]
    
    return "".join([new[i] if type(i)== int else i for i in a])

#keyword_cipher("keyword", "abchij") #➞ "keyabc"

#keyword_cipher("purplepineapple", "abc") #➞ "pur"

#keyword_cipher("mubashir", "edabit") #➞ "samucq"
#keyword_cipher("purplepineapple","xyz")#, "xyz")

#keyword_cipher("tfozcivbsjhengarudlkpwqxmy","tjuukf") #, "kjpphi")
#keyword_cipher("tfozcivbsjhengarudlkpwqxmy","ajqqtb") #, "tjuukf")
keyword_cipher("tfozcivbsjhengarudlkpwqxmy","a_bc&*83") #, "t_fo&*83")