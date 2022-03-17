"""
Next in the Alphabet
Create a function which returns the next letters alphabetically in a given string. If the last letter is a "Z", change the rest of the letters accordingly.

Examples
next_letters("A") ➞ "B"

next_letters("ABC") ➞ "ABD"

next_letters("Z") ➞ "AA"

next_letters("CAZ") ➞ "CBA"

next_letters("") ➞ "A"
Notes
Tests will all be in CAPITALS.
Empty inputs should return a capital "A" (as if it were in letter position 0!).
Think about the letter "Z" like the number 9 and how it carries over to increment the next letter/digit over.
"""
def next_letters(s):

    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
    d = list(range(len(alf)+1))
    st= list(s)[::-1]
    a, b = [], []    
    if s == "" : return "A"
    if s == "Z" : return "AA"
    if st[0] != "Z":
        st[0] = alf[int(d[alf.index(st[0])])+1]
    elif st[0] == "Z":        
        for i in range(len(st)-1):
            b.append(st[i])
            if st[i +1] != "Z":
                break
            if st.count("Z")==len(s):
                return( "A"*(len(s)+1))
        for i in range(len(b)):
            st[i] = "A"
        st[len(b)] = alf[int(d[alf.index(st[len(b)])])+1]
    return "".join(st[::-1])



#next_letters("A") #, "B")
#next_letters("ABC") #, "ABD")
#next_letters("Z") #, "AA")
#next_letters("CAZ") #, "CBA")
#next_letters("AAA") #, "AAB")
#next_letters("ZYZ") #, "ZZA")
#next_letters("ZZZ") #, "AAAA")
#next_letters("ACZZZ") #, "ADAAA") !!!!!!!!!!
next_letters("ZZZAZAZAZAZAZZZZ") #, "ZZZAZAZAZAZBAAAA") !!!!!!!!!!!!!!
#next_letters("") #, "A")
#next_letters("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ") #, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")!
#next_letters("EDABIS") #, "EDABIT")
#next_letters("JOSHTZ") #, "JOSHUA")