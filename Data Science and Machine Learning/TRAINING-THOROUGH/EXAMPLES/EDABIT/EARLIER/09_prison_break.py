"""
Prison Break
A prison can be represented as a list of cells. Each cell contains exactly one prisoner. A 1 represents an unlocked cell and a 0 represents a locked cell.

[1, 1, 0, 0, 0, 1, 0]
Starting from the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch. Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.

So, if we use the example above:

[1, 1, 0, 0, 0, 1, 0] 
# You free the prisoner in the 1st cell.

[0, 0, 1, 1, 1, 0, 1] 
# You free the prisoner in the 3rd cell (2nd one locked).

[1, 1, 0, 0, 0, 1, 0]
# You free the prisoner in the 6th cell (3rd, 4th and 5th locked).

[0, 0, 1, 1, 1, 0, 1]
# You free the prisoner in the 7th cell - and you are done!
Here, we have freed 4 prisoners in total.

Create a function that, given this unique prison arrangement, returns the number of freed prisoners.

Examples
freed_prisoners([1, 1, 0, 0, 0, 1, 0]) ➞ 4

freed_prisoners([1, 1, 1]) ➞ 1

freed_prisoners([0, 0, 0]) ➞ 0

freed_prisoners([0, 1, 1, 1]) ➞ 0
Notes
You must free a prisoner in order for the locks to switch. So in second example where the input is [1, 1, 1], after you release the first prisoner, the locks change to [0, 0, 0]. Since all cells are locked, you can release no more prisoners.
You always start with the leftmost element in the list (the first prison cell). If all the prison cells to your right are zeroes, you cannot free any more prisoners.
"""
def freed_prisoners(prison):
    
    ff=[]
    
    if prison[0] == 0:
        return 0
    
    if prison[0] == 1:
        ff.append(1)

    a=[]
    for i in prison:
        if i == 0:
            a.append(1)
        else:
            a.append(0)     
    prison = a
    if prison[1] == 1:
        ff.append(1)
    
    for k in range(1, len(prison)-1):
        a=[]
        if prison[k] == 1:
            for i in prison:
                if i == 0:
                    a.append(1)
                else:
                    a.append(0)
        else:
            a=prison
        prison = a
        if prison[k+1] == 1:
            ff.append(1) 

    
    return(sum(ff))


#freed_prisoners([1, 1, 0, 0, 0, 1, 0]) #➞ 4
freed_prisoners([1, 0, 1, 0, 1, 0])  #➞ 6
#freed_prisoners([0, 1, 1, 1]) #➞ 0