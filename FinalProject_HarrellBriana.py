# Briana Harrell
# December 13 2025
# Final Project
# "Heads or Tails" coin flip game.

# Psuedocode
# Import random
# Set the wins to 0
# Set the rounds to 0
# While rounds is less than 5:
#  ask user to guess heads or tails
#  flip coin randomly
#  IF guess is correct, increase wins 
# IF wins is 3 or more , display "You win the game"
# ELSE display "You lose the game"



import random 

def play_round(): 
    coin = random.choice(["heads", "tails"])
    guess = input("Guess heads or tails: ").lower()

    if guess == coin: 
        print("Correct!")
        return 1
    else:
        print("Wrong! It was", coin)
        return 0

def main():
    wins = 0
    rounds = 0

    while rounds < 5:
        wins += play_round()
        rounds += 1
        print()

    print("You won", wins, "out of 5 rounds.")

    if wins >= 3:
        print("You win the game!")
    else:
        print("You lose the game.")


main()