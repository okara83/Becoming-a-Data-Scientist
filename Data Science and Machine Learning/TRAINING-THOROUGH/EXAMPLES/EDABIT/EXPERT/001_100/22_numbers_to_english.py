""" 
Numbers to English
Write a function that accepts a positive integer between 0 and 999 inclusive and returns a string representation of that integer written in English.

Examples
num_to_eng(0) ➞ "zero"

num_to_eng(18) ➞ "eighteen"

num_to_eng(126) ➞ "one hundred twenty six"

num_to_eng(909) ➞ "nine hundred nine"
Notes
There are no hyphens used (e.g. "thirty five" not "thirty-five").
The word "and" is not used (e.g. "one hundred one" not "one hundred and one").
"""
def num_to_eng(n):
    
    ones = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}


    a=[]
    if n<20:
        return ones[n]
    elif n<100:
        if int(str(n)[-1])==0:
            a.append(tens[int(str(n)[0])])
            return (" ".join(a))            

        a.append(tens[int(str(n)[0])])
        a.append(ones[int(str(n)[1])])
        return (" ".join(a))

    elif n<1000:
        if int(str(n)[1:])>19:
            if int(str(n)[-1])==0:
                a.append(ones[int(str(n)[0])])
                a.append("hundred")
                a.append(tens[int(str(n)[1])])
                return (" ".join(a))            

            a.append(ones[int(str(n)[0])])
            a.append("hundred")
            a.append(tens[int(str(n)[1])])
            a.append(ones[int(str(n)[2])])
            return (" ".join(a))

        a.append(ones[int(str(n)[0])])
        a.append("hundred")
        a.append(ones[int(str(n)[1:])])
        return (" ".join(a))         


#num_to_eng(0) #, "zero")
#num_to_eng(26) #, "twenty six")
#num_to_eng(519) #, "five hundred nineteen")
num_to_eng(106) #, "one hundred six")
#num_to_eng(999) #, "nine hundred ninety nine")