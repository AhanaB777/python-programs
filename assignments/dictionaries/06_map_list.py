""" 6. Write a Python program to map two lists into a dictionary.
"""

l1=[1,2,3,4,5]
l2=[10,20,30,40,50]
d={}
if len(l1)!=len(l2):
    print("Cannot map two lists")
else:    
    for i in range(0,len(l1)):
        d[l1[i]]=l2[i]
print(d)