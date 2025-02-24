# Read three numbers and check if any two are equal
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 == num2:
    print(f"{num1} is equal to {num2}")
elif num1 == num3:
    print(f"{num1} is equal to {num3}")
elif num2 == num3:
    print(f"{num2} is equal to {num3}")
else:
    print("No two numbers are equal.")
