import random


def number_guessing():
    print("Welcome to the Number Guessing Game!")
    lower = int(input("Enter the lowest number of the range: "))
    upper = int(input("Enter the Highest number of the range: "))

    number = random.randint(lower, upper)


    while True:
        try:
            guess = int(input(f"Guess the number between {lower} and {upper}: "))


            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("Congratulations!")
                break
        except ValueError:
            print("Please enter a valid number.")


# Run the game
number_guessing()
