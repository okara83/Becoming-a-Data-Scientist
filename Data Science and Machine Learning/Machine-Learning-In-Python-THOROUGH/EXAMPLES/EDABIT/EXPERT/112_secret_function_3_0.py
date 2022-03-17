"""
https://edabit.com/challenge/ZsAXt5Kj5EP4v3ack

Secret Function 3.0
Create a function based on the input and output. Look at the examples, there is a pattern.

Examples

Notes
Input is a string.
"""
def secret(txt):
    z=[]
    a = txt.split(">")[0]
    b= (txt.split(">")[1]).split(".")[0]
    c= (txt.split(".")[1]).split("$")[0]
    n= int(txt.split("*")[1])    
    zero = txt.count("$") -1
    z.append("<"+a+">")   
    for i in range(1,n+1):
        z.append("<" + str(b) + " class='" + str(c) + str("0"*zero)+ str(i) + "'></" + str(b)+">")       
    z.append('</' + a + '>')
    return ("".join(z))
    
    
#secret("div>p.a$$*2") #➞ `<div><p class="a01"></p><p class="a02"></p></div>`
# Only whitespace in the entire string ===  One whitespace before each class. Total " " === 2
#secret("ul>li.b$*3") #➞ `<ul><li class="b1"></li><li class="b2"></li><li class="b3"></li></ul>`
# Only whitespace in the entire string === One whitespace before each class. Total " " === 3
#secret("p>h1.c$$$*2") #➞ `<p><h1 class="c001"></h1><h1 class="c002"></h1></p>`
# Only whitespace in the entire string === One whitespace before each class. Total " " === 2

secret("ul>li.item$$$*5") #,  "<ul><li class='item001'></li><li class='item002'></li><li class='item003'></li><li class='item004'></li><li class='item005'></li></ul>"


