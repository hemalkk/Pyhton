#-------------------------------------------------------------------------------
# Name:        Simple Calculator
# Purpose:
#
# Author:      HK
#
# Created:     04-03-2024
# Copyright:   (c) HK 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

firstNumber=int(input("Enter your first number: "))
operator=input("Enter your operator (+,-,*,/,%): ")
secondNumber=int(input("Enter your second number: "))


if operator=='+':
    print(firstNumber + secondNumber)
elif operator=='-':
    print(firstNumber - secondNumber)
elif operator=='*':
    print(firstNumber * secondNumber)
elif operator=='/':
    print(firstNumber / secondNumber)
elif operator=='%':
    print(firstNumber % secondNumber)
else:
    print("Invalid")