"""
 Write a program to odd Frequency Characters
"""
s = input("Enter a string : ")
freq = {}
for i in s :
    if i!= " ":
        freq[i] = freq.get(i,0) + 1

print("Odd frequency characters are:")
for key,value in freq.items() :
    if value%2 != 0 :
        print(f"Character:{key} with frequency:{value}")
