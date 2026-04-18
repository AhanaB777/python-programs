"""
Write a program to capitalize the first and last character of each word in a string
"""
s = input("Enter a string: ")

result = ""
n = len(s)

for i in range(n):

    ch = s[i]

    # FIRST character of a word
    if (i == 0 or s[i-1] == ' ') and ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)   # make uppercase
        continue

    # LAST character of a word
    if (i == n-1 or s[i+1] == ' ') and ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)   # make uppercase
        continue

    # Otherwise keep the character as it is
    result += ch

print(result)

