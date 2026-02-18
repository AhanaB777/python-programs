""" 
7. Write a Python program to get the maximum and minimum values of a dictionary.
"""

d={'a':10,'b':20,'c':30,'d':40}
max_val=0
min_val=min(d.values())
print("Min value: ",min_val)
for i in d.values():
    if i>max_val:
        max_val=i
print("Max value: ",max_val)
