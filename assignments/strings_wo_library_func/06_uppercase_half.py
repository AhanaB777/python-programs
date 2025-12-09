"""
Write a program to uppercase Half String. 
"""
s = input("Enter a string: ")

# find length
length = 0
for _ in s:
    length += 1

# midpoint
mid = length // 2

result = ""
i = 0

for ch in s:
    if i < mid:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        else:
            result += ch
    else:
        result += ch

    i += 1

print("Result:", result)

