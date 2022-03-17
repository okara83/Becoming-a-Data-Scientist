# File permuteabcd.py
# The first letter varies from A to D
for first in 'ABCD':
    for second in 'ABCD': # The second varies from A to D
        if second != first: # Don't duplicate letters
            for third in 'ABCD': # The third varies from A to D
                if third != first and third != second: # Don't duplicate letters
                    for forth in 'ABCD': # The forth varies from A to D
                        if forth != first and forth != second and forth != third:# Don't duplicate first or second letter
                            print(first + second + third + forth)