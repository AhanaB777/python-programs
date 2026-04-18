"""6. Write a Python program to understand the use of asterisk(*) character declared in a function."""

def add(*nums):
    total = 0
    for i in nums:
        total += i
    print("Sum =", total)

add(2, 3)
add(1, 2, 3, 4, 5)
