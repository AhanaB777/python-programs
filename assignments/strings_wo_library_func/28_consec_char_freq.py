"""
Write a program to find consecutive characters frequency
"""
s = input("Enter a string: ")

count = 1
for i in range(1, len(s)):

    if s[i] == s[i-1]:
        count += 1
    else:
        print(s[i-1], "=", count)
        count = 1

if s:
    print(s[-1], "=", count)
