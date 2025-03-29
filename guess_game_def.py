def guess_game():
    correct_age = 23             # The correct answer to guess
    max_attempts = 3             # Maximum attempts allowed per round
    key = "Y"                    # Controls whether the user wants to continue

    while key == "Y":
        count = max_attempts     # Reset attempts at the start of each round
        while count > 0:
            try:
                guess = int(input("Guess my age: "))  # User input (must be an integer)
            except ValueError:
                print("Please enter a valid integer!")  # Handle non-integer input
                continue  # Skip this round and ask again

            if guess == correct_age:
                print("Congratulations! You guessed it right!")
                return  # Exit the game immediately if guessed correctly
            else:
                count -= 1
                if count > 0:
                    print(f"Incorrect. You have {count} attempts left.")

        # After 3 incorrect attempts, ask if the user wants to continue
        key = input("Attempts used up. Do you want to continue? Enter 'Y' to try again, or 'N' to quit: ").strip().upper()
        if key not in ["Y", "N"]:
            print("Invalid input. Exiting the game by default.")
            key = "N"  # Exit if input is invalid

    print("Game over. Thanks for playing!")

# Start the game
guess_game()
