from itertools import combinations_with_replacement
a=input("Enter (word k) : ").split()
s,k=sorted(a[0]),int(a[1])
l=[]
l.append(list(combinations_with_replacement(s,k)))
for i in l:
    for j in i:
        print("".join(j))
