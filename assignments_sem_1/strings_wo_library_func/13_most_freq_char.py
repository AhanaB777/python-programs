"""
Write a program to maximum frequency character in String 
"""
s = input("Enter string: ")

# Count frequencies manually
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find max frequency
max_freq = 0
for ch in freq:
    if freq[ch] > max_freq:
        max_freq = freq[ch]

# Print all characters with max frequency
print("Maximum frequency characters: ")
for ch in freq:
    if freq[ch] == max_freq:
        print(ch, "=", max_freq)
