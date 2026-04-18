a=[5,6,7]
b=[3,6,10]
res=[]
p,q=0,0
for i in range(len(a)):
    if a[i]>b[i]:
        p+=1
    elif a[i]<b[i]:
        q+=1
    else:
        pass
res=[p,q]
print(res)