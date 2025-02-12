# While loop..example 1
# Python program to show how to use a while loop

counter = 0
# Initiating the loop
while counter < 10:  # Giving the condition
    counter = counter + 3
    print("Python Loops")

# Using else Statement with while Loops..example 2
# Python program to show how to use else statement with the while loop

counter = 0

# Iterating through the while loop
while counter < 10:
    counter = counter + 3
    print("Python Loops")  # Executed until condition is met
# Once the condition of while loop gives False this statement will be executed
else:
    print("Code block inside the else statement")

# Single statement while Block..example 3
# Python program to show how to write a single statement while loop

counter = 0
while counter < 3: print("Python Loops"); counter += 1
