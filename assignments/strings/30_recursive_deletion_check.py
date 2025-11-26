"""
Write a program to string slicing in Python to check if a string can become empty by 
recursive deletion 
"""
s = input("Enter main string: ")
sub = input("Enter substring to delete: ")

while sub in s:
    #s = s.replace(sub, "")
    index=s.find(sub)
    s=s[:index] + s[index+len(sub):]

if len(s) == 0:
    print("YES, the string can become empty.")
else:
    print("NO, final string:", s)
