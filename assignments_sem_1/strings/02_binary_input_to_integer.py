"""
Write a program to take binary input numbers and convert it to an integer without 
using int() function. 
"""
b = input("Enter binary number: ")

decimal = 0
for i in b:
    bit = ord(i) - ord('0')
    decimal = decimal * 2 + bit

print(f"Decimal value: {decimal}")