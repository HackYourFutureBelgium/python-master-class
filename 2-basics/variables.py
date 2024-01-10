# variables_intro.py

# Introduction
"""
In Python, variables are used to store and manage data. They act as symbolic names that reference values.
This script provides a brief overview of creating and deleting variables, along with the concept of constant variables in Python.
"""

# Integer variable
age = 25

# String variable
name = "John Doe"

# Floating-point variable
salary = 50000.0

# Boolean variable
is_student = True

# Deleting Variables
x = 10
print(x)  # Output: 10

# Deleting the variable
del x

# Trying to access x after deletion will result in an error
# print(x)  # Uncommenting this line will result in a NameError

# Constant Variables
# In Python, there is no strict concept of constant variables.
# However, by convention, variables that are not intended to be modified are written in uppercase to indicate that their values should remain constant.
PI = 3.14159
GRAVITY = 9.8


