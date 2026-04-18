import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    a= numpy.array(arr,float)
    res=a[::-1]
    return res
arr = input().strip().split(' ')
result = arrays(arr)
print(result)