"""
Phone Letter Combinations
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Alternative Text

Examples
letter_combinations("23") ➞ ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

letter_combinations("532") ➞ ["jda", "jdb", "jdc", "jea", "jeb", "jec", "jfa", "jfb", "jfc", "kda", "kdb", "kdc", "kea", "keb", "kec", "kfa", "kfb", "kfc", "lda", "ldb", "ldc", "lea", "leb", "lec", "lfa", "lfb", "lfc"]
Notes
"""

def letter_combinations(digits):
    
    ln = len(digits)
    
    letters = "abcdefghijklmnopkrstuvwxyz"
    
    dict_lttrs = { "d2" : list(letters)[0:3], "d3" : list(letters)[3:6], "d4" : list(letters)[6:9] , "d5" : list(letters)[9:12] , "d6" : list(letters)[12:15] , "d7" : list(letters)[15:19] , "d8" : list(letters)[19:22] , "d9" : list(letters)[22:26] }
       
    combine = []
        
    if ln == 1:
        return "".join(dict_lttrs["d"+ str(digits)])
        
    elif ln == 2:
        for i in dict_lttrs["d"+ str(digits[0])]:
            for j in dict_lttrs["d"+ str(digits[1])]:
                combine.append(i + j)    
    elif ln == 3:
        for i in dict_lttrs["d"+ str(digits[0])]:
            for j in dict_lttrs["d"+ str(digits[1])]:
                for k in dict_lttrs["d"+ str(digits[2])]:
                    combine.append(i + j + k)                    
    elif ln == 4:
        for i in dict_lttrs["d"+ str(digits[0])]:
            for j in dict_lttrs["d"+ str(digits[1])]:
                for k in dict_lttrs["d"+ str(digits[2])]:
                    for l in dict_lttrs["d"+ str(digits[3])]:
                        combine.append(i + j + k + l)                                    
    elif ln == 5:
        for i in dict_lttrs["d"+ str(digits[0])]:
            for j in dict_lttrs["d"+ str(digits[1])]:
                for k in dict_lttrs["d"+ str(digits[2])]:
                    for l in dict_lttrs["d"+ str(digits[3])]:
                        for m in dict_lttrs["d"+ str(digits[4])]:
                            combine.append(i + j + k + l + m)                   
                      
    return combine
letter_combinations("532")