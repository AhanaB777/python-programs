"""
 Write a program to perform string slicing in Python to rotate a string 
"""
s = input("Enter a string: ")
k = int(input("Enter rotation value: "))

k = k % len(s)

left_rot = s[k:] + s[:k]
right_rot= s[-k:] + s[:-k]

print("Left rotated string:", left_rot)
print("Right rotated string:", right_rot)
