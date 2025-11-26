"""
 Write a program to find uncommon words from two Strings
"""
s1=input("Enter first string: ")
s2=input("Enter second string: ")
result=""
for i in s1:
    if i not in s2:
        result+=i+" "    
for j in s2:
    if j not in s1:
        result+= j+ " "
print(f"Uncommon words are : {result}")        