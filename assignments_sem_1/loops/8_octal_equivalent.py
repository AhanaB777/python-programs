"""
    Write a program to find the octal equivalent of the entered number.
"""

n_decimal=int(input("Enter a number: "))

n_octal=0
i=1

while n_decimal != 0:
    rem = n_decimal%8
    n_octal += rem*i
    n_decimal //= 8
    i *= 10

print(f"The octal equivalent is {n_octal}")
