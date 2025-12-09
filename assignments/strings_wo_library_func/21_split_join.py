"""
 Write a program to split and join a string 
"""
s = input("Enter sentence: ")
split_words = []

word = ""
for ch in s + " ":
    if ch != " ":
        word += ch
    else:
        split_words.append(word)
        word = ""

joined = ""
for w in split_words:
    joined += w + " "

print("Split:", split_words)
print("Joined:", joined[:-1])