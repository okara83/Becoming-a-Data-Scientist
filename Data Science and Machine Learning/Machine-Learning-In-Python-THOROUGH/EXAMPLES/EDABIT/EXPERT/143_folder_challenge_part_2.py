"""
https://edabit.com/challenge/cvA35yPFAggr7rtve   EXPERT

Folder Challenge (Part #2)
This is a sequel to part #1, with the same setup, but a different goal.

A folder system on a computer might look something like the picture below:



In this challenge, folder systems will be represented by dictionaries where the keys are folders X and the value at X is the list of subfolders of X.

For example, the picture above becomes the dictionary:

{
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}
The inputs for this challenge will be:

A dictionary representing a folder system.
Two folders X and Y.
Write a function that finds the "smallest" folder containing both X and Y (in the illustration, this is the lowest folder for which you can travel down to both X and Y; or, if you view the system as a "family tree", this is the last common ancestor).

Examples
last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "B", "C") ➞ "A"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "J") ➞ "G"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "I", "K") ➞ "D"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "D", "I") ➞ "D"

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "G", "G") ➞ "G"
Notes
All the examples above use the folder system in the illustration, but the tests will use other folder systems as well.
For the purposes of this challenge, any folder is inside itself, as in the last two examples.
"""

def last_ancestor(folders, X, Y):
    ancent = {a:b for b,c in folders.items() for a in c}
    a = [c for c in ancent.values() if c not in ancent.keys()][0]
    ancent[a] = "zz"
    #print(ancent)
    while X in ancent.keys():
        y = Y
        while y in ancent.keys():
            if ancent[y] == X or y == X:
                return X
            y = ancent[y]
        X = ancent[X]

last_ancestor({
  "A": ["B", "C", "D"],
  "B": ["E", "F"],
  "D": ["G", "H"],
  "G": ["I", "J"],
  "H": ["K"]
}, "G", "G") #➞ "G"