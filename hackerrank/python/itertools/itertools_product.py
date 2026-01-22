from itertools import product
a=input("Elements of A: ").split()
A=[]
for i in a:
    A.append(int(i))
b=input("Elements of B: ").split()
B=[]
for i in b:
    B.append(int(i))
l=list(product(A,B,repeat=1))
for i in l:
    print(i,end=" ")