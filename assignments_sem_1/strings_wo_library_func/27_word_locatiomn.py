"""
Write a program to word location in String
"""
s = input("Enter sentence: ")
target = input("Enter word to find: ")

words = []
word = ""
for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        words.append(word)
        word = ""

index = -1
for i in range(len(words)):
    if words[i] == target:
        index = i
        break

print("Location:", index)
