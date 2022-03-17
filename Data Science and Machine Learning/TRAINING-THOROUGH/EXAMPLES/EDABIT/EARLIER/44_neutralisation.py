"""
Neutralisation
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
Worked Example
neutralise("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
Examples
neutralise("--++--", "++--++") ➞ "000000"

neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"

neutralise("-++-", "-+-+") ➞ "-+00"
"""
def neutralise(s1, s2):
    a = []
    for i in range(len(s1)):
        if s1[i] == "+":
            if s2[i]== "+":
                a.append("+")
            if s2[i]== "-":
                a.append("0")
        if s1[i] == "-":
            if s2[i]== "+":
                a.append("0")
            if s2[i]== "-":
                a.append("-")

    return "".join(a)      
            

neutralise("-++-", "-+-+") #➞ "-+00"