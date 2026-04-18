"""
Write a program to string slicing in Python to check if a string can become empty by 
recursive deletion 
"""
s = input("Enter string: ")
pattern = input("Enter pattern to delete: ")

while True:
    found = False
    i = 0

    while i <= len(s) - len(pattern):
        match = True
        for j in range(len(pattern)):
            if s[i+j] != pattern[j]:
                match = False
                break
        if match:
            s = s[:i] + s[i+len(pattern):]
            found = True
        else:
            i += 1

    if not found:
        break

if s == "":
    print("String can become empty")
else:
    print("String cannot become empty")