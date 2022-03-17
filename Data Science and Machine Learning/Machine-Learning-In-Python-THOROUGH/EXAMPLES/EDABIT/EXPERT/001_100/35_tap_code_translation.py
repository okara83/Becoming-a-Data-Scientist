"""
Tap Code Translation
Tap code is a way to communicate messages via a series of taps (or knocks) for each letter in the message. Letters are arranged in a 5x5 polybius square, with the letter "K" being moved to the space with "C".

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
Each letter is translated by tapping out the row and column number that the letter appears in, leaving a short pause in-between. If we use "." for each tap, and a single space to denote the pause:

text = "break"

"B" = (1, 2) = ". .."
"R" = (4, 2) = ".... .."
"E" = (1, 5) = ". ....."
"A" = (1, 1) = ". ."
"K" = (1, 3) = ". ..."
Another space is added between the groups of taps for each letter to give the final code:

"break" = ". .. .... .. . ..... . . . ..."
Write a function that returns the tap code if given a word, or returns the translated word (in lower case) if given the tap code.

Examples
tap_code("break") ➞ ". .. .... .. . ..... . . . ..."

tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"
Notes
For more information on tap code, please see the resources section. The code was widely used in WW2 as a way for prisoners to communicate.
"""
def tap_code(text):

    tt = text.split(" ")
    alf = "ABCDEFGHIJLMNOPQRSTUVWXYZK"
    n, r, p, dp = [], [] ,[], []
    for i in range(1,6):
        for j in range(1,6):
            n.append(str(i)+str(j)) 
    n.append("13")
    if tt[0][0].upper() in alf:
        for i in tt:
            for j in range(len(i)):
                i== i[:j]+ i[j+1:]
        for i in tt:
            for j in range(len(i)):        
                if i[j] in alf or i[j] in alf.lower():
                    r.append(n[alf.index(str(i[j]).upper())])
            r.append(" ")
        dgt = (list("".join(r[:-1])))
        for i in dgt:
            p.append("."*int(i))
        return " ".join(p)    
    elif tt[0][0] == ".":
        for i in range(len(tt)//2):
            dp.append(str(len(tt[2*i]))+str(len(tt[2*i+1])))
        for i in dp:
            r.append(alf[n.index(str(i))])
        return ("".join(r).lower())


tap_code("break") #➞ ". .. .... .. . ..... . . . ..."

#tap_code(".... ... ... ..... . ..... ... ... .... ....") #➞ "spent"