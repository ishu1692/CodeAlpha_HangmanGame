import random

# ===============================
# Enhanced Hangman Game
# ===============================

# Predefined words with hints
words = {
    "apple": "A fruit",
    "tiger": "A wild animal",
    "python": "A programming language",
    "planet": "Exists in space",
    "school": "A place to study"
}

# Choose random word
word = random.choice(list(words.keys()))
hint = words[word]

# Game variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Hangman stages
hangman_stages = [
    """
     ----
     |  |
        |
        |
        |
        |
    --------
    """,
    """
     ----
     |  |
     O  |
        |
        |
        |
    --------
    """,
    """
     ----
     |  |
     O  |
     |  |
        |
        |
    --------
    """,
    """
     ----
     |  |
     O  |
    /|  |
        |
        |
    --------
    """,
    """
     ----
     |  |
     O  |
    /|\\ |
        |
        |
    --------
    """,
    """
     ----
     |  |
     O  |
    /|\\ |
    /   |
        |
    --------
    """,
    """
     ----
     |  |
     O  |
    /|\\ |
    / \\ |
        |
    --------
    """
]

# Welcome message
print("=" * 40)
print("🎮 WELCOME TO HANGMAN GAME 🎮")
print("=" * 40)

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display current hangman stage
    print(hangman_stages[wrong_guesses])

    # Display word progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Hint:", hint)
    print("Guessed Letters:", " ".join(guessed_letters))
    print(f"Remaining Chances: {max_wrong_guesses - wrong_guesses}")

    # Check win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word.upper())
        break

    # User input
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only ONE alphabet letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Save guessed letter
    guessed_letters.append(guess)

    # Correct or wrong guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        print("❌ Wrong Guess!")
        wrong_guesses += 1

# Lose condition
if wrong_guesses == max_wrong_guesses:
    print(hangman_stages[wrong_guesses])
    print("\n💀 GAME OVER!")
    print("The correct word was:", word.upper())

print("\nThanks for playing Hangman! 🎯")