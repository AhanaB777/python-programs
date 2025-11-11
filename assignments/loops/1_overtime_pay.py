"""
    Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs.
    12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for
    fractional part of an hour.
"""
# Program to calculate overtime pay of 10 employees

rate = 12  # Rs 12 per extra hour

for emp in range(1, 11):   # employees 1 to 10
    hours = int(input("Enter hours worked by employee " + str(emp) + ": "))

    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate
    else:
        overtime_hours = 0
        overtime_pay = 0

    print("Employee", emp, "overtime hours =", overtime_hours)
    print("Employee", emp, "overtime pay = Rs", overtime_pay)
    print()   # blank line for readability
