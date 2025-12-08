# Briana Harrell
# December 7 2025
# P4HW1
# This program collects valid scores, removes the lowest one, calculates the average, and shows the final grade.

# Pseudocode
# Ask user how many scores they want to enter.
# Create an empty list to store scores.
# Loop for each score needed.
# Ask user for score.
# If invalid, show error message.
# Use a loop to keep asking until a valid score is entered.
# Add valid score to the list.
# After collecting all scores: Identify lowest score, create modified list, calculate average, determine letter grade, display results.


num_scores = int(input("How many scores do you want to enter? "))

scores = []

num = 1
while num <= num_scores:
    score = float(input("Enter score #" + str(num) + ": "))

    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter score #" + str(num) + " again: "))

    scores = scores + [score]
    num = num + 1

# Calculate 
lowest = min(scores)
scores.remove(lowest)
average = sum(scores) / len(scores)

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

#Output
print("\n--------------Results-------------")
print("Lowest Score : " + str(lowest))
print("Modified List : " + str(scores))
print("Scores Average: " + format(average, ".2f"))
print("Grade        : " + grade)
print("---------------------------------")
