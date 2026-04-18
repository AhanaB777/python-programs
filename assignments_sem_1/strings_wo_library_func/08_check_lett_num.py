"""
Python program to check if a string has at least one letter and one number 
"""
s=input("Enter a string: ")
digits="0123456789" 
letters="AaBbCcDdEeFfGgHhIiJjkKlLmMnNoOpPQqRrSsTtUuVvWwXxYyZz"
d=False
l=False
for ch in s:
    if ch in digits :
        d=True 
    if ch in letters:
        l=True

if d and l :
    print("String contains both digits and letters")
else:
    print("Does not contain both digits and letters")


