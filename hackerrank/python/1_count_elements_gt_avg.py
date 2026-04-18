"""Count Elements Greater Than Previous Average
Given an array of positive integers: 
Return the number of elements that are strictly greater than the average of all previous elements. 
Skip the first element."""

l=[100,200,150,300]
count=0
for i in range(1,len(l)):
    sum=0
    for j in l[:i+1]:
        sum+=j
    avg=sum/(i+1)
    if l[i]>avg:
        count+=1
print(count)
