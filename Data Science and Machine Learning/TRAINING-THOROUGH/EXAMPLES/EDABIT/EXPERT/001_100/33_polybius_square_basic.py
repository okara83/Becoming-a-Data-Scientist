"""
Polybius Square (Basic)
The Polybius Square cipher is a simple substitution cipher that makes use of a 5x5 square grid. The letters A-Z are written into the grid, with "I" and "J" typically sharing a slot (as there are 26 letters and only 25 slots).

1	2	3	4	5
1	A	B	C	D	E
2	F	G	H	I/J	K
3	L	M	N	O	P
4	Q	R	S	T	U
5	V	W	X	Y	Z
To encipher a message, each letter is merely replaced by its row and column numbers in the grid.

Create a function that takes a plaintext or ciphertext message, and returns the corresponding ciphertext or plaintext.

Examples
polybius("Hi") ➞ "2324"

polybius("2324  4423154215") ➞ "hi there"

polybius("543445 14343344 522433 21422415331443 52244423 4311311114") ➞ "you dont win friends with salad"
Notes
As "I" and "J" share a slot, both are enciphered into 24, but deciphered only into "I" (see third and fourth test).
"""

def polybius(text):
    tt = text.split(" ")
    alf = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    d = "0123456789"
    n, r = [] ,[]    
    for i in range(1,6):
        for j in range(1,6):
            n.append(str(i)+str(j)) 

    if not tt[0][0].upper() in d:                
        for i in tt:
            for j in range(len(i)):
                if i[j] == "J" or i[j]==("j"):
                    r.append("24")
                elif not i[j] in (alf or alf.upper()):
                    i== i[:j]+ i[j+1:]
        
        for i in tt:
            for j in range(len(i)):        
                if i[j] in alf or i[j] in alf.lower():
                    r.append(n[alf.index(str(i[j]).upper())])
            r.append(" ")
        return ("".join(r[:-1]))
 
    elif tt[0][0] in d:
        for i in tt:
            for j in range(len(i)//2):
                r.append(alf[n.index(str(i[2*j:2*j+2]))])
            r.append(" ")
        return ("".join(r[:-1]).lower())


polybius('4323343531242144243322 2443 11 51241344243231154343 1342243215 31242515 3545331323243322 43343215343315 2433 442315 14114225') #, "shoplifting is a victimless crime like punching someone in the dark")
#polybius('Hi')  #, '2324')
#polybius("Just because I don't care doesn't mean that I don't understand")  #, '24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314')  #, "Disregard punctuation, but keep spaces")
#polybius('24454344 12151311454315 24 14343344 13114215 143415433344 32151133 44231144 24 14343344 45331415424344113314') #, 'iust because i dont care doesnt mean that i dont understand')
#polybius('543445 14343344 522433 21422415331443 52244423 4311311114') #, 'you dont win friends with salad')
#polybius('The lesson is: never try') #, '442315 311543433433 2443 3315511542 444254')
