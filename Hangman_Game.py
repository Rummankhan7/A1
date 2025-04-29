import random

words = ['apple', 'banana', 'computer', 'python', 'hangman','rcb','khan']
word = random.choice(words)
guessed = ''
tries = 6

print("Welcome to Hangman!")

while tries > 0:
    display = ''
    for letter in word:
        display += letter if letter in guessed else '_'

    print("\nWord:", display)
    print("Guessed letters:", ' '.join(guessed))

    if display == word:
        print("You won!")
        break

    guess = input("Guess a letter: ").strip().lower()

    if not guess or not guess.isalpha() or len(guess) != 1:
        print("Please enter a **single alphabet letter**.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed += guess

    if guess not in word:
        tries -= 1
        print("Wrong! Tries left:", tries)

if tries == 0:
    print("\nYou lost! The word was:", word)