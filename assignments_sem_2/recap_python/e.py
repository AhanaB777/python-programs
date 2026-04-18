"""E. Write a function that takes a string as a parameter and returns a string 
with every successive repetitive character replaced with a star(*). For 
example, 'balloon' is returned as 'bal*o*n'. """

def fun(s):
    r=""
    for i in range(0,len(s)):
        if s[i]==s[i-1]:
            r+='*'
        else:
            r+=s[i]
    return r
s="balloon"
result=fun(s)
print(result)
