"""
Write a program to take input a string of digits and convert it to an integer without 
using int() function. 
"""
s = input("Enter a number string: ")

num = 0
for ch in s:
    digit = ord(ch) - ord('0')     
    num = num * 10 + digit         

print(f"Converted integer: {num}")
