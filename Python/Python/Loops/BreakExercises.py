# Example 1: break statement with for loop
# break statement example 
my_list = [1, 2, 3, 4] 
count = 1 
for item in my_list: 
    if item == 4: 
        print("Item matched") 
        count += 1 
        break 
print("Found at location", count) 

# Example 2: Breaking out of a loop early
# break statement example 
my_str = "python" 
for char in my_str: 
    if char == 'o': 
        break 
    print(char) 

# Example 3: break statement with while loop
# break statement example 
i = 0
while True: 
    print(i, " ", end="")
    i = i + 1
    if i == 10: 
        break
print("came out of while loop")

# Example 4: break statement with nested loops
# break statement example 
n = 2 
while True: 
    i = 1 
    while i <= 10: 
        print("%d X %d = %d\n" % (n, i, n * i)) 
        i += 1 
    choice = int(input("Do you want to continue printing the table? Press 0 for no: ")) 
    if choice == 0: 
        print("Exiting the program...") 
        break 
    n += 1 
print("Program finished successfully.")
