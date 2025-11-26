"""
Write a program to least Frequent Character in String 
"""
s = input("Enter a string : ")
freq = {}
for i in s :
    freq[i] = freq.get(i,0) + 1

min_value = min(freq.values())

print("Least frequent characters are:")
for ch in freq:
    if freq[ch] == min_value:
        print(ch,end=" ")