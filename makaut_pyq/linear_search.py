a=[1,12,14,22,2,89,70]
key=12
i=0
while i<len(a):
    if a[i]==key:
        print("key found at ",i+1)
        break
    else:
        i+=1