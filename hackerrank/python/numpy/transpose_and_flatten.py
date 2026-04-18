import numpy
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
arr=numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())