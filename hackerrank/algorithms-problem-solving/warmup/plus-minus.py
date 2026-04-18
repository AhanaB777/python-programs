arr=[-4, 3, -9, 0, 4, 1]
l=len(arr)
p=n=z=0
for i in range(l):
    if arr[i]==0:
        z+=1
    elif arr[i]>0 :
        p+=1
    else:
        n+=1
print(f"{p/l:.6f}")
print(f"{n/l:.6f}")
print(f"{z/l:.6f}")