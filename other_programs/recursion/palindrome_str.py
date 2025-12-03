""" Checking palindrome using recursion """
def pal(s):
    if s=='':
        return True
    else:
        return s[0]==s[-1] and pal(s[1:-1])
s=input("Enter a string: ")
res=pal(s)
if res:
    print(f"Yes {s} is a palindrome")
else:
    print(f"No {s} is not a palindrome")