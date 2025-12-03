""" Flatten a list using recursion """
def flatten(l):
    l1=[]
    for item in l:
        if isinstance(item,list):
            l1.extend(flatten(item))
        else:
            l1.append(item)
    return l1

l=[1,2,[3,[4,5]],6,[7],[8,9]]
res=flatten(l)
print(f"Sum of all elements in list is {res}")