"""
Write a program to specific Characters Frequency in String List
"""
s = input("Enter strings separated by space: ")
ch = input("Enter the character to count: ")
count=0
for i in s:
    if i==ch:
        count+=1
print(count)