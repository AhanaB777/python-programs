""" Goal : Find the interquartile range for a given array """
values = [10,40,30,50,20]
freqs = [1,2,3,4,5]
arr=[]
for i in range(len(values)):
    arr.extend([values[i]]*freqs[i])

arr.sort()

n=len(arr)

if n%2 == 0:
    arr1=arr[:n//2]
    arr2=arr[n//2:]

else:
    arr1=arr[:n//2]
    arr2=arr[(n//2)+1:]

l=len(arr1)
if l%2==0 :
    q1=(arr1[l//2 - 1] + arr1[l//2])/2.0
else:
    q1=float(arr1[l//2])

u=len(arr2)
if u%2==0 :
    q3=(arr2[u//2] + arr2[u//2 +1])/2.0
else:
    q3=float(arr2[u//2])


q=q3-q1

print(round(q,1))