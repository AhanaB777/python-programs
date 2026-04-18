import numpy
n,m,p=map(int,input().split())
a1=[list(map(int,input().split())) for _ in range(n)]
a2=[list(map(int,input().split())) for _ in range(m)]
arr1=numpy.array(a1)
arr2=numpy.array(a2)
result=numpy.concatenate((arr1,arr2), axis=0)
print(result)