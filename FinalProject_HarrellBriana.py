# Briana Harrell
# December 13 2025
# Final Project
# "Heads or tails" coin flip game. This program lets the user guess heads or tails and play again.

# Psuedocode
# Import random
# Ask user to guess heads or tails
# Flip coin randomly
# IF guess is correct, display win message
# ELSE- display lose message
# Ask user if they want to play again




import random 

def flip_coin(): 
    coin = random.choice(["heads", "tails"])
    guess = input("Guess heads or tails: ").lower()

    if guess == coin: 
        print("You win!")
    else:
        print("You lose. It was", coin)

def main():
    play = "yes"
    while play == "yes":
        flip_coin()
        play = input("Play again? (yes/no): ").lower()

main()