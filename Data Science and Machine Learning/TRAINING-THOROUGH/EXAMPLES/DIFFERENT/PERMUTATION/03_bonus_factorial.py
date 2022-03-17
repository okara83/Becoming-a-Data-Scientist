number = int(input("Enter a number to calculate factoriyel : "))

def factorial(number):
   fact = 1
   for i in range(1,number+1):
       fact *= i
   return fact

print(number, " factorial is  ",factorial(number))