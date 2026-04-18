"""Task : value pf a polynomial at a given point (value of x)"""
import numpy

a = list(map(float, input().split()))
x=float(input())

print(numpy.polyval(a,x))