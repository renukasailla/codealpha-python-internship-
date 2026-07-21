import random

words = ["python", "apple", "computer", "college", "program"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("=== Welcome to Hangman Game ===")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts Left:", attempts)
    print("Guessed Letters:", " ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print("Wrong!")
        attempts -= 1

if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n😢 Game Over! The word was:", word)
