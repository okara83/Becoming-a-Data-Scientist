#!/usr/bin/env python3

'''
Look in subdirectories for Jupyter notebooks like "subdir/notebook.ipynb" that have a 
"subdir/flashcards/notebook.json" and rerun all those "subdir/notebook.ipynb" files to
make sure that those files are using the latest JupyterCards
'''




import os
import re
import json


pattern = re.compile("DEFIN")
defns=[]
chdefns=[]
fileroot=""


for filename in os.listdir("."):

    if os.path.isdir(filename):
        #print(filename)
        fc_path=filename+"/flashcards"
        if os.path.isdir(fc_path):
            #print("\t"+"/flashcards")
            for fc_file in os.listdir(fc_path):
                #print("\t\t"+fc_file,end="")
                nb_file=filename+"/"+fc_file.split(".")[0]+'.ipynb'
                #print(",", nb_file)
                if os.path.isfile(nb_file):
                    returned=os.system("jupyter nbconvert --execute --inplace " + 
                         nb_file)
                    if returned !=0:
                        print(returned)
                    print()

print("Done")


