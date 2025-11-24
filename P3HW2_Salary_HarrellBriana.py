# Briana Harrell
# November 23 2025
# P3HW2
# Salary Calculator

# Pseudocode
# Ask user for employee name
# Ask user for hours worked by employee
# Ask user to enter employee's pay rate

# If hours worked > 40:
#    overtime hours = hours - 40
#    overtime pay = overtime hours * (pay rate * 1.5)
#    regular pay = 40 * rate
#    gross pay = ragular pay + overtime pay

# Else:
#   overtime pay = 0
#   overtime hours = 0
#   regular pay = hours * rate
#   gross pay = regular_pay

# Display the following:
# Employee Name, Pay Rate, Hours Worked, Overtime Hours, Overtime Pay, Regular Pay, Gross Pay




# request employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# evaluate overtime
if hours > 40:
    # calculate overtime
    overtime_hours = hours - 40
    # calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # calculate salary for regular hours
    regular_pay = 40 * rate
    # calculate gross pay
    gross_pay = regular_pay + overtime_pay 
else:
    overtime_pay = 0 
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# display results
print("---------------------------------------")
print("Employee Name:", name)
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"Overtime Pay":<15}{"Regular Pay":<15}{"Gross Pay":<12}')
print("-----------------------------------------------------------------")
print(f'{hours:<15}${rate:<12.2f}${overtime_pay:<15.2f}${regular_pay:<15.2f}${gross_pay:<15.2f}')
