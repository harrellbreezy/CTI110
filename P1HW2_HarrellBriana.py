# Briana Harrell
# November 10, 2025
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much wi;l you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("-----Travel expenses---------")
print("Location:", destination)
print("Initial budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("food:", food)
print()
print("Remaining Balance:", remaining_balance)
