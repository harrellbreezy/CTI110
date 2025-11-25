# Briana Harrell
# November 24 2025
# P2HW2
# This program should store grades entered in a list

# Pseudocode
# Ask user to enter grades for modules 1-6
# Store all grades in a list, give the list a descriptive name
# Display the following: lowest grade, highest grade, sum of grades, and the grades average

# get grades from user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# store grades in a list
grades = [mod1, mod2, mod3, mod4, mod5, mod6]

# calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total/ len(grades)

# display results
print("-----------------Results-------------------")
print("Lowest Grade: ", lowest)
print("Highest Grade: ", highest) 
print("Sum of grades: ", total)
print("Average: ", format(average, ".2f"))
print("------------------------------------------------------")