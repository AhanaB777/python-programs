"""
 Write a program to sort String list by K character frequency 
"""
lst = ["apple", "banana", "mango", "papaya"]
k_ch = input("Enter character to sort by: ")

freqs = []
for word in lst:
    count = 0
    for ch in word:
        if ch == k_ch:
            count += 1
    freqs.append(count)

# simple bubble sort based on freq
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if freqs[j] > freqs[j+1]:
            freqs[j], freqs[j+1] = freqs[j+1], freqs[j]
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("Sorted list:", lst)
