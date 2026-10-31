import random

WORDS = ["python", "program", "computer", "keyboard", "internet"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("=== HANGMAN GAME ===")
    print(f"The word has {len(word)} letters. Maximum wrong guesses: {MAX_WRONG}\n")

    while wrong < MAX_WRONG:
        display = " ".join(ch if ch in guessed else "_" for ch in word)
        print("Word:", display)
        print("Wrong guesses left:", MAX_WRONG - wrong)
        print("Letters guessed so far:", ", ".join(guessed) if guessed else "-")

        if "_" not in display:
            print("\nCongratulations! You won! The word was:", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter only!\n")
            continue
        if guess in guessed:
            print("You already guessed that letter!\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

    print("Game over! You lost. The correct word was:", word)


if __name__ == "__main__":
    while True:
        play()
        again = input("\nDo you want to play again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break
        print()