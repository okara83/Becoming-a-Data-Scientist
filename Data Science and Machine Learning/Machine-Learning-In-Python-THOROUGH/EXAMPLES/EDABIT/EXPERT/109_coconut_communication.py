"""
https://edabit.com/challenge/Kk5Ku4CtipaFtATPT

Coconut Communication
"coconuts" has 8 letters.
A byte in binary has 8 bits.
A byte can represent a character.
We can use the word "coconuts" to communicate with each other in binary if we use upper case letters as 1s and lower case letters as 0s.

Create a function that translates a word in plain text, into Coconut.

Worked Example
The binary for "coconuts" is
01100011 01101111 01100011 01101111 01101110 01110101 01110100 01110011
c         o        c       o       n        u        t       s

Since 0s are lowercase and 1s are uppercase, we can map the binary like this.
cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS

coconut_translator("coconuts") ➞ "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS"
Examples
coconut_translator("Hi") ➞ "cOcoNuts cOCoNutS"

coconut_translator("edabit") ➞ "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts"

coconut_translator("123") ➞ "coCOnutS coCOnuTs coCOnuTS"
Notes
All inputs will be strings.
Make sure to separate the coconuts with spaces.
"""
def coconut_translator(txt):
    if len(txt)==0: return ""
    key, key1, byte_list, a , b = "oconuts","conuts", [], [], []
        
    for i in txt :
        if i in "0123456789": a.append(["co"])
        else:a.append(["c"])

    a_byte_array = bytearray(txt, "utf8")  #Create bytearray
    
    for byte in a_byte_array:
        binary_representation = bin(byte)  #Convert to binary
        byte_list.append(binary_representation[2:])  #Add to list

    for i in range(len(byte_list)):
        for j in range(len(byte_list[i])):
            if txt[i] in "0123456789":
                if byte_list[i][j] == "0": a[i].append(key1[j].lower())
                else: a[i].append(key1[j].upper())            
            else:
                if byte_list[i][j] == "0": a[i].append(key[j].lower())
                else: a[i].append(key[j].upper())

    for i in a: b.append("".join(i))
    return (" ".join(b))
                
#coconut_translator("Hi") #, "cOcoNuts cOCoNutS")
#coconut_translator("edabit") #, "cOConUtS cOConUts cOConutS cOConuTs cOCoNutS cOCOnUts")
coconut_translator("123") #, "coCOnutS coCOnuTs coCOnuTS")
#coconut_translator("coconuts") #, "cOConuTS cOCoNUTS cOConuTS cOCoNUTS cOCoNUTs cOCOnUtS cOCOnUts cOCOnuTS")
#coconut_translator("") #, "")