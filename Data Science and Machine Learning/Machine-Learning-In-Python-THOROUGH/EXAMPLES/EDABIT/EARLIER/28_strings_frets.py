"""
Strings & Frets
Write a function that gets a string number and a fret of a 6-string guitar in 'standard tuning' and return the corresponding note. For this challenge we use a 24 fret model.

The notes are:

C, C#/Db, D, D#/Eb, E, F, F#/Gb, G, G#/Ab, A, A#/Bb, B
Try not to use a 2 dimensional list. Look at the image on the bottom to see the note names on the guitar neck.

Examples
string_fret(2, 10) ➞ "A"

string_fret(0, 16) ➞ "Invalid input"

string_fret(2, 19) ➞ "F#/Gb"

string_fret(3, 0) ➞ "G"
Notes
If the string or fret number isn't correct return "Invalid input".
24 frets on the guitar neck.
"""
def string_fret(st, fr):
    
    st_open = "EBGDAE"
    strings = [1, 2, 3, 4, 5, 6]
    notes = ["C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
    s=[]
    if not (st in strings) or (fr>24):
        return "Invalid input"
    for i in st_open:
        s.append(notes.index(i))
    return (notes[(s[st-1]+fr)%12])
    
#string_fret(2, 10) #➞ "A"
#string_fret(0, 16) #➞ "Invalid input"
string_fret(2, 19) #➞ "F#/Gb"
#string_fret(3, 0) #➞ "G"