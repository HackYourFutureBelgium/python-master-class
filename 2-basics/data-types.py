"""
Data types in Python

1. Numeric data type: int, float, complex
"""
age = 25  # Integer
height = 1.80  # Float
num = 10 + 3j  # Complex number (consists of real and imaginary parts)

"""
2. String data type
"""
name = "John"  # String

"""
3. Sequence data type: list, tuple, range (ordered collections indexed starting with 0)
   You can use + for concatenation and * for repetition
"""
message = "Hello world"  # String
second_char = message[1]  # Accessing the second character 'e'
hello = message[0:5]  # Slicing the string from index 0 to 4 ('Hello')

colors = ["red", "blue", "green"]  # List (mutable, can be changed)
print(colors[1:])  # Output: ['blue', 'green']

user_types = ("admin", "user")  # Tuple (immutable, read-only)
admin = user_types[0]
print(admin)  # Output: admin

# Range (ordered collection)
for num in range(5):
    print(num)  # Output: 0, 1, 2, 3, 4

"""
4. Binary data type: bytes, bytearray, memoryview
"""
binary_data = b"hello"  # Bytes
mutable_binary_data = bytearray(b"hello")  # Bytearray (mutable)
memory_view = memoryview(b"hello")  # Memoryview

"""
5. Mapping data type: dict (key-value pairs)
"""
person = {"name": "John", "age": 30, "city": "Brussels"}

"""
6. Boolean data type: True or False
"""
is_male = True
is_hot = False

"""
7. Set data type: set, frozenset
"""
fruits = {"apple", "banana", "orange"}  # Set (mutable)
frozen_fruits = frozenset({"apple", "banana", "orange"})  # Frozenset (immutable)

"""
8. None data type: NoneType
"""
result = None

"""
Displaying information
"""
print(f"Age: {age}, Height: {height}, Complex Number: {num}")
print(f"Name: {name}")
print(f"Second Character: {second_char}, Substring: {hello}")
print(f"Colors: {colors}, User Types: {user_types}")
print(
    f"Binary Data: {binary_data}, Mutable Binary: {mutable_binary_data}, Memory View: {memory_view}"
)
print(f"Person Info: {person}")
print(f"Boolean Values: Male - {is_male}, Hot - {is_hot}")
print(f"Fruits: {fruits}, Frozen Fruits: {frozen_fruits}")
print(f"Result: {result}")
