"""12. Write a Python function to multiply all the numbers in a list."""
def multList(l):
    m=1
    for i in l:
        m*=i
    return m

l=[1,2,3,4,5]
res=multList(l)
print(res)