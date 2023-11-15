# Control Flow 

## 1. if-else Statements

x = 10

if x > 0:
    print("Positive number")
else:
    print("Non-positive number")

## 2. while Loop

count = 0

while count < 5:
    print(f"Count: {count}")
    count += 1

## 3. for Loop

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"Current fruit: {fruit}")

## 4. Nested Control Flow

grade = 75

if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade < 80:
    print("C")
else:
    print("Fail")

## 5. Break and Continue

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num % 2 == 0:
        print("Encountered an even number. Stopping.")
        break
    print(f"Odd number: {num}")


