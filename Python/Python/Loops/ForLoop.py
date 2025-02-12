# For loop..example 1 -- Python program to show how the for loop works

# Creating a sequence which is a tuple of numbers
numbers = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]
square = 0
squares = []

# Creating a for loop
for value in numbers:
    square = value ** 2
    squares.append(square)
print("The list of squares is", squares)

# Using else Statement with for Loop..example 2 -- Python program to show how if-else statements work

string = "Python Loop"
for s in string:
    if s == "o":
        print("If block")
    else:
        print(s)

# Using else with for loop..example 3 -- Python program to show how to use else statement with for loop
tuple_ = (3, 4, 6, 8, 9, 2, 3, 8, 9, 7)
for value in tuple_:
    if value % 2 != 0:
        print(value)
else:
    print("These are the odd numbers present in the tuple")

# The range() Function..example 4 -- Python program to show the working of range() function

print(range(15))
print(list(range(15)))
print(list(range(4, 9)))
print(list(range(5, 25, 4)))

# Iterating over a sequence with the help of indexing..example 5 -- Python program to iterate over a sequence with the help of indexing

tuple_ = ("Python", "Loops", "Sequence", "Condition", "Range")
# Iterating over tuple_ using range() function
for iterator in range(len(tuple_)):
    print(tuple_[iterator].upper())
