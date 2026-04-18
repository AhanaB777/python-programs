""" Goal : Find quartiles Q1, Q2, Q3 """

arr=[3 ,7, 8, 5, 12, 14, 21, 15, 18, 14]
n=len(arr)
arr.sort()

if n%2 != 0: # odd length array
    q2=arr[n//2]
    arr1 = arr[:n//2]
    arr2 = arr[(n//2)+1:]

else: # even length array
    q2=(arr[n//2 -1] + arr[n//2])//2
    arr1=arr[:n//2]
    arr2=arr[n//2:]

l=len(arr1)
if l%2 == 0:
    q1=(arr1[l//2 -1] + arr1[l//2])//2
else:
    q1=arr1[l//2]

u=len(arr2)
if u%2 == 0:
    q3=(arr1[u//2 -1] + arr1[u//2])//2
else:
    q3=arr2[u//2]


quart=[]
quart.extend([q1,q2,q3])
for i in quart:
    print(i)