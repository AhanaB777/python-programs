"""
Write a program to frequency of numbers in String 
"""
s=input("Enter a string: ")
digits=0
for ch in s:
    if ch.isdigit():
        digits+=1   
print(f"Number of digits in string {s} is {digits}")