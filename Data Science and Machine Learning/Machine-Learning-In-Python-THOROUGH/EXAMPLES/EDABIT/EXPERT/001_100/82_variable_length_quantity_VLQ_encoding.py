"""
https://edabit.com/challenge/Zx9L2dpHr2nMjaKXp

Variable Length Quantity (VLQ) Encoding
In this challenge, you have to create functions to encode and decode variable-length quantities. A variable-length quantity (VLQ) is a universal code that uses an arbitrary number of binary octets (eight-bit bytes) to represent an arbitrarily large integer. A VLQ is essentially a base-128 representation of an unsigned integer with the addition of the eighth bit to mark a continuation of bytes.

The way it works is fairly simple. As a big-endian series of bytes, the most significant bit (MSB) of each byte is a 1 to indicate that another VLQ byte follows. The remaining 7 bits of each byte make up the decoded value.

Examples
# ENCODE:
int_to_vlq(127) ➞ [127]
# numbers between 0 and 127 are unchanged
# binary: [01111111]

int_to_vlq(128) ➞ [129, 0]
# 1st byte = 1 + 128 equivalent to 1 * 128 with MSB set to 1 indicating byte follows
# 2nd byte = 0 
# 128 + 0 ➞ 128
# binary: [10000001, 00000000]

int_to_vlq(106903) ➞ [134, 195, 23]
# 1st byte = 128 + 6 ➞ 6 * 128^2 ➞ 98304
# 2nd byte = 128 + 67 ➞ 67 * 128 ➞ 8576
# 3rd byte = 23 ➞ 23
# 98304 + 8576 + 23 = 106903
# binary: [10000110, 11000011, 00010111]

# DECODE:
vlq_to_int([229, 145, 63]) ➞ 1657023
# (229 - 128)*128^2 + (145 - 128)*128 + 63 = 1657023
"""
def int_to_vlq(n):
    a,b=[],[]
    p,r=0,n
    while r>127:
        r=r//128
        p +=1
    for i in range(p+1):
        a.append((n%(128**(p-i+1))))
    for i in range(p+1):
        if i ==0 :
            b.append((n%(128**(i+1)))//(128**i))
        else: b.append(128+(n%(128**(i+1)))//(128**i))
        n = n - n%(128**(i+1))
    return(b[::-1])    

    
def vlq_to_int(lst):
    av=[]
    for i in range(len(lst)):
        av.append((lst[i]-128)*128**(len(lst)-i-1))
    return(sum(av)+128)
           


#int_to_vlq(0) #, [0])
#int_to_vlq(12) #, [12])
#int_to_vlq(128) #, [129, 0])
#int_to_vlq(106903) #, [134, 195, 23])
#int_to_vlq(268435455) #, [255, 255, 255, 127])
#int_to_vlq(1234567890123) #, [163, 247, 143, 236, 137, 75])
int_to_vlq(562949953421312) #, [129, 128, 128, 128, 128, 128, 128, 0])
#int_to_vlq(9223372036854775807) #, [255, 255, 255, 255, 255, 255, 255, 255, 127])

# decode VLQ
#vlq_to_int([12]) #, 12 )
#vlq_to_int([129, 0]) #, 128)
#vlq_to_int([134, 195, 23]) #, 106903)
#vlq_to_int([255, 255, 255, 127]) #, 268435455)
#vlq_to_int([163, 247, 143, 236, 137, 75]) #, 1234567890123)
#vlq_to_int([129, 128, 128, 128, 128, 128, 128, 0]) #, 562949953421312)
#vlq_to_int([255, 255, 255, 255, 255, 255, 255, 255, 127]) #, 9223372036854775807)