x = 5       # x is an integer
y = 2.0     # y is a float
z = x + y   # z is automatically converted to float
print(z)    # Output: 7.0


x = "5"       # x is a string
y = int(x)    # y is an integer
print(y)      # Output: 5

a = 3.14      # a is a float
b = str(a)    # b is a string
print(b)      # Output: '3.14'


user_input = input("Enter your name: ")
print("Hello, " + user_input)


str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World


s = "Python"
print(len(s))  # Output: 6


s = "cutu"
print(s[0])  # Output: c
print(s[1])  # Output: u
print(s[2])  # Output: t
print(s[3])  # Output: u


print(s[-1])  # Output: u
print(s[-2])  # Output: t
print(s[-3])  # Output: u
print(s[-4])  # Output: c


s = "Python"
print(s[0:3])    # Output: Pyt (ending index is not included)
print(s[2:])     # Output: thon (from index 2 to the end)
print(s[:4])     # Output: Pyth (from start to index 4, not included)


s = "Python"
print(s.endswith("on"))  # Output: True


s = "python"
print(s.capitalize())  # Output: Python


s = "Hello World"
print(s.replace("World", "Python"))  # Output: Hello Python


s = "Hello World"
print(s.find("World"))  # Output: 6


s = "banana"
print(s.count("a"))  # Output: 3
