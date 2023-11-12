# Operators and Expressions in Python

# 1. Arithmetic Operators
x = 10
y = 5

addition = x + y  # Addition (+)
subtraction = x - y  # Subtraction (-)
multiplication = x * y  # Multiplication (*)
division = x / y  # Division (/)
modulus = x % y  # Modulus (%)
exponentiation = x ** y  # Exponentiation (**)
floor_division = x // y  # Floor Division (//)

print("Arithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
print("Floor Division:", floor_division)

# 2. Comparison Operators
is_equal = x == y  # Equal to (==)
is_not_equal = x != y  # Not Equal to (!=)
is_greater = x > y  # Greater than (>)
is_less = x < y  # Less than (<)
is_greater_equal = x >= y  # Greater than or Equal to (>=)
is_less_equal = x <= y  # Less than or Equal to (<=)

print("\nComparison Operators:")
print("Is Equal:", is_equal)
print("Is Not Equal:", is_not_equal)
print("Is Greater:", is_greater)
print("Is Less:", is_less)
print("Is Greater or Equal:", is_greater_equal)
print("Is Less or Equal:", is_less_equal)

# 3. Logical Operators
is_true = True
is_false = False

logical_and = is_true and is_false  # Logical AND (and)
logical_or = is_true or is_false  # Logical OR (or)
logical_not = not is_true  # Logical NOT (not)

print("\nLogical Operators:")
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical NOT:", logical_not)

# 4. Assignment Operators
a = 10
a += 5  # Equivalent to: a = a + 5
a -= 2  # Equivalent to: a = a - 2
a *= 3  # Equivalent to: a = a * 3
a /= 4  # Equivalent to: a = a / 4
a %= 3  # Equivalent to: a = a % 3
a **= 2  # Equivalent to: a = a ** 2
a //= 2  # Equivalent to: a = a // 2

print("\nAssignment Operators:")
print("Value of a after assignments:", a)

# 5. Bitwise Operators
p = 5  # Binary: 0101
q = 3  # Binary: 0011

bitwise_and = p & q  # Bitwise AND (&)
bitwise_or = p | q  # Bitwise OR (|)
bitwise_xor = p ^ q  # Bitwise XOR (^)
bitwise_not_p = ~p  # Bitwise NOT (~)
left_shift = p << 2  # Left Shift (<<)
right_shift = p >> 1  # Right Shift (>>)


print("\nBitwise Operators:")
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)
print("Bitwise NOT (p):", bitwise_not_p)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)

# 6. Identity Operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("\nIdentity Operators:")
print("Is list1 the same as list2?", is_list1_same_as_list2)
print("Is list1 the same as list3?", is_list1_same_as_list3)

is_list1_same_as_list2 = list1 is list2  # Identity operator "is"
is_list1_same_as_list3 = list1 is list3

# 7. Membership Operators
fruits = ["apple", "banana", "cherry"]

is_apple_in_fruits = "apple" in fruits  # Membership operator "in"
is_mango_not_in_fruits = "mango" not in fruits  # Membership operator "not in"


print("\nMembership Operators:")
print("Is 'apple' in fruits?", is_apple_in_fruits)
print("Is 'mango' not in fruits?", is_mango_not_in_fruits)

# Expressions
expression1 = (x + y) * (x - y)
expression2 = x ** 2 - y ** 2

print("\nExpressions:")
print("Expression 1:", expression1)
print("Expression 2:", expression2)













