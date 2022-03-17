def tournament_scores(lst)
           
    countA = 0
    countB = 0
    countC = 0
    countD = 0
 
    goalA = 0
    goalB = 0
    goalC = 0
    goalD = 0

    concededgoalA = 0
    concededgoalB = 0
    concededgoalC = 0
    concededgoalD = 0   
    
    for i in lst

        if i.split()[1]  i.split()[3]
            
            if i.split()[4] == A
                countA +=3
                goalA = goalA + int(i.split()[3])
                concededgoalA = concededgoalA + int(i.split()[1])
            elif i.split()[4] == B 
                countB +=3
                goalB = goalB + int(i.split()[3])
                concededgoalB = concededgoalB + int(i.split()[1])
            elif i.split()[4] == C
                countC +=3
                goalC = goalC + int(i.split()[3])
                concededgoalC = concededgoalC + int(i.split()[1])
            elif i.split()[4] == D
                countD +=3
                goalD = goalD + int(i.split()[3])
                concededgoalD = concededgoalD + int(i.split()[1])

            if i.split()[0] == A
                goalA = goalA + int(i.split()[1])
                concededgoalA = concededgoalA + int(i.split()[3])
            elif i.split()[0] == B
                goalB = goalB + int(i.split()[1])
                concededgoalB = concededgoalB + int(i.split()[3])
            elif i.split()[0] == C
                goalC = goalC + int(i.split()[1])
                concededgoalC = concededgoalC + int(i.split()[3])
            elif i.split()[0] == D
                goalD = goalD + int(i.split()[1]) 
                concededgoalD = concededgoalD + int(i.split()[3])                
           
        elif i.split()[1]  i.split()[3]
            if i.split()[0] == A
                countA +=3
                goalA = goalA + int(i.split()[1])
                concededgoalA = concededgoalA + int(i.split()[3])
            elif i.split()[0] == B
                countB +=3
                goalB = goalB + int(i.split()[1])
                concededgoalB = concededgoalB + int(i.split()[3])
            elif i.split()[0] == C
                countC +=3
                goalC = goalC + int(i.split()[1])
                concededgoalC = concededgoalC + int(i.split()[3])
            elif i.split()[0] == D
                countD +=3 
                goalD = goalD + int(i.split()[1])
                concededgoalD = concededgoalD + int(i.split()[3])
            if i.split()[4] == A
                goalA = goalA + int(i.split()[3])
                concededgoalA = concededgoalA + int(i.split()[1])
            elif i.split()[4] == B 
                goalB = goalB + int(i.split()[3])
                concededgoalB = concededgoalB + int(i.split()[1])
            elif i.split()[4] == C
                goalC = goalC + int(i.split()[3])
                concededgoalC = concededgoalC + int(i.split()[1])
            elif i.split()[4] == D
                goalD = goalD + int(i.split()[3]) 
                concededgoalD = concededgoalD + int(i.split()[1]) 
           
        else 
            if i.split()[0] == A
                countA +=1
                goalA = goalA + int(i.split()[1])
                concededgoalA = concededgoalA + int(i.split()[3])
            elif i.split()[0] == B
                countB +=1
                goalB = goalB + int(i.split()[1])
                concededgoalB = concededgoalB + int(i.split()[3])
            elif i.split()[0] == C
                countC +=1
                goalC = goalC + int(i.split()[1])
                concededgoalC = concededgoalC + int(i.split()[3])
            elif i.split()[0] == D
                countD +=1
                goalD = goalD + int(i.split()[1]) 
                concededgoalD = concededgoalD + int(i.split()[3])

            if i.split()[4] == A
                countA +=1
                goalA = goalA + int(i.split()[3]) 
                concededgoalA = concededgoalA + int(i.split()[1])
            elif i.split()[4] == B
                countB +=1
                goalB = goalB + int(i.split()[3]) 
                concededgoalB = concededgoalB + int(i.split()[1])
            elif i.split()[4] == C
                countC +=1
                goalC = goalC + int(i.split()[3])
                concededgoalC = concededgoalC + int(i.split()[1])
            elif i.split()[4] == D
                countD +=1                
                goalD = goalD + int(i.split()[3])
                concededgoalD = concededgoalD + int(i.split()[1])
    
    minusA = goalA - concededgoalA
    minusB = goalB - concededgoalB
    minusC = goalC - concededgoalC
    minusD = goalD - concededgoalD
  
    a1 = [A, countA, goalA, minusA]
    a2 = [B, countB, goalB, minusB]
    a3 = [C, countC, goalC, minusC]
    a4 = [D, countD, goalD, minusD]
    
    result = [a1, a2, a3, a4]
    sorted_result = sorted(result, key=lambda R (R[1], R[2], R[3]), reverse = True)
    
    print(sorted_result)
    return sorted_result

