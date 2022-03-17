"""
The Resistor Colors
A resistor is a common electrical component found in every electronic circuit. Usually a resistor has a color-based code (as painted bands over it) to decipher through a table.

Color	Digits	Magnitude	Tolerance	T.C.R.
Black	0	0	-	-
Brown	1	1	+/-1%	100ppm/k
Red	2	2	+/-2%	50ppm/k
Orange	3	3	-	15ppm/k
Yellow	4	4	-	25ppm/k
Green	5	5	+/-0.5%	-
Blue	6	6	+/-0.25%	10ppm/k
Violet	7	7	+/-0.1%	5ppm/k
Gray	8	8	+/-0.05%	-
White	9	9	-	-
Gold	-	-1	+/-5%	-
Silver	-	-2	+/-10%	-
Starting from the left assign a number to each coloured band:

4 bands resistor:
1st and 2nd color: digits from column 1.
3rd color: 10 elevated to the digit of column 2.
4th color: tolerance from column 3.
5 bands resistor:
1st, 2nd and 3rd color: digits from column 1.
4th color: 10 elevated to the digit of column 2.
5th color: tolerance from column 3.
6 bands resistor:
From 1st to 5th: as above.
6th color: coefficient from column 4.
Then, when numbers have replaced colors:

Resistance is equal to the number resulting by the union of digits from column 1 multiplied for the magnitude calculated from column 2: is measured in Ohms (symbol: Ω). When Ohms are in the thousands order the notation is kΩ (kiloOhms), in the millions order the notation is MΩ (MegaOhms), in the billions order the notation is GΩ (GigaOhms).
Tolerance and TCR (temperature coefficient of resistance, only for 6-banded resistors) are the results of columns 3 and 4.
Given a list of colors you must return the resistor resistance, tolerance and (eventually) the TCR as a string (with identifiers separated by spaces between them).

Examples
resistor_code(["red", "yellow", "blue", "green"]) ➞ "24MOhm +/-0.5%"
# red + yellow = 24; blue = 10^6, green = +/-0.5%
# resistance * magnitude = 24000000 (24M)

resistor_code(["white", "black", "white", "blue", "gold"]) ➞ "909MOhm+/-5%"
# white + black + white = 909

resistor_code(["black", "white", "black", "orange", "red", "yellow"]) ➞ "90kOhm +/-2% 25ppm/k"
# black + white + black = 090 = 90; orange = 10^3
# resistance * magnitude = 90000 (90k)
Notes
For more info about resistors and their color codes check the Resources tab.
All given lists are valid, no exceptions to handle.
"""
def resistor_code(colors):
    d = {
    "black" : [0,0,"",""],
    "brown":[1,1,"+/-1%","100ppm/k"],
    "red":[2,2,"+/-2%","50ppm/k"],
    "orange":[3,3,"","15ppm/k"],
    "yellow":[4,4,"","25ppm/k"],
    "green":[5,5,"+/-0.5%",""],
    "blue":[6,6,"+/-0.25%","10ppm/k"],
    "violet":[7,7,"+/-0.1%","5ppm/k"],
    "gray":[8,8,"+/-0.05%",""],
    "white":[9,9,"",""],
    "gold":["",-1,"+/-5%",""],
    "silver":["",-2,"+/-10%",""]  
    }
    
    if len(colors) == 4:
        r4 = int(str(d[colors[0]][0]) + str(d[colors[1]][0]))    
        m4 = 10 ** (int(d[colors[2]][1]))
        rm4 = r4 * m4
        if rm4 % 10**9 == 0:
            rm44 = rm4 // (10**9)
            p = "G"
        elif rm4 % 10**6 == 0:
            rm44 = rm4 // (10**6)
            p = "M"
        elif rm4 > 1000:
            rm44 = rm4 / (10**3)
            p = "k"
        else:
            rm44 = rm4
            p = "OM"
        return (str(rm44) + p + "Ohm" + " " +d[colors[3]][2])
            
    if len(colors) == 5:
        r5 = int(str(d[colors[0]][0]) + str(d[colors[1]][0]) + str(d[colors[2]][0]))           
        m5 = 10 ** (int((d[colors[3]][1])))    
        rm5 = r5 * m5
        if rm5 % 10**9 == 0:
            rm55 = rm5 // (10**9)
            p = "G"
        elif rm5 % 10**6 == 0:
            rm55 = rm5 // (10**6)
            p = "M"
        elif rm5 >  1000:
            rm55 = rm5 // (10**3)
            p = "k"
        else:
            rm55 = rm5
            p = ""
        return (str(rm55) + p + "Ohm" + " " +d[colors[4]][2])            
    
    if len(colors) == 6:
        r6 = int(str(d[colors[0]][0]) + str(d[colors[1]][0]) + str(d[colors[2]][0]))         
        m6 = 10 ** (int(d[colors[3]][1]))
        rm6 = r6 * m6
        if rm6 % 10**9 == 0:
            rm66 = rm6 // (10**9)
            p = "G"
        elif rm6 % 10**6 == 0:
            rm66 = rm6 // (10**6)
            p = "M"
        elif rm6 >  1000:
            rm66 = rm6 // (10**3)
            p = "k"
        else:
            rm66 = rm6
            p = ""
        return (str(rm66) + p + "Ohm" + " " + d[colors[4]][2] + " " + d[colors[5]][3])    
    
#resistor_code(["black", "blue", "black", "brown"])   #, "6OMOhm +/-1%")    
#resistor_code(["orange", "yellow", "white", "gold", "gray"])   #, "34.9Ohm +/-0.05%")    
#resistor_code(["yellow", "brown", "green", "black", "green", "orange"])  #, "415Ohm +/-0.5% 15ppm/k")
resistor_code(["brown", "violet", "red", "silver"])  #, "1.7kOhm +/-10%")
#resistor_code(["red", "yellow", "blue", "green"]) #➞ "24MOhm +/-0.5%"
# red + yellow = 24; blue = 10^6, green = +/-0.5%
# resistance * magnitude = 24000000 (24M)

#resistor_code(["white", "black", "white", "blue", "gold"]) #➞ "909MOhm+/-5%"
# white + black + white = 909

#resistor_code(["black", "white", "black", "orange", "red", "yellow"]) #➞ "90kOhm +/-2% 25ppm/k"
# black + white + black = 090 = 90; orange = 10^3
# resistance * magnitude = 90000 (90k)    