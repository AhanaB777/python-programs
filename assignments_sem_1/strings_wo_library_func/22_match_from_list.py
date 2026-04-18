"""
 Write a program to find all close matches of input string from a list 
"""
target = input("Enter target string: ")

lst = ["apple", "apply", "ape", "maple", "people"]
matches = []

for word in lst:
    same = 0
    for i in range(min(len(word), len(target))):
        if word[i] == target[i]:
            same += 1
    if same >= 2:   # similarity threshold
        matches.append(word)

print("Close matches:", matches)

