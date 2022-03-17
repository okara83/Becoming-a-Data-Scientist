"""
Throwing <N> Amount of Darts Find All Possible Combinations to Reach a Target Score
You're given a dartboard divided into sections, each section has a unique score. That means there won't be two sections with the same score.

alt text

Throwing a certain amount of valid darts, find how many solutions there are to reach the target score. Your function will be passed three parameters...

Sections: A list of values for the sections (e.g. [3, 6, 8, 11, 15, 19, 22], the list is already sorted).

Darts: The amount of darts to throw.

Target: The target score.

Return an empty list if no solution is found, otherwise a list of non-duplicate strings for each solution (e.g. ["3-11-18", "7-7-18", "7-11-14"]).

Examples
If there are duplicate values, keep only the one sorted from smallest to biggest.

"8-19-8"

"8-8-19" <-- This is the one you would keep.

"19-8-8"
Multiple solutions should be sorted before returning them.

["3-11-18", "7-7-18", "7-11-14"] is ok.

["7-11-14", "7-7-18", "3-11-18"] is not ok.
Notes
Multiple darts can land in the same section.
A dart must land in a valid section (it can't miss).


"""

def darts_solver(sections, darts, target):        
    p,q=[],[]
    if darts == 3:
        for a in sections:
            for b in sections:
                for c in sections:
                    if (a + b + c)== target:
                        z=[]
                        z.append(a)
                        z.append(b)
                        z.append(c)
                        if len(z)>1:            
                            if not (sorted(z) in p): p.append(sorted(z))
    elif darts == 4:
        for a in sections:
            for b in sections:
                for c in sections:
                    for d in sections:
                        if (a + b + c + d)== target:
                            z=[]
                            z.append(a)
                            z.append(b)
                            z.append(c)
                            z.append(d)
                            if len(z)>1:            
                                if not (sorted(z) in p):p.append(sorted(z)) 
    for i in p: 
        for j in range(len(i)): i[j]=str(i[j])
        q.append("-".join(i))
    return q

#darts_solver([3, 6, 8, 11, 15, 19, 22], 3, 35) #, ["8-8-19"])
#darts_solver([2, 4, 7, 10, 13, 18, 24], 3, 29) #, ["4-7-18"])
#darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 40) #, ["11-11-18"])
#darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 8) #, [])
darts_solver([3, 7, 11, 14, 18, 20, 25], 3, 32) #, ["3-11-18", "7-7-18", "7-11-14"])
#darts_solver([3, 7, 11, 14, 18, 20, 25, 29, 34], 3, 67) #, ["18-20-29"])
#darts_solver([3, 7, 11, 14, 18, 20, 25], 4, 23) #, ["3-3-3-14"])