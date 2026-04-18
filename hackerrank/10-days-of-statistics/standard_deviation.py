""" Goal : Find standard deviation of a given array """
import math
arr =[10, 40, 30, 50, 20]
n=len(arr)
mean=sum(arr)/len(arr)
s=0
for i in arr:
    a=(i-mean) ** 2
    s+=a
std_dev=math.sqrt(s/n)
print(round(std_dev,1))