import numpy
n,m=map(int,input().split())
a1=[list(map(int,input().split())) for _ in range(n)]
a2=[list(map(int,input().split())) for _ in range(n)]
a=numpy.array(a1)
b=numpy.array(a2)
print(a+b) 
print(a-b) 
print(a*b)
print(a//b) 
print(a%b) 
print(a**b)