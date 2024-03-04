#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HK
#
# Created:     04-03-2024
# Copyright:   (c) HK 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


age=input("Enter your age:" )

if int(age) >= 18:
    print("You are adult.")
elif int(age)<18 and int(age)>12:
    print("You are in School.")
else:
    print("You are child")