count = 3  # User gets 3 attempts initially
key = "Y"  # Control variable: 'Y' to continue, 'N' to exit

while count > 0 and key == "Y":
    try:
        age = int(input("Guess my age: "))  # Prompt user for input
    except ValueError:
        print("Please enter a valid integer.")  # Handle non-integer input
        continue  # Skip this round, don't reduce count

    if age == 23:
        print("Congratulations! You guessed it right.")
        key = "N"  # Exit the game
    else:
        count -= 1
        if count > 0:
            print(f"Wrong guess. You have {count} guesses left.")
        else:
            # If user used all attempts, ask whether to continue
            key = input("Too many attempts! Continue? Enter 'Y' for 3 more chances or 'N' to exit: ").strip().upper()
            if key == "Y":
                count = 3  # Reset attempts
            elif key != "N":
                print("Invalid input. Exiting the game.")
                key = "N"
