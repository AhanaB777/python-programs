"""
WAP to calculate the length of a string, avoid space.
"""

s = input("Enter a string: ")

length = 0

for ch in s:
    if ch != " " :
        length+=1

print(f"Length of string without counting space is {length}")

