"""
Write a program to generating random strings until a given string is generated 
"""
import random
import string

target = input("Enter the target string: ").lower()
length = len(target)

attempts = 0

while True:
    attempts += 1
    rand_str = "".join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    if rand_str == target:
        break

print("Generated:", rand_str)
print("Attempts:", attempts)
