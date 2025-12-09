"""
WAP to print even length words in a string. 
"""
s= input("Enter a string: ")
word=str.split(s)

for i in word :
    if len(i)%2 == 0:
        print(i, end=' ')
        break
else :
    print("No even length string found.")

