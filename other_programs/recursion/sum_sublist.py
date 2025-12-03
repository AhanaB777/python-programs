""" Find sum of each integer element in a list containing other lists using recursion """
def sum_list(l):
    total=0
    for item in l:
        if isinstance(item,list):
            total+=sum_list(item)
        else:
            total+=item
    return total
l=[1,2,[3,[4,5]],6,[7],[8,9]]
res=sum_list(l)
print(f"Sum of all elements in list is {res}")