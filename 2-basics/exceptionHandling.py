# Error Handling in Python

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as zde:
        print(f"Error: {zde} - Cannot divide by zero.")
    except TypeError as te:
        print(f"Error: {te} - Please provide valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("This block always executes, regardless of whether an exception was raised or not.")

# Example 1: Division with valid numbers
result1 = divide_numbers(10, 2)
print(f"Result 1: {result1}")

# Example 2: Division by zero
result2 = divide_numbers(5, 0)

# Example 3: Invalid input type
result3 = divide_numbers(10, '2')

# Example 4: Using try-except-else block
def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at path '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("File read successfully.")
        return content

# Example 5: Reading a valid file
file_content = open_file('sample.txt')
print(f"File Content: {file_content}")

# Example 6: Reading a non-existent file
file_content2 = open_file('nonexistent.txt')

# Example 7: Handling multiple exceptions in one block
def process_data(data):
    try:
        result = data['key'] * 2
        print(f"Processed result: {result}")
    except (KeyError, TypeError) as e:
        print(f"Error: {e} - Invalid data format.")

# Example 8: Processing valid data
data1 = {'key': 5}
process_data(data1)

# Example 9: Processing invalid data
data2 = {'wrong_key': 10}
process_data(data2)
