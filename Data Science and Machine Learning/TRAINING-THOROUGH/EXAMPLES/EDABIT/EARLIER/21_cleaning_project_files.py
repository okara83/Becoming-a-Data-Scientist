"""
Cleaning Project Files
You are in the midst of organizing all of your coding projects. It's a mess! Every file you've ever created is located in the same folder.

To clean it up, you've decided that you will use one of two organization methods.

The prefix method: You will group all files with the same project name under the same folder.
The suffix method: You will group all files with the same extension under the same folder.
Create a function that takes in the current folder sorts the files according to the organization method (prefix or suffix). A folder is a grouping of files in the same list.

Examples
# Sorting by project name (ex1 and ex2)
clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix") ➞ [
  ["ex1.html", "ex1.js"],
  ["ex2.html", "ex2.js"]
]

# Sorting by extension (.html and .js)
clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix") ➞ [
  ["ex1.html", "ex2.html"],
  ["ex1.js", "ex2.js"]
]

clean_up(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix") ➞ [
  ["music_app.js", "music_app.png", "music_app.wav"],
  ["tetris.png", "tetris.js"]
]

clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "suffix") ➞ [
  ["_1.rb", "_2.rb", "_3.rb", "_4.rb"]
]

clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix") ➞ [
  ["_1.rb"], ["_2.rb"],
  ["_3.rb"], ["_4.rb"]
]
Notes
Keep elements in the same relative order.
"""
def clean_up(files, sort):
    
    a,b,c = [],[],[]
    if sort == "suffix":
        for i in files:
            a.append(i[(i.index(".")):])
        for i in a:
            if not i in b:
                b.append(i)
        for i in range(len(b)):
            k = str("c"+str(i))
            k= []
            c.append(k)
        for i in files:
            for j in b:
                if j == i[(i.index(".")):]:
                    c[b.index(j)].append(i)
        return (c)

    elif sort == "prefix":    
        for i in files:
            a.append(i[:(i.index("."))])
        for i in a:
            if not i in b:
                b.append(i)
        for i in range(len(b)):
            k = str("c"+str(i))
            k= []
            c.append(k)
        for i in files:
            for j in b:
                if j == i[:(i.index("."))]:
                    c[b.index(j)].append(i)
        return (c)


#clean_up(['project1.html', 'project2.html', 'project1.css', 'project2.css', 'project1.js', 'project2.js'], 'suffix')  
#, [['project1.html', 'project2.html'], ['project1.css', 'project2.css'], ['project1.js', 'project2.js']])


#clean_up(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix")  #➞ [
  #["music_app.js", "music_app.png", "music_app.wav"],
  #["tetris.png", "tetris.js"]
#]
clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix") #➞ [
  #["_1.rb"], ["_2.rb"],
  #["_3.rb"], ["_4.rb"]
#]