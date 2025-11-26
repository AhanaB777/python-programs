"""
Write a program to word location in String
"""
"""
s = input("Enter a string: ")
word = input("Enter the word to find: ")

start = 0
positions = []

while True:

    index = s.find(word, start)

    if index == -1:
        break

    positions.append(index)

    start = index + len(word)

print("Locations:", positions) """

s = input("Enter a string: ")
word = input("Enter the word to find: ")

pos = s.find(word)

if pos == -1:
    print("Word not found") 
else:
    res = s[:pos].count(' ') + 1 
    print(f"Word found at position: {res}")
