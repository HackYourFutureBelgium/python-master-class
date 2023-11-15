# Functions and Modules 

# 1. Functions
# A function is a block of  reusable code that is used to perform a specific task. 

# Function definition
def greet(name):
    print(f"Hello, {name}!")

# Function call
greet("John")

# 2. Modules
# each file considered a module, modules helps to organize code into different files

# import the module
import myModule 

# Using functions from the module
result_add = myModule.add(5, 3)
result_subtract = myModule.subtract(8, 4)

# Printing the results
print(f"Addition Result: {result_add}")
print(f"Subtraction Result: {result_subtract}")