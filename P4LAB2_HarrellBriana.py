# Briana Harrell
# December 13 2025
# P4LAB2
# This program shows the multiplication table of a number entered by the user.


choice = "yes"

while choice.lower() == "yes":
    number = int(input("Enter an integer: "))

    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    print()
    choice = input("Would you like to run the program again? ")
    print()

print("Exiting program...")
