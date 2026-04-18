"""F. Write a function thant takes a list of integers as a parameters and
returns third smallest number from the list. For example, 
input:[34,89,54,20,50,76,10,45,90] output: 34 """
def thirdsmallest(l):
    f=min(l)
    s=float('inf')
    for i in range(len(l)):
        if l[i]>f and l[i]<s:
            s=l[i]

    t=float('inf')
    for i in range(len(l)):
        if l[i]>f and l[i]>s and l[i]<t:
            t=l[i]
            
    return t
l=[34,89,54,20,50,76,10,45,90]
res=thirdsmallest(l)
print(res)