"""
Write a program to accept the strings which contain all vowels
"""
s=input("Enter a string : ")

vowels="aAeEiIoOuU"

for i in s:
    if i not in vowels:
        print("String is rejected.")
        break

else:
    print("String is accepted")
    