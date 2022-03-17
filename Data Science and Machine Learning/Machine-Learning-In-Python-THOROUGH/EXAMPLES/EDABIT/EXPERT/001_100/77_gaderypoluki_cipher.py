"""
https://edabit.com/challenge/4AzBbuPLxKfJd7aeG

Gaderypoluki Cipher
Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. 
Group the letters of the key by two:

"gaderypoluki" -> "ga de ry po lu ki"
Now take the message for encryption. If the message character appears in the key, 
replace it with an adjacent character in the grouped version of the key. 
If the message character does not appear in the key, leave it as is. 
If the letter in the key occurs more than once, the first result is used.

Return the encrypted message.

Examples
encrypt("ab c", "abc ab") ➞ "ba cba"

encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"

encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"
"""
def encrypt(key, message):
    a, d = [], {}
    for i in range(len(key)//2):
        if not key[2*i] in d: d.update({key[2*i]:key[2*i+1]})
        if not key[2*i+1] in d:d.update({key[2*i+1]:key[2*i]})
    for i in message:
        if i in key: a.append(d[i])
        else: a.append(i)
    return "".join(a)

encrypt("gaderypoluki", "This is an encrypted message") #, "Thks ks gn dncyrotde mdssgad")
#encrypt("otorhinolaryngological", "My name is Paul") #, "Mr olme hs Plua")
#encrypt("ab c","abc ab") #, "ba cba")
#encrypt("1234567890", "1029384756") #, "2910473865")