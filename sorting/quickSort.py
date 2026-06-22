""" Quick Sort Program """

def partition(a,l,r):
    p=l
    left=l+1
    right=r
    while True:
        while right>=left and a[p]<a[right]:
            right=right-1
        if a[p]>a[right]:
            a[p],a[right]=a[right],a[p]
            p=right
            right-=1
        if right <left:
            return p
        while right>=left and a[p]>a[left]:
            left=left+1
        if a[p]<a[left]:
            a[p],a[left]=a[left],a[p]
            p=left
            left+=1
        if right<left:
            return p

def quickSort(a, l, r):
    if l<r:
        p = partition(a,l,r)
        quickSort(a,l,p-1)
        quickSort(a,p+1,r)
    return a


a=[10,44,2,14,6,7]
b=quickSort(a,0,len(a)-1)
print(b)