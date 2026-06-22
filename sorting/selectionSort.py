""" Selection Sort Program """

def selectionSort(a):
    for i in range(0,len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
    
    return a

a=[10,44,2,14,6,7]
b=selectionSort(a)
print(b)
