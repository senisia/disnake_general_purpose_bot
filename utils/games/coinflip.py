import random

choices = ["heads", "tails"]

def coinflip(coinflip_choice):
    result = random.choice(choices)
    if coinflip_choice == result:
        return True
    elif coinflip_choice != result:
        return False
    else:
        return "There has been an error"