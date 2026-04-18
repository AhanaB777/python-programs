a=[2,3,4,1]
i=0
for i in range(0,len(a)):
    min_index=i
    for j in range(i+1,len(a)):
        if a[j]<a[min_index]:
            min_index=j
    a[i],a[min_index]=a[min_index],a[i]
print(a)