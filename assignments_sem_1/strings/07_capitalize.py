"""
Write a program to capitalize the first and last character of each word in a string
"""
s=input("Enter a string : ")
words=s.split()
result=' '.join([
    i[0].upper() + i[1:-1] + i[-1].upper()
    if len(i)>1 else i.upper()
    for i in words
])
print(f"Resulted string: {result}")
