from itertools import combinations
a=input("Enter (word k) : ").split()
s,k=sorted(a[0]),int(a[1])
l=[]
for i in range(1,k+1):
    l.append(list(combinations(s,i)))
for i in l:
    for j in i:
        print("".join(j))



