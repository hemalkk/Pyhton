# This is a single-line comment

"""
This is a multi-line comment.
It can span multiple lines.
"""

name = input("Enter your name: ")

age = int(input("Enter your age: "))

height = float(input("Enter your height in meters: "))

if condition1:
    # Execute this block if condition1 is true
elif condition2:
    # Execute this block if condition2 is true
else:
    # Execute this block if none of the above conditions are true

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

result = value_if_true if condition else value_if_false

is_adult = True if age >= 18 else False


print("Adult") if age >= 18 else print("Minor")

is_adult = ("Minor", "Adult")[age >= 18]
