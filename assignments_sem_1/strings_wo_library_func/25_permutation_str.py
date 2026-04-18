"""
Write a program to print permutation of a given string using inbuilt function 
"""
from itertools import permutations

s=input("Enter a string: ")

perm = permutations(s)

for p in perm:
    print("".join(p))
