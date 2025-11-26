"""
 Write a program to split and join a string 
"""
s=input("Enter a string: ")

print("Splitting string into specific words: ")
words=s.split()
print(words)

print("Joining string together: ")
new_str = " ".join(words)
print(new_str)