"""
 Write a program to find uncommon words from two Strings
"""
s1 = input("Enter first sentence: ")
s2 = input("Enter second sentence: ")

words1 = []
words2 = []

# split s1
word = ""
for ch in s1 + " ":
    if ch != " ":
        word += ch
    else:
        words1.append(word)
        word = ""

# split s2
word = ""
for ch in s2 + " ":
    if ch != " ":
        word += ch
    else:
        words2.append(word)
        word = ""

uncommon = []

for w in words1:
    found = False
    for x in words2:
        if w == x:
            found = True
            break
    if not found:
        uncommon.append(w)

for w in words2:
    found = False
    for x in words1:
        if w == x:
            found = True
            break
    if not found:
        uncommon.append(w)

print("Uncommon:", uncommon)      