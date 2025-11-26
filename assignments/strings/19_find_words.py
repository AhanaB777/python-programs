"""
Write a program to find words that are greater than the given length k
"""
s=input("Enter a string : ")
k=int(input("Enter length : "))
res=[words for words in s.split() if len(words)>k]
res_str=" ".join(res)
print(f"Words with length greater than {k} are : {res_str}")