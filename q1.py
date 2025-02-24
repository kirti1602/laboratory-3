# Swap two numbers using a third variable
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Using third variable
temp = a
a = b
b = temp

print(f"After swapping: a = {a}, b = {b}")
