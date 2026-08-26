# Variables
num = 5
print(num)


# Naming conventions
first_name = "Nader"  # Snake Case
firstName = "Nader"   # Camel Case

print(first_name)
print(firstName)


# Data types
print(type(5))        # Integer
print(type(5.6))      # Float
print(type("Nader"))  # String
print(type(True))     # Boolean


# Calculate age
birth_year = int(input("Enter your birth year: "))
age = 2026 - birth_year
print(f"Your age is {age} years old.")


# Convert values to Integer
print(int("123"))  # String to Integer
print(int(1.7))    # Float to Integer
print(int(True))   # Boolean to Integer


# Convert values to Float
print(float("123"))  # String to Float
print(float(4))      # Integer to Float
print(float(True))   # Boolean to Float


# Convert values to Boolean
print(bool("123"))  # String to Boolean
print(bool(4))      # Integer to Boolean
print(bool(""))     # Empty String -> False


# Simple calculator
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

sum_result = num1 + num2

print(f"Sum = {sum_result}")
