""" Reversing a string using recursion """
def rev(s) :
    if s=='':
        return ''
    else:
        return s[-1]+rev(s[:-1])
s=input("Enter a string: ")
res=rev(s)
print(f"Reversed string is {res}")