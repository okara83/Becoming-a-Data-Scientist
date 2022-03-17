"""
Underscore-Hash Staircase
Create a function that will build a staircase using the underscore _ and hash # symbols. A positive value denotes the staircase's upward direction and downwards for a negative value.

Examples
staircase(3) ➞ "__#\n_##\n###"
__#
_##
###

staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######

staircase(2) ➞ "_#\n##"
_#
##

staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#
Notes
"""
def staircase(n):    
    a=[]
    if n>0:
        for i in range(0,n): a.append((n-1-i)*"_"+(i+1)*"#")    
    elif n<0:
        for i in range(abs(n)): a.append((i*"_")+(abs(n)-i)*"#")
    return "\n".join(a)    



staircase(7)