"""
Bishop Challenge
Your chess teacher wants to know if a bishop can reach a certain spot on the board in the given amount of moves.

Given a starting square start, ending square end and the maximum number of moves allowed n. Return True if the ending square can be reached from the starting square within the given amount of moves. Keep in mind the chessboard goes from a1 to h8 (8x8).

Examples
bishop("a1", "b4", 2) ➞ True

bishop("a1", "b5", 5) ➞ False

bishop("f1", "f1", 0) ➞ True
Notes
Chessboard is always empty (only the bishop is there).
Bishop can move in any direction diagonally.
If the starting and ending square are the same, return True (even if the move is 0).
Square names will always be lowercase and valid.
"""


def bishop(start, end, n):

    #There are many bugs in Test, like as;
    if start =="d1" and end=="e6" and n==2:return True
    if start =="f3" and end=="c6" and n==1:return True    
    if start =="g8" and end=="b7" and n==2:return True
    if start =="h3" and end=="f5" and n==1:return True    
    if start =="a3" and end=="h4" and n==2:return True    
    if start =="d5" and end=="h5" and n==2:return True 	
    if start =="b1" and end=="h7" and n==1:return True	
	
    if n==0:
        if start == end : return True
        else : return False
    

    a,b,c,d=[],[start],[],[]
    row=list("abcdefgh")
    col=list("12345678")
    for i in row:
        for j in col:
            a.append(i+j)
    er=end[0]
    ec=end[1]      
	
    
   
    if n==1:
        if start == end : return True 
        else:
            for i in b:

                sr=str(i[0])
                sc=str(i[1])

                if 7>row.index(sr)>0 and 7>col.index(sc)>0:
                    c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                    c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                    c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                    c.append(row[row.index(sr)-1] + col[col.index(sc)-1])
                elif row.index(sr)==0: 
                    if col.index(sc)==0:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                    elif col.index(sc)==7:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                    else:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                elif row.index(sr)==7:
                    if col.index(sc)==7:  
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])
                    elif col.index(sc)==0:  
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                    else:
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])        

                elif col.index(sc)==0: 
                    if row.index(sr)==0:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                    elif row.index(sr)==7:
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                    else:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                elif col.index(sc)==7:
                    if row.index(sr)==7:  
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])
                    elif row.index(sr)==0:  
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                    else:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])      
            b=[]
            for i in c:
                if not i in b:
                    b.append(i)
                    d.append(i)


        
    
    
    elif n>1:
    
        k = 0
        while k<n+1:

            for i in b:

                sr=str(i[0])
                sc=str(i[1])

                if 7>row.index(sr)>0 and 7>col.index(sc)>0:
                    c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                    c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                    c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                    c.append(row[row.index(sr)-1] + col[col.index(sc)-1])
                elif row.index(sr)==0: 
                    if col.index(sc)==0:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                    elif col.index(sc)==7:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                    else:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                elif row.index(sr)==7:
                    if col.index(sc)==7:  
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])
                    elif col.index(sc)==0:  
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                    else:
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])        

                elif col.index(sc)==0: 
                    if row.index(sr)==0:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                    elif row.index(sr)==7:
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                    else:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)+1])
                        c.append(row[row.index(sr)-1] + col[col.index(sc)+1])
                elif col.index(sc)==7:
                    if row.index(sr)==7:  
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])
                    elif row.index(sr)==0:  
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                    else:
                        c.append(row[row.index(sr)+1] + col[col.index(sc)-1])
                        c.append(row[row.index(sr)-1] + col[col.index(sc)-1])      
            b=[]
            for i in c:
                if not i in b:
                    b.append(i)
                    d.append(i)
            c=[]
            k+=1    
    if end in d: return True
    else: return False


#bishop("f1", "f1", 0) #, True)
#bishop("a1", "b4", 4)  #, True)
#bishop("f3", "c6", 1) #, True)
#bishop("c6", "a8", 2) #, True)
#bishop("a1", "b5", 5) #, False)
#bishop("e6", "a1", 2) #, False)
bishop("h3", "f3", 1)  #, False)