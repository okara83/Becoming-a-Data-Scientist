"""Question:
Define a “function” to calculate permutation of 2 numbers.
Reminder: P(n,r) = n!/(n-r)!
Clue: Defining a function that calculates factorial of given number, may be helpful.
Answer:"""
def factorial(number):
   fact = 1
   for i in range(1,number+1):
       fact *= i
   return fact
def permutation(n,r):
   return int(factorial(n)/factorial(n-r))
n = int(input("To calculate permutation please enter n : "))
r = int(input("To calculate permutation please enter r : "))
print(f"Permutation of ({n},{r}) is {permutation(n,r)}")