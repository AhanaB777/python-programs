a=[1,2,3,4,5,6,7,8,9]
key=2
low=0
high=len(a)-1
while low<=high:
    mid=(low+high)//2
    if a[mid]==key:
        print("key found at ",mid+1)
        break
    elif a[mid]<key:
        low=mid+1
    else:
        high=mid-1
else:
    print("Key not found")