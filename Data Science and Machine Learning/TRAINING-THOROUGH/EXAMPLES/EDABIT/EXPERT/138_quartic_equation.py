"""
https://edabit.com/challenge/xRM8yTQRL3W6Wtdfi      EXPERT 

Quartic Equation
Create a function that returns the number of (real) solutions of ax^4+bx^2+c=0. The function will take three arguments: a as the coefficient of x^4, b as the coefficient of x^2, and c as the constant term.

Examples
quartic_equation(1, -5, 4) ➞ 4

quartic_equation(4, 3, -1) ➞ 2

quartic_equation(1, 10, 9) ➞ 0
Notes
Hint: Try substitution t=x^2.
"""
def quartic_equation(a, b, c):
	if a==0:
		if b==0: return float('Inf') if c==0 else 0
		if c>0: return 0
		return 1 if c==0 else 2
	
	delt=(b/(2*a))**2-c/a
	if delt<0: return 0
	return sum ([1 if x==0 else 2 for x in (-b/(2*a)+delt**0.5,-b/(2*a)-delt**0.5 ) if x>=0])


quartic_equation(1, -5, 4) #➞ 4
#quartic_equation(4, 3, -1) #➞ 2
#quartic_equation(1, 10, 9) #➞ 0