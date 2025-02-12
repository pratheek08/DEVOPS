# Using for loop
def reverse_string_for_loop(string): 
    str1 = ""  # Declaring empty string to store the reversed string 
    for i in string: 
        str1 = i + str1  # Adding characters in reverse order
    return str1 

string = "JavaTpoint"  # Given String 
print("The original string is:", string) 
print("The reversed string using for loop is:", reverse_string_for_loop(string))

# Using while loop
def reverse_string_while_loop(string):
    reverse_string = ""  # Empty String 
    count = len(string)  # Find length of a string
    while count > 0: 
        reverse_string += string[count - 1]  # Append last character to new string
        count = count - 1  # Decrement index 
    return reverse_string

print("The reversed string using while loop is:", reverse_string_while_loop(string))

# Using slice operator
def reverse_string_slice(string):
    return string[::-1]  # Slicing with -1 step to reverse the string

print("The reversed string using slice operator is:", reverse_string_slice(string))

# Using reversed() function
def reverse_string_reversed(string):
    return "".join(reversed(string))  # Using reversed() and join()

print("The reversed string using reversed() function is:", reverse_string_reversed(string))

# Using recursion
def reverse_string_recursion(string):
    if len(string) == 0:  # Base case: if empty string, return itself
        return string
    else:
        return reverse_string_recursion(string[1:]) + string[0]  # Recursive call
string2 = "Devansh Sharma"
print("The original string is:", string2)
print("The reversed string using recursion is:", reverse_string_recursion(string2))