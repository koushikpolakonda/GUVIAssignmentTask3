import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble_game():
    words = ["python", "javascript", "java", "automation", "pytest", "guvi", "selenium"]
    word_to_guess = random.choice(words)
    scrambled = scramble_word(word_to_guess)

    print("Welcome to the Word Scramble Game!")
    print(f"Unscramble this word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").strip().lower()
        if guess == word_to_guess:
            print("Correct! You unscrambled the word!")
            break
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print(f"Out of attempts! The correct word was: {word_to_guess}")

# Run the game
word_scramble_game()
