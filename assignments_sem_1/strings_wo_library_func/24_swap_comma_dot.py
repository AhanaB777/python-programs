"""
Write a program to swap commas and dots in a String 
"""
s = input("Enter string: ")
new_s = ""

for ch in s:
    if ch == ",":
        new_s += "."
    elif ch == ".":
        new_s += ","
    else:
        new_s += ch

print(new_s)