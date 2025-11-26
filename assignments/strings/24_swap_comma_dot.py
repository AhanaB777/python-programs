"""
Write a program to swap commas and dots in a String 
"""
s=input("Enter a string: ")
print(f"Before swapping dots and commas: {s}")

temp = s.replace(",","#")
temp=temp.replace(".",",")
result=temp.replace("#",".")

print(f"After swapping dots and commas: {result}")