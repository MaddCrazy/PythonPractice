#Hypotenuse Calculator
#imports only the sqrt(square root) function from the math library
from math import sqrt
print ("Welcome to the hypotenuse calculator!")
sideA = float(input("Please enter the length of side 'a': "))
sideB = float(input("Please enter the length of side 'b': "))
c = sqrt(sideA ** 2 + sideB ** 2)
print("Thank you! The length of the Hypotenuse is", str(c))