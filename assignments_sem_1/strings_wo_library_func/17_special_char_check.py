"""
Write a program to program to check if a string contains any special character
"""
s = input("Enter a string: ")

has_special = False

for ch in s:
    if not ((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9')):
        has_special = True
        break

if has_special:
    print("Contains special character")
else:
    print("No special character")