"""
Something in the Box?
Create a function that returns True if an asterisk * is inside a box.

Examples
in_box([
  "###",
  "#*#",
  "###"
]) ➞ True

in_box([
  "####",
  "#* #",
  "#  #",
  "####"
]) ➞ True

in_box([
  "*####",
  "# #",
  "#  #*",
  "####"
]) ➞ false

in_box([
  "#####",
  "#   #",
  "#   #",
  "#   #",
  "#####"
]) ➞ False
Notes
The asterisk may be in the array, however, it must be inside the box, if it exists.
"""


def in_box(lst):

    for i in lst:
        if ("#" in i) & ("*" in i):
            if (i.index("#")<i.index("*")) & (i[::-1].index("#")<i[::-1].index("*")):
                return True
    return False
    
  



in_box([
  "####",
  "#* #",
  "#  #",
  "####"
]) #➞ True

