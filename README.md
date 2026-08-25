# 🐍 Python Basics – Variables & Data Types

This repository contains my beginner Python practice, covering **variables, naming conventions, data types, type conversion, user input, and basic arithmetic operations**.

## 📚 Topics Covered

* Variables
* Camel Case & Snake Case
* Data Types
* `int`
* `float`
* `str`
* `bool`
* User Input
* Type Conversion
* Basic Arithmetic
* Formatted Strings (`f-strings`)

## 💻 Code Examples

```python
num = 5

#print(num)

# (Camel & Snake) Case

frist_name = "Nader"  # snake_case

fristName = "Nader"  # camelCase

#print(frist_name)

#print(fristName)


# Data Types

#print(type(5))

#print(type(5.6))

#print(type("Nader"))

#print(type(True))


# User Input & Age Calculation

# BirthYear = int(input("Enter your birth year :"))

# age = 2026 - BirthYear

# print(f"Your age is {age} years old")


# Type Conversion

#print(int("123"))

#print(int(1.7))

#print(int(True))

#print(float("123"))

#print(float(4))

#print(float(True))

#print(bool("123"))

#print(bool(4))

#print(bool(""))

#print(bool("0"))


# Simple Calculator

# num1 = float(input("Enter num 1 :"))

# num2 = float(input("Enter num 2 :"))

# sum_res = num1 + num2

# print(f"sum = {sum_res}")
```

## 🧠 What I Learned

### Variables

Variables are used to store data in Python.

```python
num = 5
name = "Nader"
```

### Naming Conventions

Python commonly uses **snake_case**:

```python
first_name = "Nader"
```

Camel case can also be written as:

```python
firstName = "Nader"
```

> Note: The correct spelling is `first_name`, not `frist_name`.

### Data Types

Python has several built-in data types:

```python
int      # Integer
float    # Decimal number
str      # String
bool     # Boolean
```

Examples:

```python
5          # int
5.6        # float
"Nader"    # str
True       # bool
```

You can check the type of a value using:

```python
type()
```

Example:

```python
print(type(5))
```

### Type Conversion

Python allows converting values between different data types.

```python
int("123")
float("123")
bool("123")
```

Examples:

```python
print(int("123"))
print(float("123"))
print(bool("123"))
```

### User Input

The `input()` function allows the user to enter data.

```python
name = input("Enter your name: ")
```

Since `input()` returns a string, we can convert the input when necessary:

```python
BirthYear = int(input("Enter your birth year: "))
```

### f-Strings

f-strings make it easy to insert variables into strings.

```python
age = 20

print(f"Your age is {age} years old")
```

### Basic Arithmetic

We can perform calculations using variables:

```python
num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))

sum_res = num1 + num2

print(f"sum = {sum_res}")
```

## 🚀 Goal

The goal of this repository is to document my progress while learning **Python fundamentals** step by step.

More Python topics and exercises will be added as I continue learning.

---

⭐ **Learning Python one step at a time.**
