# Read a number and perform operations based on whether it's even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"The square of {number} is {number**2}")
else:
    print(f"The cube of {number} is {number**3}")
