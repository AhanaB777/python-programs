""" Bubble Sort Program """

def bubbleSort(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[10,44,2,14,6,7]
print(bubbleSort(a))
