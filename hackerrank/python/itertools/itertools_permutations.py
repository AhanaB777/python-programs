from itertools import permutations
a=input().split()
s,k=sorted(a[0]),int(a[1])
l=[]
l.append(list(permutations(s,k)))
for i in l:
    for j in i:
        print("".join(j))
