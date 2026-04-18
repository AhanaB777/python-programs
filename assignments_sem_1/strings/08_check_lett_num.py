"""
Python program to check if a string has at least one letter and one number 
"""
s=input("Enter a string: ")
d=l=False
for i in s :
    if i.isalpha() :
        l=True
    if i.isdigit() :
        d=True
if d and l :
    print("String contains both digits and letters")
else:
    print("Does not contain both digits and letters")


