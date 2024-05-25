x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")


x = 10
y = 5
if x > 0:
    if y > 0:
        print("Both x and y are positive")
    else:
        print("x is positive, but y is not positive")
else:
    print("x is not positive")


ages = [25, 30, 35]
mixed_list = [25, "hello", 3.14]


ages = [25, 30, 35, 40, 45]
print(ages[1:4])  # Output: [30, 35, 40]


ages.append(50)
ages.sort()
ages.sort(reverse=True)
ages.reverse()
ages.insert(2, 33)
ages.remove(30)
ages.pop(1)


coordinates = (10, 20)
single_element_tuple = ("single",)
coordinates.index(20)  # Output: 1
coordinates.count(10)  # Output: 1

