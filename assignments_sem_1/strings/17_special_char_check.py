"""
Write a program to program to check if a string contains any special character
"""
s=input("Enter a string: ")
spec_char = any(not ch.isalnum() and not ch.isspace() for ch in s)

if spec_char:
    print(f"String contains special characters ")
else :
    print(f"String does not contain special characters ") 