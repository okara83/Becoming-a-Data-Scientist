"""
https://edabit.com/challenge/mm2fm6ynbR7HQQm9z    EXPERT ----


Knights Jump
Knights can jump across the board.

Knights in Chess

Create a function that takes a square where a knight jumps from as a string and returns all the possible squares the knight can land on as a string. Ignore capturing and further Chess rules. Be aware of the sides of the board. Knights don't go over the edge, obviously.

Examples
knights_jump("F4") ➞ "E2,G2,D3,H3,D5,H5,E6,G6"

knights_jump("A1") ➞ "C2,B3"

knights_jump("E2") ➞ "C1,G1,C3,G3,D4,F4"
Notes
The input is always a valid square on the board.
The order of the return string is 1 ➞ 8, A ➞ H.
"""



def knights_jump(square):
    
    # Solution 1:
    #c = int(square[1]) - 1
    #r = ord(square[0]) - 65
    #result = []
    #for c2 in range(8):
        #for r2 in range(8):
            #if sorted([abs(r - r2), abs(c - c2)]) == [1, 2]:
                #result.append(chr(65+r2) + str(1+c2))
    #return ','.join(result)

    ### SOLUTION 2 ### LIST COMPRHENSION ###
    c, r  = int(square[1]) - 1, ord(square[0]) - 65    
    return ','.join([chr(65+r2) + str(1+c2) for c2 in range(8) for r2 in range(8) if sorted([abs(r - r2), abs(c - c2)]) == [1, 2]])
    
    
knights_jump("F4") #➞ "E2,G2,D3,H3,D5,H5,E6,G6"