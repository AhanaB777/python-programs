import numpy
a=map(int,input().split())
l=list(a) 
arr=numpy.array(l)
print(arr.reshape(3,3))