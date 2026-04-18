"""
Write a program to find words that are greater than the given length k
"""
s = input("Enter a sentence: ")
k = int(input("Enter length k: "))

word = ""
for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        if len(word) > k:
            print(word)
        word = ""