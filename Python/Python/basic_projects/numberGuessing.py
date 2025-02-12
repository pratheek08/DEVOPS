import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number (1-100): "))

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it right.")
            break  # Exit loop when the correct number is guessed

    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")
