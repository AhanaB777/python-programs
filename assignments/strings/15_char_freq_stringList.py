"""
Write a program to specific Characters Frequency in String List
"""
strings = input("Enter strings separated by space: ").lower().split()

ch = input("Enter the character to count: ")

total = sum(s.count(ch) for s in strings)

print("Total frequency =", total)
