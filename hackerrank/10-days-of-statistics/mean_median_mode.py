""" Goal : Find mean, median, mode of the elements in list x """

n=int(input("Enter number of elements: "))
x=[]
a=input().split()
for i in range(n):
    x.append(int(a[i]))
print(x)

# MEAN
s=sum(x)
m=s/n
print("Mean : ",round(m,1))

# MEDIAN
x.sort()
if n%2 == 0 :
    mid=(x[n//2 -1] + x[n//2])/2
else:
    mid=x[(n-1)//2]
print("Median : ",round(mid,1))

# MODE
# c={}
# for i in set(x):
#     c[i]=x.count(i)

# max_val=max(c.values())
# if max_val==1:
#     mode = min(c.keys())
# else:
#     mode=c[max_val]
c={}
for i in x:
    c[i]=c.get(i,0)+1
print(c)

max_freq=max(c.values())
mode = min(k for k, v in c.items() if v == max_freq)
print("Mode : ",mode)