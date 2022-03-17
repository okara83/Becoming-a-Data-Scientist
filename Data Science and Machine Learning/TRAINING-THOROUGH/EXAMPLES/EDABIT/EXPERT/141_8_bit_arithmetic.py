"""
https://edabit.com/challenge/cXoBRe9RdDGeLNfaD      EXPERT

8 Bit Arithmetic
You will be given a simple string expression representing an addition or subtraction in 8-bit 2's complement arithmetic. Write a function that returns the result in base 10 followed by a binary representation. If any of the values are outside the range of 8-bit 2's complement, return "Overflow".

Examples
eight_bit("3 + 12") ➞ (15, "11 + 1100 = 1111")

eight_bit("3 - 12") ➞ (-9, "11 - 1100 = 11110111")

eight_bit("-18 - 6") ➞ (-24, "11101110 - 110 = 11101000")

eight_bit("65 + 70") ➞ "Overflow"

eight_bit("-127 + 127") ➞ (0, "10000001 + 1111111 = 0")
Notes
Numbers in 8-bit 2's complement notation can range from -128 to 127. The eighth (leftmost) bit signifies a negative number. See Resources for details.
"""
def eight_bit(exp):

    a, b, c = exp.split(" ")
    if not (-129<int(a) < 128) or not (-129 <int(c) < 128):
        return "Overflow"
    if not (-129 < eval(exp) < 128):
        return "Overflow"
    return (eval(exp), "{} {} {} = {}".format(bin(int(a))[2:] if int(a) > 0 else bin(int(a) & 255)[2:], b, bin(int(c))[2:] if int(c) > 0 else bin(int(c) & 255)[2:], bin(eval(exp) & 255)[2:]))



eight_bit("-18 - 6") #➞ (-24, "11101110 - 110 = 11101000")

#eight_bit("65 + 70") #➞ "Overflow"