""" Length of a string using recursion """
def length(s):
    if s=='':
        return 0
    else:
        return 1 + length(s[1:])
s=input("Enter a string: ")
res=length(s)
print(f"Length of string {s} is {res}")