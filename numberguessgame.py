import random  # Importing the random module to generate random numbers.
import math  # Importing the math module for mathematical functions.

print("Welcome to the Number Guessing Game!")

# Taking input for the lower bound of the range.
lower = int(input("Enter the first number: "))  # Prompts the user to enter the lower bound and converts it to an integer.

# Taking input for the upper bound of the range.
upper = int(input("Enter the second number: "))  # Prompts the user to enter the upper bound and converts it to an integer.

# Generates a random number which the user has to guess.
x = random.randint(lower + 1, upper - 1)  # Uses the .randint function of the random module to generate a random integer, within the two bounds.

# Calculates the maximum number of allowed attempts to guess number 'x'.
max_tries = round(math.log(upper - lower + 1, 2))  # Uses the .log function (log base 2: the binary logarithm) of the math module to calculate the maximum number of allowed attempts and rounds it.

# Informing the user of the number of attempts they have.
if max_tries == 1:
    print("\n\tYou have only 1 chance to guess the correct number.\n")  # When the user has only 1 chance to guess the correct number.
else:
    print("\n\tYou have", max_tries, "chances to guess the correct number.\n")  # When the user has more than 1 chance to guess the correct number, with a limit of chances.

# Initializing the number of guesses.
count = 0  # The guess count starts with 0.

# While loop to allow the user to guess the number (x) within the allowed attempts. 
# Continues the loop until the user has exceeded the maximum number of allowed attempts.
while count < max_tries:
    count += 1  # Increases the guess count with 1, every time the user guesses.

    # Taking the user's guess as input.
    guess = int(input("Enter a number: "))  # Prompts the user to enter a number, as a guess, and converts it to an integer.
    
    # Conditioning to check if the guess is correct, too low, or too high.
    if guess == x: 
        if count == 1:
            print("\n\tYou are a master, you did it in 1 try.\n")  # Correct guess on the first attempt. 
        else:
            print("\n\tCongratulations, you did it in", count, "tries.\n")  # Correct guess after multiple attempts.
        break
    elif x > guess:
        print("Too small!")  # Tells the user that their guess is not correct, it's too small.
    elif x < guess:
        print("Too high!")  # Tells the user that their guess is not correct, it's too high.
        
# If the number of guesses has exceeded the allowed attempts. 
else:
    print("\nThe correct number is %d." % x)  # Reveals the correct number failing to guess the correct number within the allowed attempts.
    print("\tBetter luck next time!")  # Encourages the user to try again.