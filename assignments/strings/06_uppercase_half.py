"""
Write a program to uppercase Half String. 
"""
s=input("Enter a string: ")
length=len(s)//2
res=s[:length].upper()+s[length:]
print(f"Resulted string: {res}")
