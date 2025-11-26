"""
Write a program to maximum frequency character in String 
"""
from collections import Counter
s=input("Enter a string: ")

freq=Counter(s)

most_freq=max(freq.values())
for ch in freq :
    if freq[ch] == most_freq:
        print(ch,end=" ")