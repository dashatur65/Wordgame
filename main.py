import random


def play_game():

# Step 1: List of words from the file, (I removed the word "hint" from the 4 letter word list, so it wouldnt mess up the "hint" option.)
    try:
        with open("4letter.txt") as file:
            words = [word.strip().upper() for word in file.readlines()]
        if not words:
            print("\033[31mWord list is empty!\033[0m")
            return
    except FileNotFoundError:
        print("\033[31mError: '4letter.txt' not found.\033[0m")
        return

# Step 2: Computer selects a random word
    random_word = random.choice(words)

# Get the player's name at the start
    player_name = input("Enter your name: ").capitalize()

# Instructions for the player
    print(f"\n\033[1m\033[34mWelcome to the word guessing game, {player_name}!\033[0m")
    print("The computer has chosen a 4-letter word. Your goal is to guess it.")
    print("\033[31mYou can ask for 1 hint by typing 'HINT'. Good luck!\033[0m\n")

# Guess counter
    guess_count = 1

# Lives (Hint System)
    max_hints = 1
    hearts = ["❤️"] # Red heart
    hints_given = 0  # To keep track of how many you've used

# Encouraging/motivational messages
    encouragements = [
        "You're doing great, {name}!",
        "Keep it up, {name}!",
        "You're getting closer, {name}!",
        "Nice try, {name}!",
        "You're almost there, {name}!",
        "Don't give up, {name}!"
    ]

# Start the game loop
    while True:
# Show current score (guess count) in green and available hearts
        print(f"\033[32mCurrent Guess Count: {guess_count}\033[0m")
        print(f"\033[31mHint left: {' '.join(hearts)}\033[0m")

# Ask the user/player for a guess or a hint
        guess = input("Guess the 4-letter word or type 'HINT' for a hint: ").upper()

# Handle the hint request (only if the input is exactly "HINT")
        if guess == 'HINT':
            if hints_given < max_hints:
# Provide the next letter in sequence
                hint = random_word[:hints_given + 1]
                print(f"\033[1mHint: The first {hints_given + 1} letter(s) of the word are '{hint}'.\033[0m")
                hearts[hints_given] = "💔"  # Shattered heart from the right
            else:
                print("\033[31mNo more hints available!\033[0m")
            continue

# Ensure the guess is valid
        if len(guess) != 4 or not guess.isalpha() or guess not in words:
            print("\n\033[31mInvalid input! Please enter a valid 4-letter word from the list.\033[0m\n")
            continue

# Increase the guess counter after a valid guess
        guess_count += 1

# Step 3: Check how many letters are correct and in the right position
        correct = sum(1 for a, b in zip(random_word, guess) if a == b)

# Bold the number of correct letters
        print(f"\033[1m{correct} letter(s) are in the correct position.\033[0m\n")

        if correct == 4:
            print(f"\n✨ \033[1mCorrect! The word was '{random_word}'.\033[0m")
            print(f"🎉  Congratulations, {player_name}! You guessed the word in {guess_count} tries.")
            break
        elif correct > 0:
# If at least one letter is correct, give a random encouragement message
            print(f"\033[35m{random.choice(encouragements).format(name=player_name)}\033[0m")

# Simple leaderboard for this session
    leaderboard.append((player_name, guess_count))
    leaderboard.sort(key=lambda x: x[1])

# Show the leaderboard
    print("\n\033[1mLeaderboard:\033[0m")
    for player, score in leaderboard:
        print(f"{player}: {score} guesses")

# Initialize the leaderboard for the current session
leaderboard = []

# Main loop for replaying the game
while True:
    play_game()

# Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\n\033[31mThank you for playing! Goodbye!\033[0m")
        break
