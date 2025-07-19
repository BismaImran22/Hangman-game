# Hangman Text-Based Game
# Key Concepts: Loops, Conditionals, Lists

import random

# Predefined list of 5 words
word_list = ['apple', 'banana', 'grape', 'orange', 'peach']

# Choose a random word from the list
choosen_word = random.choice(word_list)
word_length = len(choosen_word)
display = ['_'] * word_length
lives = 6

print("Welcome to Hangman!")
print(f"The word has {word_length} letters: {' '.join(display)}")

while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed '{guess}'. Try again.")
        continue

    if guess in choosen_word:
        for index, letter in enumerate(choosen_word):
            if letter == guess:
                display[index] = guess
        print(f"Good guess! Current word: {' '.join(display)}")
    else:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")
        print(f"Current word: {' '.join(display)}")

if '_' not in display:
    print("Congratulations, you won!")
else:
    print(f"Game over! The word was {choosen_word}.")