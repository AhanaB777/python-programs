"""Q3. Counting Rock Samples 
Juan Marquinho is a geologist and he needs to count rock samples in order to send it to 
a chemical laboratory. He has a problem: The laboratory only accepts rock samples by 
a range of its size in ppm (parts per million).

Juan Marquinho receives the rock samples one by one and he classifies the rock 
samples according to the range of the laboratory. This process is very hard because the 
number of rock samples may be in millions. 
Juan Marquinho needs your help, your task is to develop a program to get the number 
of rocks in each of the ranges accepted by the laboratory. 

Input Format: 
An positive integer S (the number of rock samples) separated by a blank space, and a 
positive integer R (the number of ranges of the laboratory); A list of the sizes of S 
samples (in ppm), as positive integers separated by space R lines where the ith line 
containing two positive integers, space separated, indicating the minimum size and 
maximum size respectively of the ith range. 

Output Format: 
R lines where the ith line containing a single non-negative integer indicating the number 
of the samples which lie in the ith range. 
"""
a=input("Enter value of S and R: ")
a_list=list(map(int,a.split()))
s,r=a_list[0],a_list[1]

x=input().split()
samples=(list(map(int,x)))
print(samples)

ranges=[]
for i in range(r):
    v=input().split()
    v_list=list(map(int,v))
    ranges.append(v_list)
print(ranges)

for i in range(0,r):
    count=0
    for j in samples:
        x=0
        if j>ranges[i][x] and j<ranges[i][x+1] :
            count+=1
        x+=1
    print(f"count {i+1} = {count}")
    

