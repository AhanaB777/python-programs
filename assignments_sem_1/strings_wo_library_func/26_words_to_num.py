"""
Write a program to  convert numeric words to numbers
"""
s = input("Enter number words: ").lower().split()

word_to_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

result = ""

for word in s:
    if word in word_to_num:          # O(1) lookup
        result += str(word_to_num[word])
    else:
        print(f"Invalid word found: {word}")
        exit()

print("Converted number:", int(result))

