"""
Write a program to frequency of numbers in String 
"""
s=input("Enter a string: ")
d="0123456789"
c=0
for ch in s:
    if ch in d:
        c+=1   
print(f"Number of digits in string {s} is {c}")