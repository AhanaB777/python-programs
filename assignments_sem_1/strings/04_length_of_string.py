"""
WAP to calculate the length of a string, avoid space.
"""

s = input("Enter a string: ")
length = len(s.replace(" ",""))
print(f"Length of string '{s}' is {length}")
