"""
Write a program to count the Number of matching characters in a pair of string 
"""
s1= input("Enter first string: ")
s2= input("Enter second string: ")

count=0
s3=""

for i in s1 :
    if i in s2 and i not in s3 :
        count+=1
        s3+=i

print(f"Number of matching characters: {count}")