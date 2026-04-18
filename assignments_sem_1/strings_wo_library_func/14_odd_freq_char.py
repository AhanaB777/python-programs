"""
 Write a program to odd Frequency Characters
"""
s = input("Enter a string: ")

freq = {}

# Count frequency manually
for ch in s:
    if ch != " ":        # ignore spaces
        if ch in freq:   # manually increment
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

print("Characters with odd frequency:")

# Print only odd frequency characters
for ch in freq:
    if freq[ch] % 2 != 0:
        print(ch, "=", freq[ch])
