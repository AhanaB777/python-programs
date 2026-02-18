"""19. Write a Python program to print the even numbers from a given list."""
def printEven(l):
    r=[]
    for i in l:
        if i%2==0:
            r.append(i)
    return r

l=[1,2,3,4,5,6,7,8,9,10]
res=printEven(l)
print(res)