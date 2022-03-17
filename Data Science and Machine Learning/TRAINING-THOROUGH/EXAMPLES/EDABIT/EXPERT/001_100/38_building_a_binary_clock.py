"""
Building a Binary Clock
A binary clock displays the time of day in binary format. 
Modern binary clocks have six columns of lights; two for each of the hours, minutes and seconds. 
The photo below shows a binary clock displaying the time "12:15:45":

The binary values increase from the bottom to the top row. 
Lights on the bottom row have a value of 1, lights on the row above have a value of 2, then 4 on the row above that, and finally a value of 8 on the top row. Any 24-hour time can be shown by switching on a certain combination of lights. For example, to show the time "10:37:49":

You've decided to build your own binary clock, and you need to figure out how to light each row of the clock to show the correct time. Given the time as a string, return a list containing strings that shows the lights for each row of the clock (top to bottom). Use "1" for on, and "0" for off. Leave a blank space for any part of the row that doesn't require a light.

Examples
binary_clock("10:37:49") ➞ [
  " 0 0 1",
  " 00110",
  "001100",
  "101101"
]

binary_clock("18:57:31") ➞ [
  " 1 0 0",
  " 01100",
  "000110",
  "101111"
]

binary_clock("10:50:22") ➞ [
  " 0 0 0",
  " 01000",
  "000011",
  "101000"
]
Notes
See the Resources section for more information on binary clocks.
"""
def binary_clock(time):
    
    a = list("".join(time.split(":")))
    b, c = [], []    
    for i in a:
        b.append(bin(int(i))[2:])
    
    b[0]="0"*(2-len(b[0]))+b[0]
    b[1]="0"*(4-len(b[1]))+b[1]
    b[2]="0"*(3-len(b[2]))+b[2]
    b[3]="0"*(4-len(b[3]))+b[3]
    b[4]="0"*(3-len(b[4]))+b[4]
    b[5]="0"*(4-len(b[5]))+b[5]
    c.append(" "+ b[1][0]+ " "+ b[3][0] + " "+ b[5][0])
    c.append(" "+b[1][1]+b[2][0]+b[3][1]+b[4][0]+b[5][1])
    c.append(b[0][0]+b[1][2]+b[2][1]+b[3][2]+b[4][1]+b[5][2])
    c.append(b[0][1]+b[1][3]+b[2][2]+b[3][3]+b[4][2]+b[5][3])

    return c
    
binary_clock("10:37:49")
#binary_clock("07:24:16") #, [' 0 0 0', ' 10101', '011001', '010010'])
#binary_clock("13:48:18") #, [' 0 1 1', ' 01000', '010000', '110010'])
#binary_clock("18:48:15") #, [' 1 1 0', ' 01001', '000000', '100011'])
#binary_clock("11:47:55") #, [' 0 0 0', ' 01111', '000100', '110111'])
#binary_clock("05:46:39") #, [' 0 0 1', ' 11100', '000110', '010011'])
#binary_clock("20:35:19") #, [' 0 0 1', ' 00100', '101000', '001111'])
#binary_clock("10:51:40") #, [' 0 0 0', ' 01010', '000000', '101100'])
#binary_clock("10:16:17") #, [' 0 0 0', ' 00101', '000101', '101011'])
#binary_clock("08:17:26") #, [' 1 0 0', ' 00101', '000111', '001100'])
#binary_clock("17:48:59") #, [' 0 1 1', ' 11010', '010000', '110011'])
#binary_clock("20:04:33") #, [' 0 0 0', ' 00100', '100011', '000011'])
#binary_clock("01:35:39") #, [' 0 0 1', ' 00100', '001010', '011111'])
#binary_clock("13:23:39") #, [' 0 0 1', ' 00000', '011110', '110111'])
#binary_clock("01:56:09") #, [' 0 0 1', ' 01100', '000100', '011001'])
#binary_clock("10:50:22") #, [' 0 0 0', ' 01000', '000011', '101000'])
#binary_clock("07:41:09") #, [' 0 0 1', ' 11000', '010000', '010101'])
#binary_clock("10:20:42") #, [' 0 0 0', ' 00010', '001001', '100000'])
#binary_clock("02:19:30") #, [' 0 1 0', ' 00000', '010010', '001110'])
#binary_clock("13:41:41") #, [' 0 0 0', ' 01010', '010000', '110101'])
#binary_clock("03:17:28") #, [' 0 0 1', ' 00100', '010110', '011100'])

