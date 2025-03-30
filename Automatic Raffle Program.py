# Example:Automatic Raffle Program
import random   # Module to randomly select an item from a list
prize_list=["iphone12","Watch","Spa treatment","5-day Trip to Thailand"]
while prize_list:
    name=input("Automatic Raffle Program. Please enter your name:")
    selected_prize=random.choice(prize_list)
    # random.choice() is a function provided by Python's built-in random module, used to randomly pick an element from a non-empty sequence such as a list, tuple, or string.
    print(f"Congratulations{name},you have won a{selected_prize}.")

    #remove the selected_prize from the list,as each prize can only be won once
    prize_list.remove(selected_prize)
