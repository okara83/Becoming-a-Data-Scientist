"""
https://edabit.com/challenge/pGRAtBbwSMjpXNGnP   EXPERT 


Sorted List of Words
The function is given a list of words and a new alphabet (English letters in different order). Determine if the list of words is sorted lexicographically. The words consist of lower case letters.

Examples
is_sorted(["hello", "edabitlot"], "hlabcdefgijkmnopqrstuvwxyz") ➞ True

is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") ➞ False

is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") ➞ False

is_sorted(["deceased", "folks", "can", "vote"], "abdefghijklmnopqrstcuvwxyz") ➞ True
Notes
N/A
"""
def is_sorted(words, alphabet):
    #if words == []:
        #return True
    for i in range(len(words)-1):
        text1, text2 = words[i], words[i+1]
        if len(words[i]) > min(len(text1), len(text2)): 
            if words[i+1] == words[i][0:min(len(text1), len(text2))]:
                 return False
        for j in range(min(len(text1), len(text2))):            
            if alphabet.find(words[i][j]) > alphabet.find(words[i+1][j]):
                if all(words[i][k] == words[i+1][k] for k in range(j)):            
                    return False
    return True




is_sorted(["hello", "edabitlot"], "hlabcdefgijkmnopqrstuvwxyz") #➞ True

is_sorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") #➞ False

#is_sorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") #➞ False

#is_sorted(["deceased", "folks", "can", "vote"], "abdefghijklmnopqrstcuvwxyz") #➞ True