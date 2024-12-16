import random
def guess_the_number():
    # Set the range for the random number
    low = 1
    high = 100

    # Generate a random number within the specified range
    number_to_guess = random.randint(low, high)

    # Initialize the number of attempts
    attempts = 0

    # Start the game
    print(f"Welcome to the Guess the Number Game!")
    print(f"I have selected a number between {low} and {high}. Can you guess what it is?")

    while True:
        # Increment the number of attempts
        attempts += 1

        # Get the user's guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Check if the guess is too low, too high, or correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
            break


# Run the game
guess_the_number()

