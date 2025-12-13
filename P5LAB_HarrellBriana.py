# Briana Harrell
# December 13 2025
# P5LAB
# This program simulates a self checkout machine and siperses change.

import random

def disperse_change(change):
    # Convert change to cents
    change = round(change * 100)

    # Calculate
    dollars = change // 100
    change = change - (dollars * 100)

    quarters = change // 25
    change = change - (quarters * 25)

    dimes = change // 10
    change = change - (dimes * 10)

    nickels = change // 5
    change = change - (nickels * 5)

    pennies = change

    # Output
    if dollars > 0:
        print(f"{dollars} Dollars")

    if quarters > 0:
        print(f"{quarters} Quarters")

    if dimes > 0:
        print(f"{dimes} Dimes")

    if nickels > 0:
        print(f"{nickels} Nickels")

    if pennies > 0:
        print(f"{pennies} Pennies")

def main():
    # Generate random amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")

    # Get cash from user
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change:.2f}\n")

    # Disperse change
    disperse_change(change)

main()






    