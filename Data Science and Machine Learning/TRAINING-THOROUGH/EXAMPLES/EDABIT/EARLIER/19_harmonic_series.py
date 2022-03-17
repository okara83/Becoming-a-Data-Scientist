"""
Harmonic Series
In mathematics, the harmonic series is the divergent infinite series:

Alternative Text

Its name derives from the concept of overtones, or harmonics in music.

Create a function that, given a precision parameter, returns the value of the harmonic series.

Examples
harmonic(3) ➞ 1.833

harmonic(1) ➞ 1.0

harmonic(5) ➞ 2.283
Notes
Round the result to the third decimal place.
"""
def harmonic(n):
    
    if n == 0:
        return 0
    else:      
        result = 0
        for i in range(1,n+1):
            result = result + (1/i)
    
        return round(result,3)




#harmonic(10) #, 2.929)
#harmonic(1)  #, 1)
harmonic(12345)  #, 9.998)
#harmonic(0)    #, 0)
#harmonic(5000)   #, 9.095)
#harmonic(2)   #, 1.5)