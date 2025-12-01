# Briana Harrell
# November 30 2025
# P3LAB
# This program allows the user to enter a money (float) value with two places after the decimal. 

#Get user input
change = float(input("Enter the amount of money as a float: $"))

# Converting the value to an integer
change = round(change * 100)

# Determine how many coins are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - num_quarters * 25

num_dimes = change // 10
change = change - num_dimes * 10

num_nickels = change // 5
change = change - num_nickels * 5

num_pennies = change

   # Output
if num_dollars > 0:
        print(f"{num_dollars} Dollar" if num_dollars == 1 else f"{num_dollars} Dollars")

if num_quarters > 0:
        print(f"{num_quarters} Quarter" if num_quarters == 1 else f"{num_quarters} Quarters")

if num_dimes > 0:
        print(f"{num_dimes} Dime" if num_dimes == 1 else f"{num_dimes} Dimes")

if num_nickels > 0:
        print(f"{num_nickels} Nickel" if num_nickels == 1 else f"{num_nickels} Nickels")

if num_pennies > 0:
        print(f"{num_pennies} Penny" if num_pennies == 1 else f"{num_pennies} Pennies")