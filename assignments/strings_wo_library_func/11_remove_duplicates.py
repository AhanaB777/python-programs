"""
 Write a program to remove all duplicates from a given string in Python, keeping the 
first character only 
"""
s = input("Enter a string : ")
result = ""

for i in s:
    if i not in result :
        result+=i

print(f"Resulted string : {result}")
