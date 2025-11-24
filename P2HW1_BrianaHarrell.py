# Briana Harrell
# November 23 2025
# P2HW1
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print()

# inputs
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# calculations
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print()
print("-----------------------------Travel Expenses---------------------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:.2f}")
print(f"{'fuel:':20}${gas:.2f}")
print(f"{'Accommodation:':20}${accommodation:.2f}")
print(f"{'Food:':20}${food:.2f}")
print("-----------------------------------------------")
print(f"Remaining Balance: ${remaining_balance:.2f}")