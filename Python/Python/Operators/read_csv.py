# Importing the csv module
import csv 

# Open file within the 'with' block
with open(r'C:\Users\289226\Desktop\DevOps Training\Python\example.csv', mode='r') as csv_file: 
    csv_read = csv.reader(csv_file, delimiter=',')  # Delimiter is comma
    
    count_line = 0  # Initialize line counter

    # Iterate through the rows
    for row in csv_read:
        if count_line == 0:
            print(f'Column names are {", ".join(row)}')  # Print header row
        else:
            print(f'\t{row[0]} roll number is: {row[1]} and department is: {row[2]}.')
        
        count_line += 1  # Increment line counter

# Print total processed lines
print(f'Processed {count_line} lines.')