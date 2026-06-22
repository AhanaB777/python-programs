""" Modified bubble sort where O(n)=n for best case time-complexity"""

def modifiedBubbleSort(a):
    n=len(a)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                swapped=True
        if not swapped:
            break
    return a

a=[10,44,2,14,6,7]
print(modifiedBubbleSort(a))