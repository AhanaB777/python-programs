"""
WAP to remove i^th character of a string.
"""

s = input("Enter a string: ")
i = int(input("Enter value of i: "))
result=s[:i]+s[i+1:]
print(result)

