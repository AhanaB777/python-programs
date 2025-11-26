"""
 Write a program to find all close matches of input string from a list 
"""
s=input("Enter a string: ").lower().split()
match_str=input("Enter word to match: ")
for ch in s:
    if ch.startswith(match_str) or match_str.startswith(ch) :
        print("Close matches found: ",ch)

