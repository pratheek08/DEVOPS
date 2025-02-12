# If statement..example 1
num = int(input("Enter the number: "))  # Taking input dynamically
if num % 2 == 0:  # Checking if the number is even
    print("The Given number is an even number")

# If statement..example 2 -- Program to print the largest of the three numbers
a = int(input("Enter a: "))  # Taking first number as input
b = int(input("Enter b: "))  # Taking second number as input
c = int(input("Enter c: "))  # Taking third number as input

if a > b and a > c:  # Checking if 'a' is the largest
    print("From the above three numbers given a is largest")
elif b > a and b > c:  # Checking if 'b' is the largest
    print("From the above three numbers given b is largest")
elif c > a and c > b:  # Checking if 'c' is the largest
    print("From the above three numbers given c is largest")

# If-else statement..example 1 -- Program to check whether a person is eligible to vote or not
age = int(input("Enter your age: "))  # Taking age as input
if age >= 18:  # Checking voting eligibility
    print("You are eligible to vote!!")
else:
    print("Sorry! You have to wait!!")

# If-else statement..example 2
# Program to check whether a number is even or odd
num = int(input("Enter the number: "))  # Taking input dynamically
if num % 2 == 0:  # Checking if the number is even
    print("The Given number is an even number")
else:
    print("The Given number is an odd number")

# Elif statement..example 1
# Program to check number equality with specific values
number = int(input("Enter the number? "))  # Taking input dynamically
if number == 10:  # Checking if the number is 10
    print("The given number is equal to 10")
elif number == 50:  # Checking if the number is 50
    print("The given number is equal to 50")
elif number == 100:  # Checking if the number is 100
    print("The given number is equal to 100")
else:
    print("The given number is not equal to 10, 50 or 100")

# Elif statement..example 2
# Program to check grading system based on marks
marks = int(input("Enter the marks? "))  # Taking marks as input
if marks > 85 and marks <= 100:  # Checking grade A
    print("Congrats! You scored grade A ...")
elif marks > 60 and marks <= 85:  # Checking grade B+
    print("You scored grade B+ ...")
elif marks > 40 and marks <= 60:  # Checking grade B
    print("You scored grade B ...")
elif marks > 30 and marks <= 40:  # Checking grade C
    print("You scored grade C ...")
else:
    print("Sorry, you failed!")