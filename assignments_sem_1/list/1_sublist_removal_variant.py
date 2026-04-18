"""
“Sub-list Removal Variants”

Problem: Given a list of integers, generate all possible lists that result from removing
exactly one element from the original list.

Input: A list of integers: length>=k
Output: A list of lists — each inner list is the original list with one element removed. Order
doesn't matter, but no duplicates, and you must generate all possible unique results.

"""
l=[1,2,3,4]
new_l=[]
for i in range(0,len(l)):
    j=l[:i]+l[i+1:]
    if j not in new_l:
        new_l.append(j)
print(new_l)    
