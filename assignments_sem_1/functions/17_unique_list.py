"""17. Write a Python function that takes a list and returns a new list with unique elements of the
first list."""
def uniqueList(l):
    new_l=[]
    for i in l:
        if i not in new_l:
            new_l.append(i)
    return new_l
l=[1,1,2,3,1,4,5,5,4,3,7]
res=uniqueList(l)
print(res)