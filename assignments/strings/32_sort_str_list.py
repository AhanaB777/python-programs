"""
 Write a program to sort String list by K character frequency 
"""
words = input("Enter words separated by space: ").split()
k = input("Enter K character: ")

words.sort(key = lambda ele: -ele.count(k))
print("Sorted list:", words)
