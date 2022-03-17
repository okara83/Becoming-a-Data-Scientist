sentence = input("Please enter a sentence : ").lower()
constants = 0
vowels = 0
digit = 0
space = 0

for i in range(len(sentence)):
    
    if sentence[i] in set("aeiou"):
        vowels += 1
    elif sentence[i] in set("bcçdfghjklmnpqrstwxyz"):
        constants += 1
    elif sentence[i] in set("0123456789"):
        digit += 1
    elif sentence[i] in set("bcçdfghjklmnpqrstwxyz"):
        constants += 1
    elif sentence[i] in set(" "):
        space += 1        
        
print(f"Your sentence has {vowels} vowels, {constants} constants, {digit} digits and {space} spaces")