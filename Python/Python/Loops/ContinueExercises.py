#Python Continue Statements in for Loop

#Printing numbers from 10 to 20 except 15 can be done using continue statement and for loop. The following code is an example of the above scenario:

for iterator in range(10, 21): 
    if iterator == 15: 
        continue 
    print(iterator) 

#Python Continue Statements in while Loop

string = "JavaTpoint" 
iterator = 0 

while iterator < len(string): 
    if string[iterator] == 'a':
        continue 
    print(string[iterator]) 
    iterator += 1 

#Python Continue statement in list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
sq_num = [num ** 2 for num in numbers if num % 2 == 0] 
print(sq_num)
