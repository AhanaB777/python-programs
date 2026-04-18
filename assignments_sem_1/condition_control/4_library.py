"""
    A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10
    days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days
    your membership will be cancelled. Write a program to accept the number of days the member is
    late to return the book and display the fine or the appropriate message
"""
days = int(input("Enter number of days late: "))

if days <= 0:
    print("No fine. Book returned on time.")
elif days <= 5:
    fine = days * 0.5
    print(f"Fine: Rs. {fine}")
elif days <= 10:
    fine = (5 * 0.5) + (days - 5) * 1
    print(f"Fine: Rs. {fine}")
elif days <= 30:
    fine = (5 * 0.5) + (5 * 1) + (days - 10) * 5
    print(f"Fine: Rs. {fine}")
else:
    print("Membership cancelled.")


