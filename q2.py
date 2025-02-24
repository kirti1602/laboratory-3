# Swap two numbers without using a third variable
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Using arithmetic operations
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
