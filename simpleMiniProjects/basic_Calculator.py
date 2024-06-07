# Basic Calculator
print(".......Basic Calculator.......")

# Prompt the user to enter the first number
number1 = float(input("Enter your first number: "))

# Prompt the user to enter the second number
number2 = float(input("Enter your second number: "))

# Display the operation choices to the user
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

# Prompt the user to enter their choice of operation
choice = int(input("Enter your choice from 1-4: "))

# Perform the chosen operation and display the result
if choice == 1:
    print("The Answer is:", number1 + number2)
elif choice == 2:
    print("The Answer is:", number1 - number2)
elif choice == 3:
    print("The Answer is:", number1 * number2)
elif choice == 4:
    print("The Answer is:", number1 / number2)
else:
    print("Invalid input")
