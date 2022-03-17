"""
https://edabit.com/challenge/FgAsxMCaEzvKhnuAH

Deep Arithmetic
Create a function that takes an array of strings of arbitrary dimensionality ([], [][], [][][], etc) and returns the deep_sum of every separate number in each string in the array.

Examples
deep_sum(["1",  "five",  "2wenty",  "thr33"]) ➞ 36

deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) ➞ 1099

deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) ➞ 759
Notes
Numbers in strings can be negative, but will all be base-10 integers.
Negative numbers may directly follow another number.
The hyphen or minus character ("-") does not only occur in numbers.
Arrays may be ragged or empty.
actual_param = [
  ["1", "five", "2wenty", "thr33"],
  [["1X2", "t3n"],["1024", "5", "64"]],
  [[["1"], "10v3"], ["738h"], [["s0"], ["1mu4ch3"], "-1s0"]],
  [[["0", "0x2", "z3r1"],["1", "55a46"]],[["1", "0b2", "4"],["0x5fp-2", "nine", "09"],["4", "4", "4"]],[["03"]], []],
  [[[[[[[[[[[[[[[["-1", "1"], ["3"], [""], []]]]]]]]]]]]]]]],
  [[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]],
  [[[[[["-32-64", "a-zA-Z"], ["01-1"]]]]]]
]
expected_param = [36, 1099, 759, 142, 3, 0, -96]

"""
def deep_sum(lst):
    a,b,c,rr=[],[],[],[]
    num="0123456789"
    for t in range(20): 
        for i in lst:
            if type(i)==list:
                for j in i:b.append(j)
            else:b.append(i)  
        if lst==b : break
        else:lst=b
        b=[]
    for i in b:
        e=[]
        if not len(i)==0:
            if i[0]=='-':
                if len(i)>0:
                    e=list(i)
                    for k in range(1,len(i)):
                        if not i[k] in num:
                            e.remove(i[k])
                            if i[k]=='-': 
                                b.append("".join(i[k:]))
                            elif not i[k] in num:
                                b.append("".join(i[k+1:]))
                            c.append("".join(i[0:k]))
                            break
                if e==list(i) :
                    c.append("".join(e))
            elif not (i[0] in num or i[0]=='-'):
                b.append(i[1:])
            else:
                e=list(i)
                for k in range(0,len(i)):
                    if not i[k] in num:
                        e.remove(i[k])
                        if i[k]=='-': 
                            b.append("".join(i[k:]))
                        elif not i[k] in num:
                            b.append("".join(i[k+1:]))
                        c.append("".join(i[0:k]))
                        break
                if e==list(i) :
                    c.append("".join(e))
    for i in c:
        if not (i=='' or i=="-"):rr.append(int(i))    
    return (sum(rr))
    
    
    

deep_sum(["1",  "five",  "2wenty",  "thr33"]) #➞ 36    
#deep_sum([[[[[["-32-64", "a-zA-Z"], ["01-1"]]]]]])  #-96
#deep_sum([["1X2",  "t3n"], ["1024", "5", "64"]]) #➞ 1099
#deep_sum([[["1"], "10v3"],  ["738h"],  [["s0"],  ["1mu4ch3"], "-1s0"]]) #➞ 759    
#deep_sum([[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]])
#deep_sum([[["0", "0x2", "z3r1"],["1", "55a46"]],[["1", "0b2", "4"],["0x5fp-2", "nine", "09"],["4", "4", "4"]],[["03"]], []])  #142