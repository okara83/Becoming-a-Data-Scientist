"""
https://edabit.com/challenge/L2CW7yoxZK3RWB2Kc

Nico Cipher
In Nico Cipher, encoding is done by creating a numeric key and assigning each letter position of the message with the provided key.

Create a function that takes two arguments, key and message, and returns the encoded message.

There are some variations on the rules of encipherment. One version of the cipher rules are outlined below:

message = "mubashirhassan"
key = "crazy"

nico_cipher(message, key) ➞ "bmusarhiahass n"
Step 1: Assign numbers to sorted letters from the key:

"crazy" = 23154
Step 2: Assign numbers to the letters of the given message:

2 3 1 5 4
---------
m u b a s
h i r h a
s s a n
Step 3: Sort columns as per assigned numbers:

1 2 3 4 5
---------
b m u s a
r h i a h
a s s   n
Step 4: Return encoded message Rows-wise:

eMessage = "bmusarhiahass n"
Examples
nico_cipher("mubashirhassan", "crazy") ➞ "bmusarhiahass n"

nico_cipher("edabitisamazing", "matt") ➞ "deabtiismaaznig "

nico_cipher("iloveher", "612345") ➞ "lovehir    e"
"""
def nico_cipher(message, key):
    
    sk=sorted(key)
    nl, temp, result =[], [], []    #nl:num list
    for i in key:
        if not sk.index(i) in nl: nl.append(sk.index(i))
        else: nl.append(sk.index(i)+1)
    
    ln = len(message)//len(key)+1 #line number
    sn = len(key) - (len(message) - (ln-1)*len(key)) #space number
    for i in range(ln): temp.append(list(message[len(key)*i:len(key)*(i+1)]))
    for i in range(sn): temp[-1].append(" ") 
    for i in temp:
        for j in range(len(key)): result. append(i[nl.index(j)])
    return "".join(result)        
    

#nico_cipher("mubashirhassan", "crazy")#, "bmusarhiahass n")
#nico_cipher("edabitisamazing", "matt")#, "deabtiismaaznig ")
#nico_cipher("Pakistanisamazing", "airforce")#, "Paniasktiinmsaazg       ")
#nico_cipher("iloveher", "612345"), "lovehir    e")
nico_cipher("iwillquitsoon", "endisnear")#, "iiiulwqtl os no   ")