#addition of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

#area of rectangle

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area =", l * b)

#swap two numbers

a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swap:", a, b)

# Input year
year = int(input("Enter a year: "))

# Check leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.") 

# Program to calculate grade based on marks

marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Program to check vowel or consonant

ch = input("Enter a letter: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a single alphabet.")
elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print(ch, "is a Vowel.")
else:
    print(ch, "is a Consonant.")

# Print numbers from 1 to 100

i = 1

while i <= 100:
    print(i)
    i += 1

# Program to reverse a number

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)

# Program to reverse a string

text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)

# Program to find the largest element in a list

numbers = [10, 25, 8, 45, 32]

largest = max(numbers)

print("Largest element:", largest)

# Program to check if a number is prime

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime Number.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(num, "is not a Prime Number.")
            break
    else:
        print(num, "is a Prime Number.")

# Merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1 | dict2

print("Merged Dictionary:", merged)

# Create and write data into a text file

with open("sample.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to Python.\n")
    file.write("This is a text file.")

print("Data written successfully.")

# Program to handle division by zero

try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))

    result = num / den
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")





