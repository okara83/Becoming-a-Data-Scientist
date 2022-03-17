"""
Fauna in Chitwan National Park
Create a function that takes a string containing both name and number of animals and plants that may or may not be found in Chitwan National Park. The function should return a list of tuples where first element in the tuple is animal name and second element in the tuple is number of that particular animal that is found in Chitwan National Park.

Animals Present in Chitwan National Park
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
Examples
fauna_number("There are 24 one-hornedrhino,50 python and 20000 mango.") ➞ [("one-hornedrhino", "24"), ("python", "50")]
# Mango not present in animal list.

fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples .") ➞ [("bengaltiger", "244"), ("monitorlizard", "200")]
# Apples not present in animal list.
Notes
Input contains name and number of both animals and plants.
If there is no match, return an empty list.
"""
def fauna_number(txt):
    
    animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
    a= txt.split()
    b,c=[],[]    
    for i in a:
        if "," in list(i):
            for j in i.split(","): b.append(j)
        else: b.append(i)
    for i in range(len(b)):
        if b[i] in animals:
            c.append((b[i],b[i-1]))    
    return c


#fauna_number("There are 24 one-hornedrhino,50 python and 20000 bees.")
#,[('one-hornedrhino', '24'), ('python', '50')])
#fauna_number("There are 244 bengaltiger,200 monitorlizard and 5000 apples.")
#,[('bengaltiger', '244'), ('monitorlizard', '200')])
#fauna_number("There are 2444 saltrees,2000 cobra and 5000 mangotrees.")
#[])
fauna_number("There are 180 muggercrocodile,20 krait and 500 taipan.")
#,[('muggercrocodile', '180')])
