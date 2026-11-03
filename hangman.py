import random

# List of possible secret words
words = [
    "python",
    "developer",
    "computer",
    "programming",
    "internship",
    "keyboard",
    "software",
    "technology"
]

# ASCII gallows stages
HANGMAN_STAGES = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]


def display_word(secret_word, guessed_letters):
    """Display correctly guessed letters and hide the rest."""
    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter.upper() + " "
        else:
            displayed_word += "_ "

    return displayed_word.strip()


def play_hangman():
    """Run the Hangman game."""

    secret_word = random.choice(words)

    guessed_letters = set()
    incorrect_guesses = set()

    attempts = 6

    print("\n" + "=" * 35)
    print("       WELCOME TO HANGMAN")
    print("=" * 35)

    while attempts > 0:

        print(HANGMAN_STAGES[len(incorrect_guesses)])

        print("\nWord:", display_word(secret_word, guessed_letters))

        print("Incorrect guesses:", 
              " ".join(sorted(incorrect_guesses)) 
              if incorrect_guesses else "None")

        print("Attempts remaining:", attempts)

        guess = input("\nGuess a letter: ").strip().lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You have already guessed that letter!")
            continue

        # Check whether the letter is correct
        if guess in secret_word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            incorrect_guesses.add(guess)
            attempts -= 1
            print("Incorrect guess!")

        # Check for victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + HANGMAN_STAGES[len(incorrect_guesses)])
            print("Word:", secret_word.upper())
            print("\nCongratulations! You guessed the word!")
            break

    else:
        print(HANGMAN_STAGES[6])
        print("\nGAME OVER!")
        print("The secret word was:", secret_word.upper())


# Start the game
if __name__ == "__main__":
    play_hangman()
