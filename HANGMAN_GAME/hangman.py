import random
words = ["python", "hangman", "game", "coding", "random"]


word = random.choice(words)
print("[DEBUG] The word is:", word)  
guessed = ["_"] * len(word)   
attempts = 6                 
used_letters = []             

print(" Welcome to Hangman!")
print("Guess the word:")


while attempts > 0 and "_" in guessed:
    print("\nWord: ", " ".join(guessed))
    print("Used letters:", " ".join(used_letters))
    print(f"Remaining attempts: {attempts}")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet only!")
        continue

    if guess in used_letters:
        print(" You already guessed that letter!")
        continue

    used_letters.append(guess)

    if guess in word:
        print(" Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        print(" Wrong guess!")
        attempts -= 1

if "_" not in guessed:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over! The word was:", word)