"""
Write a program to find minimum number of rotations to obtain actual string
"""
s = input("Enter a string: ")

rot = s
count = 0

while True:
    rot = rot[1:] + rot[0]  
    count += 1
    if rot == s:
        break

print("Minimum rotations needed:", count)
