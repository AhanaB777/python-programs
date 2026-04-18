"""
Write a program for removing i-th character from a string
"""
s = input("Enter a string: ")
i = int(input("Enter the value of ith letter you want to remove: "))
res=""
j=0
for ch in s:
    if j!=i:
        res+=ch
    j+=1    

print(res)