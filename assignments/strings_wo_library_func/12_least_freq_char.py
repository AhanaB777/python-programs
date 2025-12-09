"""
Write a program to least Frequent Character in String 
"""
s = input("Enter string: ")

# Count frequencies manually
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Find minimum frequency
min_freq = None
for ch in freq:
    if min_freq is None or freq[ch] < min_freq:
        min_freq = freq[ch]

# Print all characters with minimum frequency
print("Minimum frequency characters:")
for ch in freq:
    if freq[ch] == min_freq:
        print(ch, "=", min_freq)
