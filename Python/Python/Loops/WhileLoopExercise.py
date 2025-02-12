# Prime Numbers and Python While Loop..example 1
# Python program to verify if the given integer is a prime number

num = [34, 12, 54, 23, 75, 34, 11]

def prime_number(number):
    condition = 0
    iteration = 2
    while iteration <= number / 2:
        if number % iteration == 0:
            condition = 1
            break
        iteration = iteration + 1
    
    if condition == 0:
        print(f"{number} is a PRIME number")
    else:
        print(f"{number} is not a PRIME number")

for i in num:
    prime_number(i)

# Armstrong and Python While Loop..example 2
# Python program to verify whether the given integer is an Armstrong number

n = int(input())
n1 = str(n)
l = len(n1)
temp = n
s = 0

while n != 0:
    r = n % 10
    s = s + (r ** l)
    n = n // 10

if s == temp:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")

# Multiplication Table using While Loop..example 3
# Python program to print the multiplication table of a given number

num = 21
counter = 1
print("The Multiplication Table of:", num)

while counter <= 10:
    ans = num * counter
    print(num, 'x', counter, '=', ans)
    counter += 1

# Python While Loop with List..example 4
# Python program to square every number of a list

list_ = [3, 5, 1, 4, 6]
squares = []

while list_:
    squares.append((list_.pop()) ** 2)

print(squares)

# Determine odd and even numbers from a list..example 5
list_ = [3, 4, 8, 10, 34, 45, 67, 80]
index = 0

while index < len(list_):
    element = list_[index]
    if element % 2 == 0:
        print('It is an even number')
    else:
        print('It is an odd number')
    index += 1

# Determine the number of letters in every word from the given list..example 6
List_ = ['Priya', 'Neha', 'Cow', 'To']
index = 0

while index < len(List_):
    element = List_[index]
    print(len(element))
    index += 1

# Python While Loop Multiple Conditions..example 7
# Using multiple conditions in a while loop

num1 = 17
num2 = -12

while num1 > 5 and num2 < -5:
    num1 -= 2
    num2 += 3
    print((num1, num2))

# Another example with OR condition..example 8
num1 = 17
num2 = -12

while num1 > 5 or num2 < -5:
    num1 -= 2
    num2 += 3
    print((num1, num2))

# Grouping multiple logical expressions in a while loop..example 9
num1 = 9
num2 = 14
maximum_value = 4
counter = 0

while (counter < num1 or counter < num2) and not counter >= maximum_value:
    print(f"Number of iterations: {counter}")
    counter += 1
