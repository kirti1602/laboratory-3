# Read three numbers and find the smallest among them
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Using if-else to find the smallest number
if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print(f"The smallest number among {num1}, {num2}, and {num3} is {smallest}")
