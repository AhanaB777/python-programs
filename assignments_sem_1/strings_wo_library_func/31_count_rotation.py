"""
Write a program to find minimum number of rotations to obtain actual string
"""
s = input("Enter string: ")

original = s
count = 0

while True:
    s = s[1:] + s[0]   # rotate left once
    count += 1

    if s == original:
        break

print("Minimum rotations:", count)