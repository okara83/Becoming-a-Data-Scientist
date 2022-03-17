"""
https://edabit.com/challenge/5D3iXJSkSreRzNS8W

Breaking News!
A local news station needs your help to generate the scrolling text for the headlines!

Create a function which returns a list of strings, where each string contains a single frame of what the scrolling text will look like.

Text will scroll from right to left.
The screen will have a width of n characters.
Start and stop when no letters appear on the screen.
The example below will demonstrate the output when the screen width is 10.

Examples
news_at_ten('edabit', 10) ➞ [
'          ',
'         e',
'        ed',
'       eda',
'      edab',
'     edabi',
'    edabit',
'   edabit ',
'  edabit  ',
' edabit   ',
'edabit    ',
'dabit     ',
'abit      ',
'bit       ',
'it        ',
't         ',
'          '
]
Notes
Every string should be n characters long, so you should pad the string with spaces if the text isn't long enough.
Similarly, if the text is too long for the screen width, then it's only possible to display a fraction of the text at a time.
See the Tests tab for more examples.
"""

def news_at_ten(txt, n):    
    a=[]
    
    if len(txt) >= n:
        for i in range(n):
            a.append(" "*(n-i)+txt[:i])
        for i in range(len(txt) - n+1):
            a.append(txt[i:n+i])
        for i in range(1,n):
            a.append(txt[-n+i:]+" "*i)
    else:
        for i in range(len(txt)+1):
            a.append(" "*(n-i)+txt[:i])
        for i in range(1, n-len(txt)+1):
            a.append(" "*(n-len(txt)-i)+ txt + " "*i)
        for i in range(1,len(txt)):
            a.append(txt[i:]+" "*(n-len(txt)+i))
    a.append(" "*n)
    return (a)


news_at_ten('edabit', 10)
#news_at_ten('The latest news from News at Ten', 17)
#news_at_ten('Hello World', 11)